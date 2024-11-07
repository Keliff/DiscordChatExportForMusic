CREATE TABLE discord_reactions (
    reaction_id INTEGER PRIMARY KEY,
    emoji_id TEXT,
    emoji_name TEXT,
    emoji_code TEXT,
    emoji_image_URL TEXT,
    message_id REFERENCES discord_messages(message_id)
);

CREATE INDEX [IFK_ReactionsMessageId] ON discord_reactions ([message_id]);