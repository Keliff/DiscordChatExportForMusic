CREATE TABLE discord_channels (
    channel_id TEXT PRIMARY KEY,
    channel_type TEXT,
    guild_id TEXT REFERENCES discord_guilds(guild_id),
    channel_category TEXT,
    channel_name TEXT
);
CREATE INDEX [IFK_ChannelGuildId] ON discord_channels ([guild_id]);