import pymongo, os , pyrogram, time
from bot.database import setffmpeg, getffmpeg, adduser, uploadtype, setmode, uploadtype1
from .devtools import progress_for_pyrogram
from .ffmpeg import functions, ffmpeg
from bot import bot, Config, LOGS

async def changeffmpeg(bot, message):
 try:
    await adduser(message)
    changeffmpeg = message.text.split(" ", maxsplit=1)[1]
    await setffmpeg(message, changeffmpeg)
    await message.reply_text(f"**Ꮪuᴄᴄᴇssfully Ꮯhᴀngᴇd Ꭲhᴇ ᎰᎰᎷᏢᎬᏀ-ᏟᏫᎠᎬ Ꭲᴏ**\n```{changeffmpeg}```")
 except Exception as e:
    await message.reply_text(f"Error ```{e}```")
   
async def changemode(bot, message):
 try:
   newmode = message.text.split(" ", maxsplit=1)[1]
   if "video" == newmode:
    await setmode(message, newmode)
    await bot.send_message(text=f"**Ꮪuᴄᴄᴇssfully Ꮯhᴀngᴇd Ꮜᴩlᴏᴀd Ꮇᴏdᴇ Ꭲᴏ**\n```{newmode}```", chat_id=message.from_user.id, reply_to_message_id=message.id)
   elif "document" == newmode:
    await setmode(message, newmode)
    await bot.send_message(text=f"**Ꮪuᴄᴄᴇssfully Ꮯhᴀngᴇd Ꮜᴩlᴏᴀd Ꮇᴏdᴇ Ꭲᴏ**\n```{newmode}```", chat_id=message.from_user.id, reply_to_message_id=message.id)
   else:
    await bot.send_message(text=f"**Ꮜnᴋnᴏwn Ꮜᴩlᴏᴀd Ꭲyᴩᴇ**", chat_id=message.from_user.id, reply_to_message_id=message.id)
 except Exception as e:
    await bot.send_message(text=f"Ꭼrrᴏr \n ```{e}```", chat_id=message.from_user.id, reply_to_message_id=message.id)
   
async def get_type(bot, message):
  upload_type = await uploadtype(message)
  await bot.send_message(text=f"**Ꮜᴩlᴏᴀd Ꮇᴏdᴇ Ꮖs**\n```{upload_type}```", chat_id=message.from_user.id, reply_to_message_id=message.id)
    
async def get_ffmpeg(bot, message):
  ffmpegcodee = await getffmpeg(message)
  await bot.send_message(text=f"**ᎰᎰᎷᏢᎬᏀ ᏟᏫᎠᎬ ᏆᏚ**\n```{ffmpegcodee}```", chat_id=message.from_user.id, reply_to_message_id=message.id)
  

async def upload_dir(client, message):
   u_start = time.time()
   if message.reply_to_message:
    message = message.reply_to_message
   cmd1 = message.text.split(" ", maxsplit=1)[1]
   replyid = message.id
   if os.path.exists(cmd1):
    xhamster = await bot.send_message(text=f"➣ **Ꮜᴩlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 📁", chat_id=message.from_user.id, reply_to_message_id=message.id)
    await client.send_document(
                chat_id=message.chat.id,
                document=cmd1,
                caption=cmd1,
                reply_to_message_id=replyid,
                progress=progress_for_pyrogram,
                progress_args=(client, "➣ **Ꮜᴩlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 📁", xhamster, u_start)
        )
    await xhamster.delete()
   else:
    await bot.send_message(text=f"**Filᴇ Dirᴇᴄᴛᴏry Nᴏᴛ Fᴏund**\n```{cmd1}```", chat_id=message.from_user.id, reply_to_message_id=message.id)
    
async def download_dir(bot, message):
 d_start = time.time()
 if message.reply_to_message:
  reply = await bot.send_message(text=f"➣ **Ꭰᴏwnlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️", chat_id=message.from_user.id, reply_to_message_id=message.id)
  video = await bot.download_media(
        message=message.reply_to_message,
        file_name=Config.TEMP,
        progress=progress_for_pyrogram,
        progress_args=(bot, "➣ **Ꭰᴏwnlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️", reply, d_start)
  )
  await reply.edit(f"Directory Is ```{video}```")
 else:
  await bot.send_message(text=f"**Reply To A File To Download**", chat_id=message.from_user.id, reply_to_message_id=message.id)
  
async def sample(bot, message):
 if message.reply_to_message:
   d_start = time.time()
   reply = await bot.send_message(text="**➣ **Ꭰᴏwnlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️**", chat_id=message.from_user.id, reply_to_message_id=message.id)
   video = await bot.download_media(
        message=message.reply_to_message,
        file_name=Config.TEMP,
        progress=progress_for_pyrogram,
        progress_args=(bot, "➣ **Ꭰᴏwnlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️", reply, d_start)
   )
   path , filename = os.path.split(video)
   output_filename = filename + '_sample.mkv'
   await reply.edit("Generating Sample")
   sample = await functions.sample(filepath=video, output=output_filename)
   caption = filename + " SAMPLE" 
   await upload_handle(bot, message, sample, filename, caption, reply)
   os.remove(video)
   os.remove(sample)
   await reply.delete(True)
 else:
  await bot.send_message(text=f"**Reply To A Video File 📁**", chat_id=message.from_user.id, reply_to_message_id=message.id)
 
