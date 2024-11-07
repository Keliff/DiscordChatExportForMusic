CREATE TABLE discord_embeds (
    embed_id INTEGER PRIMARY KEY,
    embed_title TEXT,
    embed_URL TEXT,
    embed_description TEXT,
    embed_author_name TEXT,
    embed_author_URL TEXT,
    embed_thumbnail_URL TEXT,
    message_id TEXT REFERENCES discord_messages(message_id)
);

CREATE INDEX [IFK_EmbedsMessageId] ON discord_embeds ([message_id])