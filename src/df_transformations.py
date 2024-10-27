import os
import math

import pandas as pd
import numpy as np
from urllib.parse import urlparse

def get_file_extension(filename):
    """
    This function takes a filename as input and returns the file extension.
    """
    return os.path.splitext(filename)[1]

def attachments_fileType(df: pd.DataFrame):

    df["attachments_fileType"] = df["attachments_fileName"].apply(lambda x: get_file_extension(x))

    return df

def url_website(url: str):

    try:
        if math.isnan(url):
            return None
    except:
        pass

    parsed_url = urlparse(url).hostname

    if "youtube.com/playlist" in url:
        return "YouTube Playlist"
    elif "youtube" in parsed_url:
        return "YouTube"
    elif "bandcamp" in parsed_url:
        return "BandCamp"
    elif "spotify" in parsed_url:
        return "Spotify"
    elif "twitter" in parsed_url:
        return "Twitter"
    else:
        return parsed_url

def embeds_URL_Tag(df: pd.DataFrame):

    df["embed_url_website"] = df["embed_url"].apply(lambda x: url_website(x) if x != None else x)

    return df

def extract_content_URLs(content: str):

    try:
        if math.isnan(content):
            return None
    except:
        pass

    # Some URLs use markdown syntax or syntax to prevent embeds, this prevents them from being split properly
    content = content.replace('<',' ').replace('>',' ').replace('(',' ').replace(')',' ')

    # Split the string into words
    words = content.split()
    
    # Extract URLs from the words using urlparse()
    urls = []
    for word in words:
        parsed = urlparse(word)
        if parsed.scheme and parsed.netloc:
            urls.append(word)

    if len(urls) == 0:
        return None

    return urls

def top_level_content_URLs(df: pd.DataFrame):

    df["message_content_URLs"] = df["message_content"].apply(lambda x: extract_content_URLs(x))

    return df

def top_level_filter(df: pd.DataFrame):

    return df[df["message_content_URLs"].notna()].reset_index()

def final_explode(df: pd.DataFrame):

    df = df.explode('message_content_URLs')
    df["message_content_website"] = df["message_content_URLs"].apply(lambda x: url_website(x) if x != None else x)

    return df