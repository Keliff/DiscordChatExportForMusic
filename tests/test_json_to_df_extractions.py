from src.json_to_df_extractions import extract_mesages_top_level, messages_top_level_column_drop_list, extract_messages_embeds, messages_embeds_column_drop_list,extract_messages_attachments,messages_attachments_column_drop_list

def test_extract_mesages_top_level(message_type_embed):

    df = extract_mesages_top_level(discord_json_blob=message_type_embed)
    df_columns = df.columns
    
    existing_columns = ['message_id', 'message_type', 'message_timestamp',
       'message_content', 'author_id', 'author_name', 'author_nickname']
    
    df_column_check(df=df, df_columns=df_columns, existing_columns=existing_columns, drop_list=messages_top_level_column_drop_list)

    return

def test_extract_messages_embeds(message_type_embed):

    df = extract_messages_embeds(discord_json_blob=message_type_embed)
    df_columns = df.columns

    existing_columns = ['embed_title', 'embed_url', 'embed_description', 'message_id']

    df_column_check(df=df, df_columns=df_columns, existing_columns=existing_columns, drop_list=messages_embeds_column_drop_list)

    return

def test_extract_messages_attachments(message_type_attachment):

    df = extract_messages_attachments(discord_json_blob=message_type_attachment)
    df_columns = df.columns

    existing_columns = ['attachments_url', 'attachments_fileName',
       'attachments_fileSizeBytes', 'message_id']
    
    df_column_check(df=df, df_columns=df_columns, existing_columns=existing_columns, drop_list=messages_attachments_column_drop_list)

def df_column_check(df, df_columns, existing_columns, drop_list):

    # Re-Name
    for item in existing_columns:
        assert item in df_columns

    # Dropped Columns
    for item in drop_list:
        assert item not in df_columns

    return

# Multiple embeds?

def test_FULL_extract_mesages_top_level(full_json_file):

    df = extract_mesages_top_level(discord_json_blob=full_json_file)

def test_FULL_extract_messages_embeds(full_json_file):

    df = extract_messages_embeds(discord_json_blob=full_json_file)

    #message_id_count_check(df)

    #preview_df(df)

def message_id_count_check(df):

    message_id_count_df = df["message_id"].value_counts(ascending=False).reset_index()
    message_id_count_df = message_id_count_df[message_id_count_df["count"] > 1]

    assert message_id_count_df.empty, f"Messages found w/ more than one Count, {message_id_count_df["message_id"].tolist()}"

def test_FULL_extract_messages_attachments(full_json_file):

    df = extract_messages_attachments(discord_json_blob=full_json_file)

    #message_id_count_check(df)

    #preview_df(df)

def preview_df(df):

    import pandas as pd

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('expand_frame_repr', True)
    pd.set_option('display.max_colwidth', 1000)

    print(df.head())

    assert 1==2