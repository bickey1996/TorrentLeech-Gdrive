from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1344031905:AAGkkzYOYVZBZvy19ZliLuB8jrQ5pYXc-3U"
    APP_ID = 1786730
    API_HASH = "64bdcdc1c2b67fee6d437cc638c46e46"
    OWNER_ID = 12537936
    AUTH_CHANNEL = [-1001362595088]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
type = drive
client_id = 436078733381-9h59acfs6n07nd4snk2ulck4jq6h57t6.apps.googleusercontent.com
client_secret = u6s92dGP_TM8Q5kOaJa9p3HJ
scope = drive
token = {"access_token":"ya29.a0AfH6SMDbWR9qXZ29sWIx6Z5SZ2BWDoKRNiVVnOJkAWgO8uj-K_2Hii-qPMg4riIKgrweC3P-fBvF0WQNcg-uKElcxoJK0WN3taN6SApHGzjNxCyhR0XMAm8Bk5CJ6iAJb4rshQWgB6DkIl3UE-Ptk1PD9fmagZu21LA","token_type":"Bearer","refresh_token":"1//0gUYUKznkI00cCgYIARAAGBASNwF-L9IrvZAVcZcat0Lvvx2lOSWo6to8lORcjiu2y3zRQdznOKYDhFC-7xd4RYkXVDjgBv4WZd4","expiry":"2020-06-30T03:22:07.2461821+05:30"}
"""