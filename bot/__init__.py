
import os, logging, asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv
from pyromod import listen
import pymongo
from pymongo import MongoClient

if os.path.exists('config.env'):
  load_dotenv('config.env')

os.makedirs('encodes/')
os.makedirs('temp/')
os.makedirs('downloads/')

class Config(object):
  BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
  API_ID = int(os.environ.get("API_ID"))
  API_HASH = str(os.environ.get("API_HASH"))
  DOWNLOAD_DIR = str(os.environ.get("DOWNLOAD_DIR"))
  AUTH_USERS = list(set(int(x) for x in os.environ.get("AUTH_USERS").split()))
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
  DATABASE_URL = str(os.environ.get("DATABASE_URL"))
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
  TEMP = 'temp/'
  USERNAME = str(os.environ.get("BOT_USERNAME"))

LOG_FILE_NAME = "Encoder@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

cluster = MongoClient(Config.DATABASE_URL)
db = cluster[Config.USERNAME]
collection = db["data"]
queue = db["queue"]
words = db["words"]
               
data = []
list_handler = []
        
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


bot = Client("Encoder", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, workers=2)

if not Config.DOWNLOAD_DIR.endswith("/"):
  Config.DOWNLOAD_DIR = str() + "/"
if not os.path.isdir(Config.DOWNLOAD_DIR):
  os.makedirs(Config.DOWNLOAD_DIR)

#ses = lt.session()
#ses.listen_on(6881, 6891)
