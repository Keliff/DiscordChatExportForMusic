CREATE TABLE IF NOT EXISTS discord_stickers (
    sticker_id TEXT PRIMARY KEY,
    sticker_name TEXT,
    sticker_format TEXT,
    sticker_URL TEXT,
    message_id TEXT REFERENCES discord_messages(message_id)
);
CREATE INDEX IF NOT EXISTS [IFK_StickersMessageId] ON discord_stickers ([message_id])