"""encrypt oauth account token storage

Revision ID: 919019aead01
Revises: ad99acb9be41
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "919019aead01"
down_revision: str | None = "ad99acb9be41"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Preserve existing token text losslessly as UTF-8 bytes.
    #
    # Application-level re-encryption is intentionally separate from the
    # schema migration because authenticated encryption requires the runtime
    # ENCRYPTION_KEY_SECRET. The H9-18 rotation mechanism upgrades these raw
    # legacy bytes to the current versioned AEAD envelope.
    op.alter_column(
        "oauth_account",
        "access_token",
        existing_type=sa.Text(),
        type_=sa.LargeBinary(),
        existing_nullable=False,
        postgresql_using="convert_to(access_token, 'UTF8')",
    )

    op.alter_column(
        "oauth_account",
        "refresh_token",
        existing_type=sa.Text(),
        type_=sa.LargeBinary(),
        existing_nullable=True,
        postgresql_using="convert_to(refresh_token, 'UTF8')",
    )


def downgrade() -> None:
    # Downgrade is safe only before application-level AEAD migration.
    #
    # Refuse to reinterpret authenticated ciphertext as UTF-8 plaintext.
    bind = op.get_bind()

    encrypted_count = bind.execute(
        sa.text(
            """
            SELECT COUNT(*)
            FROM oauth_account
            WHERE
                substring(access_token from 1 for 10)
                    = convert_to('ONYXAEAD1:', 'UTF8')
                OR (
                    refresh_token IS NOT NULL
                    AND substring(refresh_token from 1 for 10)
                        = convert_to('ONYXAEAD1:', 'UTF8')
                )
            """
        )
    ).scalar_one()

    if encrypted_count:
        raise RuntimeError(
            "Cannot downgrade oauth_account token columns while "
            "ONYXAEAD1 ciphertext is present. Restore the token values "
            "to migration-compatible UTF-8 bytes using the authorized "
            "key and rollback procedure before downgrading the schema."
        )

    op.alter_column(
        "oauth_account",
        "access_token",
        existing_type=sa.LargeBinary(),
        type_=sa.Text(),
        existing_nullable=False,
        postgresql_using="convert_from(access_token, 'UTF8')",
    )

    op.alter_column(
        "oauth_account",
        "refresh_token",
        existing_type=sa.LargeBinary(),
        type_=sa.Text(),
        existing_nullable=True,
        postgresql_using="convert_from(refresh_token, 'UTF8')",
    )
