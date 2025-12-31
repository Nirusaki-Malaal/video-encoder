
import os, logging, asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv
from pyromod import listen
import pymongo
from pymongo import MongoClient

# LOADING SECRETS IN ENVIRONMENT

if os.path.exists('config.env'):
  load_dotenv('config.env')

# LOADING SECRETS IN VARIABLES

class Config(object):
  BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
  API_ID = int(os.environ.get("API_ID"))
  API_HASH = str(os.environ.get("API_HASH"))
  AUTH_USERS = list(set(int(x) for x in os.environ.get("AUTH_USERS").split()))
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
  DATABASE_URL = str(os.environ.get("DATABASE_URL"))
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
  TEMP = 'temp/'
  ROOT_DIRECTORY = ''
  if os.getcwd() != '/':
    ROOT_DIRECTORY = os.getcwd()
  DOWNLOAD_DIR = f"{ROOT_DIRECTORY}/downloads/"
  if not DOWNLOAD_DIR.endswith("/"):
    DOWNLOAD_DIR = str() + "/"
  USERNAME = str(os.environ.get("BOT_USERNAME"))

# DATABASE SHYTTT

cluster = MongoClient(Config.DATABASE_URL)
db = cluster[Config.USERNAME]
collection = db["data"]
queue = db["queue"]
words = db["words"]
data = []
list_handler = []

## CREATING LOGGER

LOG_FILE_NAME = "Encoder@Log.txt"
if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

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

## CREATING BOT OVER HERE

bot = Client("Encoder", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, workers=2)

# CREATING DIRECTORIES IF NOT PRESENT
if not os.path.isdir(f'{Config.ROOT_DIRECTORY}/encodes/'):
   os.makedirs(f'{Config.ROOT_DIRECTORY}/encodes/')
if not os.path.isdir(f'{Config.ROOT_DIRECTORY}/temp/'):
   os.makedirs(f'{Config.ROOT_DIRECTORY}/temp/')
if not os.path.isdir(f'{Config.ROOT_DIRECTORY}/{Config.DOWNLOAD_DIR}'):
   os.makedirs(f'{Config.ROOT_DIRECTORY}/{Config.DOWNLOAD_DIR}')
