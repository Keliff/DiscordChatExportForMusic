CREATE TABLE IF NOT EXISTS discord_embeds (
    embed_id INTEGER PRIMARY KEY,
    embed_title TEXT,
    embed_URL TEXT,
    embed_description TEXT,
    embed_author_name TEXT,
    embed_author_URL TEXT,
    embed_thumbnail_URL TEXT,
    message_id TEXT REFERENCES discord_messages(message_id),
    UNIQUE(message_id,embed_URL)
);

CREATE INDEX IF NOT EXISTS [IFK_EmbedsMessageId] ON discord_embeds ([message_id])