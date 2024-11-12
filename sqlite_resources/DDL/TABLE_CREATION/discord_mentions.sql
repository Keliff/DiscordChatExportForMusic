CREATE TABLE IF NOT EXISTS discord_mentions (
    mention_id INTEGER PRIMARY KEY,
    author_id TEXT REFERENCES discord_authors(author_id),
    message_id TEXT REFERENCES discord_messages(message_id)
);
CREATE INDEX IF NOT EXISTS [IFK_MentionsAuthorId] ON discord_mentions ([author_id]);
CREATE INDEX IF NOT EXISTS [IFK_MentionsMessageId] ON discord_mentions ([message_id]);