CREATE TABLE IF NOT EXISTS discord_authors (
    id INTEGER PRIMARY KEY,
    author_id TEXT,
    author_name TEXT,
    author_is_bot INTEGER,
    author_avatar_URL TEXT,
    UNIQUE(author_id,author_name)
);
CREATE INDEX IF NOT EXISTS [IFK_authorId] ON discord_authors ([author_id]);
CREATE INDEX IF NOT EXISTS [IFK_authorName] ON discord_authors ([author_name]);