from src.df_transformations import attachments_fileType, embeds_URL_Tag, top_level_content_URLs, top_level_filter

def test_attachments_fileType(attachments_csv):

    df = attachments_fileType(attachments_csv)

    assert df.loc[0, 'attachments_fileType'] == '.png'
    assert df.loc[1, 'attachments_fileType'] == '.jpg'

    #print(df.head())
    #assert 1==2

    return

def test_embeds_URL_Tag(embeds_csv):

    df = embeds_URL_Tag(embeds_csv)

    assert df.loc[0, 'embed_url_website'] == 'YouTube Playlist'
    assert df.loc[1, 'embed_url_website'] == 'YouTube'

    #a = df['embed_url_website'].unique()
    #print(a)
    #assert 1==2

def test_top_level_content_URLs(top_level_csv):

    df = top_level_content_URLs(top_level_csv)

    df = top_level_filter(df)

    #preview_df(df)

def preview_df(df):

    import pandas as pd

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('expand_frame_repr', True)
    pd.set_option('display.max_colwidth', 1000)

    #print(df["message_content_URLs"].head().notna())

    print(df.head())

    #df_exploded = df.explode('message_content_URLs')
    #print(df_exploded.head())

    assert 1==2