CREATE TABLE discord_messages (
    message_id TEXT PRIMARY KEY,
    message_type TEXT,
    message_timestamp TEXT,
    message_timestamp_ended TEXT,
    message_content TEXT,
    author_id TEXT REFERENCES discord_authors(author_id)
    channel_id TEXT REFERENCES discord_channel(channel_id),
    guild_id TEXT REFERENCES discord_guild(guild_id)
);
CREATE INDEX [IFK_MessagesAuthorId] ON discord_messages ([author_id]);
CREATE INDEX [IFK_MessagesChannelId] ON discord_messages ([channel_id]);
CREATE INDEX [IFK_MessagesGuildId] ON discord_messages ([guild_id]);