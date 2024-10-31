from src.df_transformations import attachments_fileType, embeds_URL_Tag, top_level_content_URLs, top_level_filter, extract_content_URLs

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

def test_extract_content_URLs():
    """
    Assert all regular / edge case URL patterns can be extracted as individual URLs
    """

    regular_link_test = extract_content_URLs("Since Masters got mention earlier today I do want to reiterate how awesome the remixes are: https://youtu.be/8k1SKLqT02g")
    assert regular_link_test == ['https://youtu.be/8k1SKLqT02g']

    no_embed_test = extract_content_URLs("""
    May I suggest adding this? <https://www.youtube.com/watch?v=YW8-kPTAH8s>
    """)
    assert no_embed_test == ['https://www.youtube.com/watch?v=YW8-kPTAH8s']

    new_line_test = extract_content_URLs("Celeste B-Sides \n\nPurchase: https://radicaldreamland.bandcamp.com/album/celeste-b-sides\n\nRemix by Christa Lee\nhttp://ohpoorpup.bandcamp.com\n\nMastered by Lena Raine")
    assert new_line_test == ['https://radicaldreamland.bandcamp.com/album/celeste-b-sides','http://ohpoorpup.bandcamp.com']

    new_line_at_end_test = extract_content_URLs("THE OFFICIAL KATAMARI DAMACY SOUNDTRACK DROPPED\n\nTHIS IS NOT A DRILL\nhttps://open.spotify.com/album/7KHPyc1crwPfCZekggfw77?si=VBh_lH_4T7S5DOV6f61ZlQ")
    assert new_line_at_end_test == ['https://open.spotify.com/album/7KHPyc1crwPfCZekggfw77?si=VBh_lH_4T7S5DOV6f61ZlQ']

    large_post_multiple_aliasing = extract_content_URLs("""
    I made this for another discord, but there was talk of 6 favorite albums and I wanted to talk about 6 favorite feelings w/ music and examples of that for me\n\n## WOW, SO KELIFF MUSIC TASTE\n\nI love the prompt! I am going to do my spin on it, which is 6 feelings that I crave in music and examples of those.\n\n### 1 - TAKE ME ON A JOURNEY\n\nI like songs that take you on a **journey**, as in, when there are multiple different sections of the song that feel unique. **Hail The Sun** is *very good at this* imo\n\n- [Secret Wars (Reimagined)](<https://www.youtube.com/watch?v=Rg6Og5JOWcQ>) is a favorite of mine\n- [Chunker](<https://www.youtube.com/watch?v=YLexasbqt6A>) is more of their traditional style\n- Honestly [Wake](<https://www.youtube.com/watch?v=Nbb7oa9d7fE&list=PLw21-2ls4hf64GOzOlDddGk1eq4hHgaG_>) is an album I run a lot to\n- Musicals are great for this too honestly, [Life is Looking Up](<https://www.youtube.com/watch?v=NoV66UPGX_Q>) by **Forgive Durden** is one *I love*\n\n### 2 - I LOVE SAPPY MUSIC THAT I CAN DAYDREAM TO\n\n- [Everything To Me](<https://www.youtube.com/watch?v=3y1gPtOD1N8>) and [Easier To Love You](<https://www.youtube.com/watch?v=fJ4dKnu2IvY>) from **Porter Robinson**'s new album have been WONDERFULLY SAPPY TO ME\n\n### 3 - I GOT MARRIED TO THIS SONG\n\nI am physically not allowed to skip this song if it comes up on shuffle. It brings me a special heart full feeling.\n\n- [Somewhere Only We Know](<https://www.youtube.com/watch?v=mer6X7nOY_o>) - **Lily Allen**\n\n### 4 - MUSIC FROM EMOTIONAL PARTS OF GAMES\n\nI want to re-live a part of a game where my heart got utterly destroyed? Whoa music is great for that\n\n- [Vignette: Panacea](<https://www.youtube.com/watch?v=DBsNM2h5yNQ>) - **Disasterpiece** - From Hyperlight Drifter. I cried when this song played in the game\n- [Heart to Heart](<https://www.youtube.com/watch?v=Zd0uYFBf3eA>) - **Beacon Pines**\n    - I cried at multiple parts of this game. This scene is one, the ending is another\n- *OMORI Spoilers*: || [Final Duet](<https://www.youtube.com/watch?v=8ya9EhvcNsA>) HOLY FUCK||\n\n### 5 - MUSIC THAT MAKES ME FEEL LIKE I'M IN A DIFFERENT UNIVERSE\n\nEthereal music that I can lay on the floor, stare up at the ceiling and imagine different ways my life could have gone\n\n- [White Ball](<https://www.youtube.com/watch?v=bnUZ8HcPKsA>) - **Miracle Musical**\n- [My Time](<https://www.youtube.com/watch?v=erzgjfU271g>) - **Bo En**\n    - Specifically the OMORI Trailer version, because that game also fucked me up emotionally (positive)\n\n### 6 - SAD NOSTALGIA\n\nI listened to a LOT of sad music growing up (and I still do). For this feeling, it doesn't need to be a sad song per-se, I just had to be sad while listening to it.\n\n- [At the Bottom of Everything](<https://www.youtube.com/watch?v=2GHyLhbdzN0>) - **Bright Eyes**\n- [Shine (Acoustic)](<https://www.youtube.com/watch?v=YXXuG4gxMNY>) - **Muse**\n    - I listened to this song on loop when I figured out I was gay and was sad about it\n- [I Want to Be Buried In Your Backyard](<https://www.youtube.com/watch?v=-9FDmm_rYjA>) - **Nightmare Of You**\n\n### 7 - BONUS SECTION. SONGS THAT I WILL SING VERY LOUDLY IN THE CAR TO\n\n- [Hannah](<https://www.youtube.com/watch?v=LOyM3xdSurQ>) - **Freelance Whales**\n- [The Graveyard Near The House](<https://www.youtube.com/watch?v=PJdZtoZPIhQ>) - **The Airborne Toxic Event**\n- [Everything All At Once](<https://www.youtube.com/watch?v=Ftn_xcY-t_I>) - **Local Natives**                                      
    """)

    assert large_post_multiple_aliasing == ['https://www.youtube.com/watch?v=Rg6Og5JOWcQ','https://www.youtube.com/watch?v=YLexasbqt6A','https://www.youtube.com/watch?v=Nbb7oa9d7fE&list=PLw21-2ls4hf64GOzOlDddGk1eq4hHgaG_','https://www.youtube.com/watch?v=NoV66UPGX_Q','https://www.youtube.com/watch?v=3y1gPtOD1N8','https://www.youtube.com/watch?v=fJ4dKnu2IvY','https://www.youtube.com/watch?v=mer6X7nOY_o','https://www.youtube.com/watch?v=DBsNM2h5yNQ','https://www.youtube.com/watch?v=Zd0uYFBf3eA','https://www.youtube.com/watch?v=8ya9EhvcNsA','https://www.youtube.com/watch?v=bnUZ8HcPKsA','https://www.youtube.com/watch?v=erzgjfU271g','https://www.youtube.com/watch?v=2GHyLhbdzN0','https://www.youtube.com/watch?v=YXXuG4gxMNY','https://www.youtube.com/watch?v=-9FDmm_rYjA','https://www.youtube.com/watch?v=LOyM3xdSurQ','https://www.youtube.com/watch?v=PJdZtoZPIhQ','https://www.youtube.com/watch?v=Ftn_xcY-t_I']

    return