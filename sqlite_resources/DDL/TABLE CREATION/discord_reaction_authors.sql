CREATE TABLE discord_reaction_authors (
    id INTEGER PRIMARY KEY,
    reaction_id TEXT REFERENCES discord_reactions(reaction_id),
    author_id TEXT REFERENCES discord_authors(author_id)
);

CREATE INDEX [IFK_ReactionAuthorsReactionId] ON discord_reaction_authors ([reaction_id]);
CREATE INDEX [IFK_ReactionAuthorsAuthorId] ON discord_reaction_authors ([author_id]);