async def vshots(bot, message):
  if message.reply_to_message:
   cmd1 = int(message.text.split(" ", maxsplit=1)[1])
   if cmd1 > 30:
    return message.reply_text("Bak BSDK")
   d_start = time.time()
   reply = await bot.send_message(text="**Downloading Video**", chat_id=message.from_user.id, reply_to_message_id=message.id)
   video = await bot.download_media(
        message=message.reply_to_message,
        file_name=Config.TEMP,
        progress=progress_for_pyrogram,
        progress_args=(bot, "**Downloading Video**", reply, d_start)
   )
   for x in range (1, cmd1):
    ss = await functions.screenshot(filepath=video)
    u_start = time.time()
    await reply.edit(f"Starting To Upload The Photo {x}")
    await bot.send_photo(chat_id=message.from_user.id,photo=str(ss), caption=x, progress=progress_for_pyrogram, progress_args=(bot, f"**Uploading Photo {x}**", reply, u_start))
    os.remove(ss)
   os.remove(video)
   reply.delete(True)
  else:
   await message.reply_text("Reply To A Video File") 
  
async def upload_handle(bot, message, filepath, filename, caption, reply):
 try:
  if os.path.exists(filepath) == False:
   return bot.send_message(chat_id=from_user_id, text="➮ **Ꮀilᴇ Nᴏᴛ Ꮀᴏund Ꮜnᴀʙlᴇ Ꭲᴏ Ꮜᴩlᴏᴀd.**")
  mode = await uploadtype(message)
  if mode == "video":
    u_start = time.time()
    thumb = await functions.screenshot(filepath)
    width, height = await ffmpeg.resolution(filepath)
    duration2 = await ffmpeg.duration(filepath)
    s = await bot.send_video(
      video=filepath,
      chat_id=message.from_user.id, 
      supports_streaming=True,
      file_name=filename, 
      thumb=thumb, 
      duration=duration2, 
      width=width, 
      height=height, 
      caption=caption, 
      reply_to_message_id=message.id,
      progress=progress_for_pyrogram,
      progress_args=(
        bot,
        "➣ **Ꮜᴩlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️",
        reply,
        u_start
      )
    )
    os.remove(thumb)
    await s.forward(Config.LOG_CHANNEL)
  elif mode == 'document':
   u_start = time.time()
   s = await bot.send_document(
     document=filepath,
     chat_id=message.from_user.id, 
     force_document=True,
     file_name=filename,   
     caption=caption,
     progress=progress_for_pyrogram,
     reply_to_message_id=message.id,
     progress_args=(
       bot,
       "➣ **Ꮜᴩlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️",
       reply,
       u_start
     )
  )
  await s.forward(Config.LOG_CHANNEL) 
 except Exception as e:
  LOGS.info(e)
  
async def upload_handle1(bot, from_user_id, filepath, filename, caption, reply, reply_to_message):
 mode = await uploadtype1(from_user_id)
 if os.path.exists(filepath) == False:
  return bot.send_message(chat_id=from_user_id, text="➮ **Ꮀilᴇ Nᴏᴛ Ꮀᴏund Ꮜnᴀʙlᴇ Ꭲᴏ Ꮜᴩlᴏᴀd.**")
 if mode == 'document':
  u_start = time.time()
  s = await bot.send_document(
     document=filepath,
     chat_id=from_user_id, 
     force_document=True,
     file_name=filename,   
     caption=caption,
     reply_to_message_id=reply_to_message,
     progress=progress_for_pyrogram,
     progress_args=(bot, "➣ **Ꮜᴩlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️", reply, u_start)
  )
  await s.forward(Config.LOG_CHANNEL) 
 elif mode == 'video':
  u_start = time.time()
  thumb = await functions.screenshot(filepath)
  width, height = await ffmpeg.resolution(filepath)
  duration2 = await ffmpeg.duration(filepath)
  s = await bot.send_video(
      video=filepath,
      chat_id=from_user_id, 
      supports_streaming=True,
      file_name=filename, 
      thumb=thumb, 
      duration=duration2, 
      width=width, 
      height=height, 
      caption=caption, 
      reply_to_message_id=reply_to_message,
      progress=progress_for_pyrogram,
      progress_args=(bot, "➣ **Ꮜᴩlᴏᴀding Ꭲhᴇ Ꮩidᴇᴏ** 🚴‍♀️", reply, u_start)
  )
  os.remove(thumb)
  
