from tobrot.sample_config import Config

class Config(Config):
    TG_BOT_TOKEN= "1344031905:AAGkkzYOYVZBZvy19ZliLuB8jrQ5pYXc-3U"
    APP_ID = 1786730
    API_HASH = "64bdcdc1c2b67fee6d437cc638c46e46"
    AUTH_CHANNEL = [-1001362595088]
    INDEX_LINK = ""
    GLEECH_COMMAND = "gleech"
    YTDL_COMMAND = 'ytdl'
    TELEGRAM_LEECH_COMMAND_G = "tleech"
    CLONE_COMMAND_G = "gclone"
    PYTDL_COMMAND_G = "pytdl"
    STATUS_COMMAND = "status"
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech"
    #fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    # Do not delete [DRIVE] #do not delete [DRIVE] but replace remaining part with yours data..if more data use common sense
    RCLONE_CONFIG = """
[DRIVE]
type = drive
scope = drive
client_id = 436078733381-9h59acfs6n07nd4snk2ulck4jq6h57t6.apps.googleusercontent.com
client_secret = u6s92dGP_TM8Q5kOaJa9p3HJ
token = {"access_token":"ya29.a0AfH6SMDbWR9qXZ29sWIx6Z5SZ2BWDoKRNiVVnOJkAWgO8uj-K_2Hii-qPMg4riIKgrweC3P-fBvF0WQNcg-uKElcxoJK0WN3taN6SApHGzjNxCyhR0XMAm8Bk5CJ6iAJb4rshQWgB6DkIl3UE-Ptk1PD9fmagZu21LA","token_type":"Bearer","refresh_token":"1//0gUYUKznkI00cCgYIARAAGBASNwF-L9IrvZAVcZcat0Lvvx2lOSWo6to8lORcjiu2y3zRQdznOKYDhFC-7xd4RYkXVDjgBv4WZd4","expiry":"2020-06-30T03:22:07.2461821+05:30"}
"""