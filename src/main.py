import json

import pandas as pd

from json_extractions import extract_file_name_discord
from json_to_df_extractions import extract_mesages_top_level, extract_messages_embeds, extract_messages_attachments
from df_transformations import attachments_fileType, embeds_URL_Tag, top_level_content_URLs, top_level_filter, content_URL_explode

def process_top_level(contents: str):

    top_level_df = extract_mesages_top_level(discord_json_blob=contents)
    top_level_df = top_level_content_URLs(top_level_df)
    top_level_df = top_level_filter(top_level_df)
    top_level_df = content_URL_explode(df=top_level_df)
    # The level of uniqueness we care about is through poster and URL, if two poster's both post the same link, that is fine. 
    top_level_df.drop_duplicates(
        subset=['author_id', 'message_content_URLs'], 
        keep='first', 
        inplace=True
    )
    top_level_df.to_csv("top_level.csv", index_label="new_index")
    
    return top_level_df

def process_embeds(contents: str):

    embeds_df = extract_messages_embeds(discord_json_blob=contents)
    embeds_df = embeds_URL_Tag(embeds_df)
    embeds_df.to_csv("embeds_level.csv", index_label="index")

    return embeds_df

def process_attachments(contents: str):

    attachments_df = extract_messages_attachments(discord_json_blob=contents)
    attachments_df = attachments_fileType(attachments_df)
    attachments_df.to_csv("attachments_level.csv", index_label="index")

    return attachments_df

def process_final_export(df: pd.DataFrame):

    column_export_order= [
        'message_timestamp',
        'author_nickname',
        'message_content_website',
        'message_content_URLs',
        'message_content',
        'embed_title',
        'embed_author_name',
        'embed_description',
        'embed_author_url',
        'message_id',
        'message_type',
        'author_id',
        'author_name',
        'reference_messageId',
        'embed_url',
        'embed_url_website',
        'index'
    ]

    # Re-order columns
    df = df[column_export_order]

    # Human friendly export names
    df = df.rename(
        columns={
            "index": "Original Index",
            "message_id": "Message ID",
            "message_type": "Message Type",
            "message_timestamp": "Message Timestamp",
            "message_content": "Message Content",
            "author_id": "Poster ID",
            "author_name": "Poster Username",
            "author_nickname": "Poster Nickname",
            "reference_messageId": "Reference Message ID",
            "message_content_URLs": "Message URL",
            "message_content_website": "Message Website",
            "embed_title": "Embed Title",
            "embed_url": "Embed URL",
            "embed_description": "Embed Description",
            "embed_author_name": "Embed Author",
            "embed_author_url": "Embed Author URL",
            "embed_url_website": "Embed URL Website"
        }
    )

    return df

def main():

    json_file = "keliff_music_export_2024-10-25.json"

    with open(json_file, 'r') as j:
        contents = json.loads(j.read())

    export_file_name = extract_file_name_discord(discord_json_blob=contents,extension='.csv')

    top_level_df = process_top_level(contents=contents)
    embeds_df = process_embeds(contents=contents)

    # Not using Attachment information as of 2024-10-29. Multiple attachments explode the data in an undesirable way anyway. Would need to flatten the data to be a 1-1 join on message_id if wanted in the future
    #attachments_df = process_attachments(contents=contents)
    #merged_df = pd.merge(merged_df, attachments_df, on="message_id", how="left")
    
    # The join to embeds_df needs to happen AFTER the explode. This is because we want to join on TWO elements, message_id and message_content_URLs (w/ embed_url)
    merged_df = pd.merge(
        left=top_level_df, 
        right=embeds_df, 
        how="left",
        left_on=["message_id","message_content_URLs"],
        right_on=["message_id","embed_url"]
    )

    merged_df = process_final_export(merged_df)

    merged_df.to_csv(export_file_name, index_label="Index")

    return

main()