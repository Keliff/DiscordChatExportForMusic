import os
import math

import pandas as pd
import numpy as np
from urllib.parse import urlparse

def get_file_extension(filename: str) -> str:
    """
    This function takes a filename as input and returns the file extension. Assumes only a single period in the file name

    Args:
        filename (str): String filename, including extension

    Returns:
        (str): Extension of the filename, including the '.' character

    """

    return os.path.splitext(filename)[1]

def attachments_fileType(df: pd.DataFrame):
    """
    Create a new column in a DataFrame that identifies the filetype of a filename
    
    Args:
        df (pd.DataFrame): A DataFrame that has the "attachments_fileName" column
    Returns:
        (pd.DataFrame): A DataFrame with the "attachments_fileType" column  
    """

    df["attachments_fileType"] = df["attachments_fileName"].apply(lambda x: get_file_extension(x))

    return df

def url_website(url: str):
    """
    Take in a full url of a website and return a categorical label
    
    Args:
        url (str): 

    Returns:
        Nothing is math.nan returns true. This is done as there are some nan values in the data
        (str): A categorical label of the website
    """

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
        if "/track/" in parsed_url:
            return "Spotify Track"
        elif "/album/" in parsed_url:
            return "Spotify Album"
        else:
            return "Spotify"
    elif "twitter" in parsed_url:
        return "Twitter"
    elif "soundcloud" in parsed_url:
        return "SoundCloud"
    else:
        return "Other" #parsed_url

def embeds_URL_Tag(df: pd.DataFrame) -> pd.DataFrame:
    """
    Give a categorical label to the Embed URL

    Args:
        df (pd.DataFrame): A DataFrame that has the "embed_url" column
    Returns:
        (pd.DataFrame): A DataFrame with the "embed_url_website" column   
    """

    df["embed_url_website"] = df["embed_url"].apply(lambda x: url_website(x) if x != None else x)

    return df

def extract_URLs(content: str) -> list[str]:
    """
    Takes in a string and return a list of URLs

    Args:
        content (str): A string you wish to extract URLs from
    Returns:
        list[str]: If the content contains URLs, return a list of them\n
        None: If content contains no URLs or is NaN
    """

    try:
        if math.isnan(content):
            return None
    except:
        pass

    # Some URLs use markdown syntax or syntax to prevent embeds, this prevents them from being split properly
    content = content.replace('<',' ').replace('>',' ').replace('(',' ').replace(')',' ').replace('\n',' ')

    # Split the string into words based on a space
    words = content.split(' ')
    
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
    """
    Args:
        df (pd.DataFrame): A DataFrame with the "message_content" column
    Returns:
        (pd.DataFrame): A DataFrame with the "message_content_URLs" column
    """

    df["message_content_URLs"] = df["message_content"].apply(lambda x: extract_URLs
(x))

    return df

def top_level_filter(df: pd.DataFrame):
    """
    Filter the Top Level to only posts that contain a valid URL, ignore all other posts
    """

    return df[df["message_content_URLs"].notna()].reset_index()

def content_URL_explode(df: pd.DataFrame, explode_column='message_content_URLs', new_col_name='message_content_website'):
    """
    'Explode' the df on the 'message_content_URLs', which is a list of strings, 'duplicating' each post for each unique url within the list

    Args:
        df (pd.DataFrame): The DataFrame you wish to explode
        explode_column (str): The column that contains a list of strings you wish to explode
        new_col_name (str): The new column name that will contain each individual exploded string from the explode_column
    Returns:
        pd.DataFrame: A DataFrame that has been exploded
    """

    df = df.explode(explode_column)
    df[new_col_name] = df[explode_column].apply(lambda x: url_website(x) if x != None else x)

    return df