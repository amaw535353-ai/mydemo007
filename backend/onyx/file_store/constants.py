MAX_IN_MEMORY_SIZE = 30 * 1024 * 1024  # 30MB
STANDARD_CHUNK_SIZE = 10 * 1024 * 1024  # 10MB chunks

# Marks a blob a content-free chat turn produced, so cleanup can find it by the
# record itself rather than by anything that can expire.
INCOGNITO_SESSION_METADATA_KEY = "incognito_session_id"

# Generated chat images must carry their authorization context on the file
# record itself. This makes the image owner available before the eventual
# tool-call row is persisted and avoids a temporary public-read window.
CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY = "chat_image_gen_owner_user_id"
CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY = "chat_image_gen_chat_session_id"
