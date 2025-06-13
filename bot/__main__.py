from pyrogram import filters
from pyrogram import idle
from bot import bot, data, Config, LOGS, queue, list_handler, words
import asyncio
from bot.database import adduser, napana, add_word
import traceback
import time
from datetime import datetime
from bot.plugins.compress import mediainfo, renew, sysinfo
from bot.plugins.utils import add_task1, on_task_complete
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from .plugins.devtools import exec_message_f, eval_message_f
from .plugins.extras import changeffmpeg , get_ffmpeg, upload_dir, download_dir, get_type, changemode, sample, vshots

START_TIME = datetime.now()

@bot.on_message(filters.incoming & filters.command(["uptime"]))
async def help_message(bot, message):
   if message.from_user.id in Config.AUTH_USERS:
    await bot.send_message(chat_id=message.from_user.id,text=f"**Uᴩᴛiʍᴇ: {str(datetime.now() - START_TIME).split('.')[0]}**")
    return
   else:
    return await message.reply_sticker("CAACAgUAAxkBAAIah2LNhR_vCtyL-YCw8Sf3cO0BCFnqAAKDBgACmStpV778w4PJK2OkHgQ")

@bot.on_message(filters.incoming & filters.command(["start"]))
async def help_message(bot, message):
  if message.chat.id not in Config.AUTH_USERS:
    return
  await adduser(message)
  txt = "**▻ A Siʍᴩlᴇ DB Quᴇuᴇ Vidᴇᴏ Enᴄᴏdᴇr Bᴏᴛ\n▻ Crᴇᴀᴛᴇd By Nirusᴀᴋi (Pᴏwᴇrᴇd By R136ᴀ1)\n► Cᴀn Cᴏʍᴩrᴇss, Gᴇnᴇrᴀᴛᴇ Sᴀʍᴩlᴇ, Sᴄrᴇᴇnshᴏᴛs, Eᴛᴄ.\n► This Bᴏᴛ Is Privᴀᴛᴇ**"
  await bot.send_message(
        chat_id=message.chat.id,
        text=txt,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Jᴏin Fiᴇrᴄᴇnᴇᴛwᴏrᴋ', url='https://t.me/Fiercenetwork')
                ]
            ]
        ),
        reply_to_message_id=message.id,
    )

@bot.on_message(filters.incoming & (filters.video | filters.document))  
async def help_message(bot, message):
  if message.chat.id not in Config.AUTH_USERS:
   return
  query = await message.reply_text("𐌀ძძᤉძ Ⴕჿ Ⴓսᤉսᤉ", quote=True)
  queue.insert_one({'message' : str(message)})
  await napana()
  if len(data) == 1:
   await query.delete()
   await add_task1(data[0])
  
@bot.on_message(filters.incoming & filters.command(["bash"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await exec_message_f(bot, message)
      
@bot.on_message(filters.incoming & filters.command(["vshot"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await vshots(bot, message)      
    
@bot.on_message(filters.incoming & filters.command(["eval"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await eval_message_f(bot, message)
      
@bot.on_message(filters.incoming & filters.command(["renew"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await renew(message)
    
@bot.on_message(filters.incoming & filters.command(["sysinfo"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await sysinfo(message)      
    
@bot.on_message(filters.incoming & filters.command(["getcode"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await get_ffmpeg(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["encode"]))
async def help_message(bot, message):
 if message.chat.id not in Config.AUTH_USERS:
    return await message.reply_text("You Are Not Authorised To Use This Bot 🗑")
 query = await message.reply_text("𐌀ძძᤉძ Ⴕჿ Ⴓսᤉսᤉ", quote=True)
 data.append(message.reply_to_message)
 if len(data) == 1:
    await query.delete()   
    await add_task(message.reply_to_message)    
    
@bot.on_message(filters.incoming & filters.command(["setcode"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await changeffmpeg(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["logs"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await message.reply_document('Encoder@Log.txt')
    
@bot.on_message(filters.incoming & filters.command(["info"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    await mediainfo(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["add"]))      
async def help_message(bot, message):
   if message.from_user.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
   b = message.text
   i = b.split(" ", maxsplit=1)[1]
   await add_word(str(i))
   
@bot.on_message(filters.incoming & filters.command(["getlist"]))      
async def help_message(bot, message):
   if message.from_user.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
   b = words.find({})
   string = ''
   l = 0
   for bc in b:
      string = string + f'{l}.) {bc["word"]}'
      l = l + 1
   await message.reply_text(string)
   
@bot.on_message(filters.incoming & filters.command(["pop"]))      
async def help_message(bot, message):
   if message.from_user.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
   b = message.text
   i = int(b.split(" ", maxsplit=1)[1])
   bcc = words.find({})
   dat = []
   for bc in bcc:
     dat.append(bc)
   words.delete_one(dat[i])
   await message.reply_text(f'{dat[i]}')   
   
@bot.on_message(filters.incoming & filters.command(["clear"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")
    data.clear()
    list_handler.clear()
    queue.delete_many({})
    await message.reply_text("**┌─────═━┈━═─────┐\nCleared The Queue\n└─────═━┈━═─────┘**")
    
@bot.on_message(filters.incoming & filters.command(["ul"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await upload_dir(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["dl"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await download_dir(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["ulmode"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await get_type(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["setul"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await changemode(bot, message)
    
@bot.on_message(filters.incoming & filters.command(["simp"]))
async def help_message(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return await message.reply_text("**You Are Not Authorised To Use This Bot Contact @Nirusaki**")    
    await sample(bot, message)         

async def checkup():
 try:
  await napana()
  if len(data) >= 1:
   LOGS.info("adding task")
   await add_task1(data[0])
 except Exception as e:
  LOGS.info(e)

async def startup():
    await bot.start()
    LOGS.info(f'[Started]: @{(await bot.get_me()).username}')
    x = len(Config.AUTH_USERS)
    for i in range(0, x):
      await bot.send_message(chat_id=Config.AUTH_USERS[i], text="**Ᏼᴏᴛ Ꮋᴀs Ꮢᴇsᴛᴀrᴛᴇd**")
    LOGS.info("STARTING CHECKUP")
    await checkup()
    await idle()
    await bot.stop()
    
bot.loop.run_until_complete(startup())
