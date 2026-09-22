from functools import lru_cache
from os import urandom

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from onyx.configs.app_configs import ENCRYPTION_KEY_SECRET
from onyx.utils.logger import setup_logger
from onyx.utils.variable_functionality import fetch_versioned_implementation

logger = setup_logger()


# Explicit ciphertext envelope for authenticated-encryption records.
#
# Legacy records have no prefix:
# - raw UTF-8 when no key was configured;
# - IV || AES-CBC ciphertext when the historical EE implementation was keyed.
_AEAD_MAGIC = b"ONYXAEAD1:"
_AEAD_NONCE_SIZE = 12
_AEAD_AAD = b"onyx-secret-storage:v1"


@lru_cache(maxsize=2)
def _get_trimmed_key(key: str) -> bytes:
    encoded_key = key.encode()
    key_length = len(encoded_key)
    if key_length < 16:
        raise RuntimeError("Invalid ENCRYPTION_KEY_SECRET - too short")

    # Preserve historical key-selection behavior for compatibility.
    valid_lengths = [32, 24, 16]
    for size in valid_lengths:
        if key_length >= size:
            return encoded_key[:size]

    raise AssertionError("unreachable")


def _is_current_encryption_format(input_bytes: bytes) -> bool:
    return input_bytes.startswith(_AEAD_MAGIC)


def _encrypt_string(input_str: str, key: str | None = None) -> bytes:
    effective_key = key if key is not None else ENCRYPTION_KEY_SECRET

    # Legacy/development compatibility. Production hardening requirements must
    # independently require ENCRYPTION_KEY_SECRET where encrypted-at-rest
    # secret storage is expected.
    if not effective_key:
        return input_str.encode()

    trimmed = _get_trimmed_key(effective_key)
    nonce = urandom(_AEAD_NONCE_SIZE)

    encrypted = AESGCM(trimmed).encrypt(
        nonce,
        input_str.encode(),
        _AEAD_AAD,
    )

    return _AEAD_MAGIC + nonce + encrypted


def _decrypt_current_aead(input_bytes: bytes, key: str) -> str:
    payload = input_bytes[len(_AEAD_MAGIC) :]

    # nonce + at least the 16-byte GCM authentication tag
    if len(payload) < _AEAD_NONCE_SIZE + 16:
        raise ValueError("Invalid authenticated-encryption payload")

    nonce = payload[:_AEAD_NONCE_SIZE]
    encrypted = payload[_AEAD_NONCE_SIZE:]

    try:
        plaintext = AESGCM(_get_trimmed_key(key)).decrypt(
            nonce,
            encrypted,
            _AEAD_AAD,
        )
        return plaintext.decode()
    except (InvalidTag, UnicodeDecodeError, ValueError) as exc:
        raise ValueError(
            "Authenticated secret decryption failed"
        ) from exc


def _decrypt_legacy_cbc(input_bytes: bytes, key: str) -> str:
    trimmed = _get_trimmed_key(key)

    try:
        iv = input_bytes[:16]
        encrypted_data = input_bytes[16:]

        cipher = Cipher(
            algorithms.AES(trimmed),
            modes.CBC(iv),
            backend=default_backend(),
        )
        decryptor = cipher.decryptor()
        decrypted_padded_data = (
            decryptor.update(encrypted_data)
            + decryptor.finalize()
        )

        unpadder = padding.PKCS7(
            algorithms.AES.block_size
        ).unpadder()
        decrypted_data = (
            unpadder.update(decrypted_padded_data)
            + unpadder.finalize()
        )

        return decrypted_data.decode()

    except (ValueError, UnicodeDecodeError):
        raise


def _decrypt_bytes(input_bytes: bytes, key: str | None = None) -> str:
    effective_key = key if key is not None else ENCRYPTION_KEY_SECRET

    # A versioned encrypted record must never degrade into raw decoding simply
    # because the process lacks the key.
    if _is_current_encryption_format(input_bytes):
        if not effective_key:
            raise ValueError(
                "Encrypted secret requires ENCRYPTION_KEY_SECRET"
            )
        return _decrypt_current_aead(
            input_bytes,
            effective_key,
        )

    # Legacy plaintext compatibility.
    if not effective_key:
        return input_bytes.decode()

    # Unversioned keyed data is interpreted as historical AES-CBC.
    try:
        return _decrypt_legacy_cbc(
            input_bytes,
            effective_key,
        )

    except (ValueError, UnicodeDecodeError):
        if key is not None:
            # Explicit-key operations such as rotation must fail closed.
            raise

        # Default read path preserves historical plaintext migration support.
        logger.warning(
            "Legacy AES-CBC decryption failed — falling back to raw decode. "
            "Run the re-encrypt secrets script to migrate legacy data."
        )

        try:
            return input_bytes.decode()

        except UnicodeDecodeError:
            raise ValueError(
                "Data is neither valid legacy ciphertext nor UTF-8 plaintext. "
                "Run the re-encrypt secrets script with the correct previous key."
            ) from None


def encrypt_string_to_bytes(
    input_str: str,
    key: str | None = None,
) -> bytes:
    versioned_encryption_fn = fetch_versioned_implementation(
        "onyx.utils.encryption",
        "_encrypt_string",
    )
    return versioned_encryption_fn(
        input_str,
        key=key,
    )


def decrypt_bytes_to_string(
    input_bytes: bytes,
    key: str | None = None,
) -> str:
    versioned_decryption_fn = fetch_versioned_implementation(
        "onyx.utils.encryption",
        "_decrypt_bytes",
    )
    return versioned_decryption_fn(
        input_bytes,
        key=key,
    )


def test_encryption() -> None:
    test_string = "Onyx is the BEST!"
    encrypted_bytes = encrypt_string_to_bytes(test_string)
    decrypted_string = decrypt_bytes_to_string(encrypted_bytes)

    if test_string != decrypted_string:
        raise RuntimeError(
            "Encryption decryption test failed"
        )
