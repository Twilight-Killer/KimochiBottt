
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "15672532" # integer value, dont use ""
    API_HASH = "4827d34e2c376fd3cc5a21db22e76ceb"
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1128130156 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "HaoTogelLivedraw"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/c28fca8e18d76ca6768fb.jpg"
    EVENT_LOGS = (-1001526106346)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= ""
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="1696771874-fallen-cbxc99cxbc" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1696771874]  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = [1696771874]  # User id of support users
    TIGERS = [1696771874]  # User id of tiger users
    WOLVES = [1696771874]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
