import pandas as pd
from typing import Callable

# Instantiated at the highest level in order to be imported into pytest functions
messages_top_level_column_drop_list = [
    "timestampEdited",
    "callEndedTimestamp",
    "isPinned",
    "attachments",
    "embeds",
    "stickers",
    "reactions",
    "mentions",
    "author_roles",
    "author_avatarUrl",
    "author_color",
    "author_isBot",
    "author_discriminator",
    "reference_channelIdindex_label",
    "reference_guildId",
    "reference_channelId"
]

messages_embeds_column_drop_list = [
    "timestamp", 
    "images", 
    "color",
    "fields", # Extra embed info. Such as 'Likes / Retweets' for Twiter post
    "thumbnail_url", 
    "thumbnail_width", 
    "thumbnail_height",
    "video_url",
    "video_width",
    "video_height",
    "author_iconUrl",
    "footer_text",
    "footer_iconUrl",
    "image_url",
    "image_width",
    "image_height"
]

# Attachment info is pre-pended intentionally to be able to access the id column as meta information
messages_attachments_column_drop_list = [
    "attachments_id",
]

def extract_mesages_top_level(discord_json_blob: str, extraction_level="messages", column_separator="_") -> pd.DataFrame:
    """
    Within the DiscordChatExporter .json blob, there is a lot of information about messages. This information is nested, containing information about attachments, embeds, and more. This function is concerned with the top level of message information including but not limited to:
    - Message ID
    - Author
    - Content of the message

    This is a higher-level function, dropping uncessary columns to speed up processing and re-naming columns with a consistent prefix

    Args:
        discord_json_blob (str): Json Blob. Assumed to have been parsed by json.loads()
        extraction_level (str): Assumes we sent in the entire json blob, meaning there is a particular key we wish to focus on. This is the extraction_level
        column_separator (str): 

    Returns:
        pd.DataFrame: 

    """

    return extract_messages_pattern(
        json_normalize_dict={
            "data": discord_json_blob[extraction_level],
            "sep": column_separator
        },
        drop_function=messages_top_level_column_drop,
        rename_function=messages_top_level_rename
    )

def df_drop_if_exists(df:pd.DataFrame, drop_list: list[str]) -> None:

    thisFilter = df.filter(drop_list)
    df.drop(thisFilter, inplace=True, axis=1)

    return

def messages_top_level_column_drop(df:pd.DataFrame) -> None:

    df_drop_if_exists(df=df,drop_list=messages_top_level_column_drop_list)

    return

def df_add_prefix_exclude(df: pd.DataFrame, prefix:str, exclude_columns: list[str]):

    return df.rename(columns={c: prefix+c for c in df.columns if c not in exclude_columns})

def messages_top_level_rename(df: pd.DataFrame) -> pd.DataFrame:

    return df_add_prefix_exclude(df=df,prefix="message_",exclude_columns=['author_id', 'author_name', 'author_discriminator',
       'author_nickname', 'author_color', 'author_isBot', 'author_roles',
       'author_avatarUrl','reference_messageId'])

def extract_messages_embeds(discord_json_blob: str, extraction_level="messages", embed_level="embeds", meta_info=["id"], column_separator="_") -> pd.DataFrame:
    """
    Embed information is nested within Messages. The goal of this function is to extract that information with a key to be able to join back to the main DataFrame in a structured way
    """

    return extract_messages_pattern(
        # pd.json_normalize can look at a nested element (embeds) and then also add a higher level piece of info (meta id) to join back to. The id here is re-named as message_id to be consistent and there for joined on later
        json_normalize_dict={
            "data": discord_json_blob[extraction_level],
            "sep": column_separator,
            "record_path": embed_level,
            "meta": meta_info
        },
        drop_function=extract_messages_embeds_column_drop,
        rename_function=extract_messages_embeds_rename
    )

def extract_messages_embeds_column_drop(df: pd.DataFrame) -> None:

    df_drop_if_exists(df=df,drop_list=messages_embeds_column_drop_list)

    return

def extract_messages_embeds_rename(df: pd.DataFrame) -> pd.DataFrame:

    df = df_add_prefix_exclude(df=df,prefix="embed_",exclude_columns=['id'])

    # We want to join on message_id within another DataFrame
    df.rename({"id": "message_id"}, axis=1, inplace=True)

    return df

def extract_messages_attachments(discord_json_blob: str, extraction_level="messages", attachment_level="attachments", meta_info=["id"], column_separator="_"):
    """
    Attachment information is nested within Messages. The goal of this function is to extract that information with a key to be able to join back to the main DataFrame in a structured way
    """

    return extract_messages_pattern(
        json_normalize_dict={
            "data": discord_json_blob[extraction_level],
            "sep": column_separator,
            "record_path": attachment_level,
            "meta": meta_info,
            "record_prefix": f"{attachment_level}_"
        },
        drop_function=extract_messages_attachments_column_drop,
        rename_function=extract_messages_attachments_rename
    )

def extract_messages_attachments_column_drop(df: pd.DataFrame):

    df_drop_if_exists(df=df,drop_list=messages_attachments_column_drop_list)

    return

def extract_messages_attachments_rename(df: pd.DataFrame):

    # We want to join on message_id within another DataFrame
    df.rename({"id": "message_id"}, axis=1, inplace=True)

    return df

def extract_messages_pattern(json_normalize_dict: dict, drop_function: Callable, rename_function: Callable,):
    """
    We are following the same ETL pattern multiple times, abstracted here:

    - Normalize Data to some level
    - Call a Drop Function
    - Call a Re-Name Function


    """

    temp_df = pd.json_normalize(**json_normalize_dict)

    drop_function(temp_df)
    if rename_function is not None:
        temp_df = rename_function(df=temp_df)

    return temp_df