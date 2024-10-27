
from src.json_extractions import extract_file_name_discord

def test_extract_file_name_discord(file_name_json):
    
    file_name_compare = "Guild Name_Main_channelName_1357_2024-10-26.csv"

    assert extract_file_name_discord(discord_json_blob=file_name_json, extension='.csv') == file_name_compare

