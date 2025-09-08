CREATE TABLE IF NOT EXISTS discord_logging (
    logging_id INTEGER PRIMARY KEY,
    logging_date TEXT,
    logging_table TEXT,
    logging_table_id TEXT,
    logging_file_name TEXT,
    logging_process TEXT
);