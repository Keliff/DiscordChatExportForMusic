import pytest
import json
import os

import pandas as pd

@pytest.fixture(scope="session")
def file_name_json():
    return json.loads("""
    {
    "guild": {
        "id": "xxxx",
        "name": "Guild Name",
        "iconUrl": ""
    },
    "channel": {
        "id": "1234",
        "type": "",
        "categoryId": "",
        "category": "Main",
        "name": "channelName",
        "topic": null
    },
    "exportedAt": "2024-10-26T10:22:32.1307262-05:00",
    "messageCount": 1357
    }
    """)

@pytest.fixture(scope="session")
def message_type_attachment():
    return json.loads(
    """
    {
    "messages": [
    {
      "id": "1091115849500336229",
      "type": "Default",
      "timestamp": "2023-03-30T16:44:50.473-05:00",
      "timestampEdited": null,
      "callEndedTimestamp": null,
      "isPinned": false,
      "content": ":lgwWoah:",
      "author": {
        "id": "185504812874465280",
        "name": "deltawhiskey",
        "discriminator": "0000",
        "nickname": "Delta Whiskey",
        "color": "#FD7875",
        "isBot": false,
        "roles": [
          {
            "id": "893948505998106684",
            "name": "Roo Crew",
            "color": "#FD7875",
            "position": 9
          },
          {
            "id": "980964075464978482",
            "name": "Twitch Subscriber",
            "color": null,
            "position": 6
          },
          {
            "id": "980964075464978483",
            "name": "Twitch Subscriber: Tier 1",
            "color": null,
            "position": 5
          },
          {
            "id": "1128812376226013224",
            "name": "Nardo Enjoyers",
            "color": "#F1C40F",
            "position": 2
          }
        ],
        "avatarUrl": "https://cdn.discordapp.com/avatars/185504812874465280/6e34a2302ee2444951336c61ac0fa9a0.png?size=512"
      },
      "attachments": [
        {
          "id": "1091115849068335114",
          "url": "https://cdn.discordapp.com/attachments/890591223625162792/1091115849068335114/20230330_171036.jpg?ex=671e0b92&is=671cba12&hm=c4e7b8945a4587cc9cd361c935a354b2645fb026391c766b7c975f3f01f69e76&",
          "fileName": "20230330_171036.jpg",
          "fileSizeBytes": 2519070
        }
      ],
      "embeds": [],
      "stickers": [],
      "reactions": [],
      "mentions": []
    }
    ]
    }
    """
    )

@pytest.fixture(scope="session")
def message_type_embed():
    return json.loads(
    """
    {
    "messages": [
    {
      "id": "1064973902150897706",
      "type": "Default",
      "timestamp": "2023-01-17T12:26:04.531-06:00",
      "timestampEdited": null,
      "callEndedTimestamp": null,
      "isPinned": false,
      "content": "(mild epilepsy warning) https://www.youtube.com/watch?v=V-uTOWL8X0w",
      "author": {
        "id": "204793922424274944",
        "name": "goldenpelt",
        "discriminator": "0000",
        "nickname": "Goldenpelt",
        "color": "#FD7875",
        "isBot": false,
        "roles": [
          {
            "id": "893948505998106684",
            "name": "Roo Crew",
            "color": "#FD7875",
            "position": 9
          },
          {
            "id": "980964075464978482",
            "name": "Twitch Subscriber",
            "color": null,
            "position": 6
          },
          {
            "id": "980964075464978483",
            "name": "Twitch Subscriber: Tier 1",
            "color": null,
            "position": 5
          },
          {
            "id": "1128812376226013224",
            "name": "Nardo Enjoyers",
            "color": "#F1C40F",
            "position": 2
          }
        ],
        "avatarUrl": "https://cdn.discordapp.com/avatars/204793922424274944/8e126388ac194196fd5136f91617e5ba.png?size=512"
      },
      "attachments": [],
      "embeds": [
        {
          "title": "Anonymouz - River (ヴィンランド・サガ [VINLAND SAGA] SEASON 2 OPテーマ)",
          "url": "https://www.youtube.com/watch?v=V-uTOWL8X0w",
          "timestamp": null,
          "description": "Anonymouz - River\nStream Now!▶https://Anonymouz.lnk.to/River\n*English subtitles available♡\n*日本語(佐賀弁SAGA)字幕もご覧ください♡\n\nTVアニメ「ヴィンランド・サガ」\nVINLAND SAGA SEASON 2 オープニング・テーマ\nOrder your package here▶https://www.amazon.co.jp/River-%E3%83%A1%E3%82%AC%E3%82%B8%E3%83%A3%E3%82%B1%E4%BB%98-Anonymouz/dp/B0BRZWB729/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%...",
          "color": "#FF0000",
          "author": {
            "name": "Anonymouz アノニムーズ",
            "url": "https://www.youtube.com/channel/UCe0h32Y4Po84iLubCviKRug"
          },
          "thumbnail": {
            "url": "https://images-ext-1.discordapp.net/external/W9_EMSzbmQBnx1oazzm4XA5QNrMfZQdW_ORNZtdH2wc/https/i.ytimg.com/vi/V-uTOWL8X0w/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "video": {
            "url": "https://www.youtube.com/embed/V-uTOWL8X0w",
            "width": 960,
            "height": 720
          },
          "images": [],
          "fields": []
        }
      ],
      "stickers": [],
      "reactions": [],
      "mentions": []
    }]
    }"""
    # Needed because there are japanese characters w/in the json
    ,strict=False
    )

@pytest.fixture(scope="session")
def full_json_file():

    with open("keliff_music_export_2024-10-25.json", 'r') as j:
        contents = json.loads(j.read())

    return contents

@pytest.fixture(scope="session")
def attachments_csv():
    return pd.read_csv("attachments_level.csv")

@pytest.fixture(scope="session")
def embeds_csv():
    return pd.read_csv("embeds_level.csv")

@pytest.fixture(scope="session")
def top_level_csv():
    return pd.read_csv("top_level.csv")