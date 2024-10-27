import json

def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        raise ValueError

def raise_error_if_key_not_found(json_data: str, key: str) -> None:
    if key not in json_data:
        raise KeyError(f"Key '{key}' not found in JSON data.")
    return json_data[key]

def extract_file_name_discord(discord_json_blob: str, extension="") -> str:
    """
    Return a formatted file name from a discord json blob, specifically from the DiscordChatExporter.

    Args:
        discord_json_blob (str): Json Blob. Assumed to have been parsed by json.loads()

    Returns:
        str: Formatted File Name
    """

    guild_blob = discord_json_blob["guild"]
    channel_blob = discord_json_blob["channel"]
    # First 10 character of a timestamp is YYYY-MM-DD
    exported_at = discord_json_blob["exportedAt"][:10]
    message_count = str(discord_json_blob["messageCount"])

    return "_".join( (guild_blob["name"],channel_blob["category"],channel_blob["name"], message_count, exported_at ) ) + extension

def extract_messages_embeds():

    return