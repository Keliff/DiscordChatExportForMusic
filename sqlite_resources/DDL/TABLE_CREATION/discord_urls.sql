CREATE TABLE IF NOT EXISTS discord_urls (
    id INTEGER PRIMARY KEY,
    discord_URL TEXT,
    message_id REFERENCES discord_messages(message_id)
);

CREATE INDEX IF NOT EXISTS [IFK_URLsMessageId] ON discord_urls ([message_id])