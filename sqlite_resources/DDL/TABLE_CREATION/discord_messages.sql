CREATE TABLE IF NOT EXISTS discord_messages (
    message_id TEXT PRIMARY KEY,
    message_type TEXT,
    message_timestamp TEXT,
    message_content TEXT,
    author_id TEXT REFERENCES discord_authors(author_id),
    channel_id TEXT REFERENCES discord_channels(channel_id),
    guild_id TEXT REFERENCES discord_guilds(guild_id)
);
CREATE INDEX IF NOT EXISTS [IFK_MessagesAuthorId] ON discord_messages ([author_id]);
CREATE INDEX IF NOT EXISTS [IFK_MessagesChannelId] ON discord_messages ([channel_id]);
CREATE INDEX IF NOT EXISTS [IFK_MessagesGuildId] ON discord_messages ([guild_id]);