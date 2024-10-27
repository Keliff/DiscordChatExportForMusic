import json

import pandas as pd

from json_to_df_extractions import extract_mesages_top_level, extract_messages_embeds, extract_messages_attachments
from df_transformations import attachments_fileType, embeds_URL_Tag, top_level_content_URLs, top_level_filter, final_explode

def process_top_level(contents: str):

    top_level_df = extract_mesages_top_level(discord_json_blob=contents)
    top_level_content_URLs(top_level_df)
    top_level_df = top_level_filter(top_level_df)
    top_level_df.to_csv("top_level.csv", index_label="index")

    return top_level_df

def process_embeds(contents: str):

    embeds_df = extract_messages_embeds(discord_json_blob=contents)
    embeds_URL_Tag(embeds_df)
    embeds_df.to_csv("embeds_level.csv", index_label="index")

    return embeds_df

def process_attachments(contents: str):

    attachments_df = extract_messages_attachments(discord_json_blob=contents)
    attachments_fileType(attachments_df)
    attachments_df.to_csv("attachments_level.csv", index_label="index")

    return attachments_df

def main():

    json_file = "keliff_music_export_2024-10-25.json"

    with open(json_file, 'r') as j:
        contents = json.loads(j.read())

    top_level_df = process_top_level(contents=contents)

    embeds_df = process_embeds(contents=contents)

    attachments_df = process_attachments(contents=contents)

    merged_df = pd.merge(top_level_df, embeds_df, on="message_id", how="left")
    merged_df = pd.merge(merged_df, attachments_df, on="message_id", how="left")
    merged_df = final_explode(df=merged_df)
    merged_df.to_csv("final.csv", index_label="index")

    return

main()