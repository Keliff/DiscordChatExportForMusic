CREATE TABLE IF NOT EXISTS discord_author_nicknames (
    author_nickname_id INTEGER PRIMARY KEY,
    author_id TEXT REFERENCES discord_author(author_id),
    nickname TEXT
);