import pymongo, os, pyrogram, asyncio, json
from pymongo import MongoClient
from bot import db, collection, Config, LOGS, queue,data, list_handler, words


ffmpeg = "-map 0:v -map 0:a? -map 0:s:0? -c:v libx265 -pix_fmt yuv420p -x265-params 'no-info=1' -crf 30.7 -vf 'drawtext=fontfile=Aclonica.ttf:fontsize=25:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=FIERCENETWORK' -s 854x480 -preset medium -metadata title='Visit For More Movies [t.me/Fiercenetwork]'  -metadata:s:v title='Visit Website [Fiercenetwork] t.me/Fiercenetwork] - 480p - HEVC - 8bit'  -metadata:s:a title='[Visit t.me/Fiercenetwork] - AAC - 40k kbps' -metadata:s:s title='[Fiercenetwork Subs]' -c:a libfdk_aac -ab 50k -ac 2 -profile:a aac_he_v2 -c:s copy"

async def adduser(message):
  if collection.find_one({'_id' : int(message.from_user.id)}):
   LOGS.info("YES")
  else:
   post = {'_id' : int(message.from_user.id), 'ffmpeg' : ffmpeg, 'mode' : 'document'}
   x = collection.insert_one(post)
    
async def setffmpeg(message, ffmpeg1):
  collection.update_one({'_id': int(message.from_user.id)}, {'$set': {'ffmpeg': ffmpeg1}})

async def getffmpeg(message):
  dic = collection.find_one({'_id' : int(message.from_user.id)})
  ffmpeg = dic['ffmpeg']
  return ffmpeg

async def getffmpeg1(message):
  dic = collection.find_one({'_id' : int(message)})
  ffmpeg = dic['ffmpeg']
  return ffmpeg


async def uploadtype(message):
  dic = collection.find_one({'_id' : int(message.from_user.id)})
  mode = dic['mode']
  return mode


async def uploadtype1(message):
  dic = collection.find_one({'_id' : int(message)})
  mode = dic['mode']
  return mode

async def setmode(message, mode):
  collection.update_one({'_id': int(message.from_user.id)}, {'$set': {'mode': mode}})
  
async def napana():
  queries = queue.find({})
  for query in queries:
   que = str(query["message"])
   b = json.loads(que)
   if not query["_id"] in list_handler: 
    list_handler.append(query["_id"])
   if not b in data:
    data.append(b)
    
async def add_word(word):
   post = {'word' : str(word)}
   x = words.insert_one(post)
