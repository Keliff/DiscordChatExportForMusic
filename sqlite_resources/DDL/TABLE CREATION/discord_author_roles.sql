CREATE TABLE discord_author_roles (
    author_role_id INTEGER PRIMARY KEY,
    author_id TEXT REFERENCES discord_author(author_id),
    author_role_name TEXT
);

CREATE INDEX [IFK_AuthorRolesAuthorId] ON discord_author_roles ([author_id])