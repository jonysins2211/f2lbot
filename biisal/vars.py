# (c) adarsh-goel (c) @biisal @AmRobots_Bots www.hostingup.in
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Mʟ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://t.me/Movie_loverzz"
bisal_grp = "https://t.me/+Ld8N-bvIbCJjODhl"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '27258953'))
    API_HASH = str(getenv('API_HASH', '0add43fc460daca0a86077989cfc414f'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7243323940:AAF0f5EGewMm6c67o5KanucJBGGzgfcWxDQ'))
    name = str(getenv('name', 'Mlfiletolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002005906539'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002005906539'))
    PORT = int(getenv('PORT', '9005')) #(Here, enter the hosting port you received from HostingUp, which should start From 9000)
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')) #(DO NOT CHANGE IF U DEPLOY YOUR BOT ON HOSTINGUP VPS)
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "949657126").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', '@TonYStarkk616'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', 'bots.hostingup.icu:9005/') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    HAS_SSL = False
    FQDN = 'bots.hostingup.icu:9005' #(Here, enter the domain and hosting port you received from HostingUp. If you're using your own, enter that, but make sure to use the domain name, not the IP address, and include the port as well.)
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://primebaby11220:TuGa0I5ZsiC8mp5A@cluster0.df4rivj.mongodb.net/?retryWrites=true&w=majorit'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'MovieEntertainment4u')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @Movie_loverzz ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
