CREATE TABLE IF NOT EXISTS discord_attachments (
    attachment_id TEXT PRIMARY KEY,
    attachment_URL TEXT,
    attachment_file_name TEXT,
    attachment_file_size_bytes INTEGER,
    message_id REFERENCES discord_messages(message_id)
);

CREATE INDEX IF NOT EXISTS [IFK_AttachmentsMessageId] ON discord_attachments ([message_id]);