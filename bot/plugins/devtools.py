import pyrogram, subprocess, traceback, sys ,json, math, os, io, asyncio, time
from bot import bot, Config, LOGS
FINISHED_PROGRESS_STR = "▣"
UN_FINISHED_PROGRESS_STR = "□"
MAX_MESSAGE_LENGTH = 4096

async def exec_message_f(client, message):
  if message.from_user.id in Config.AUTH_USERS:
    if True:
        DELAY_BETWEEN_EDITS = 0.3
        PROCESS_RUN_TIME = 100
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_id = message.id
        if message.reply_to_message:
            reply_to_id = message.reply_to_message.id

        start_time = time.time() + PROCESS_RUN_TIME
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        e = stderr.decode()
        if not e:
            e = "Nᴏ Ꭼrrᴏr"
        o = stdout.decode() ##g
        if not o:
            o = "Nᴏ Ꮻuᴛᴩuᴛ"
        else:
            _o = o.split("\n")
            o = "`\n`".join(_o)
        OUTPUT = f"**ᎧᏌᎬᏒᎩ:**\n__Ꮯᴏʍʍᴀnd:__\n`{cmd}` \n__ᏢᏆᎠ:__\n`{process.pid}`\n\n**ᏚᎢᎠᎬᏒᏒ:** \n`{e}`\n**Ꮻuᴛᴩuᴛ:**\n{o}"

        if len(OUTPUT) > MAX_MESSAGE_LENGTH:
            with open("exec.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(OUTPUT))
            await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption=cmd,
                disable_notification=True,
                reply_to_message_id=reply_to_id
            )
            os.remove("exec.text")
            await message.delete()
        else:
            await message.reply_text(OUTPUT)
  else:
    return

async def aexec(code, client, message):
    exec(
        f"async def __aexec(client, message): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

async def eval_message_f(client, message):
    if message.from_user.id in Config.AUTH_USERS:
        status_message = await message.reply_text("Ꮲrᴏᴄᴇssing...")
        cmd = message.text.split(" ", maxsplit=1)[1]

        reply_to_id = message.id
        if message.reply_to_message:
            reply_to_id = message.reply_to_message.id

        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await aexec(cmd, client, message)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Ꮪuᴄᴇss"

        final_output = (
            "**ᎬᏙᎪᏞ**: <code>{}</code>\n\n**ᏫᏌᎢᏢᏌᎢ**:\n<code>{}</code> \n".format(
                cmd, evaluation.strip()
            )
        )

        if len(final_output) > MAX_MESSAGE_LENGTH:
            with open("eval.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(final_output))
            await message.reply_document(
                document="eval.text",
                caption=cmd,
                disable_notification=True,
                reply_to_message_id=reply_to_id,
            )
            os.remove("eval.text")
            await status_message.delete()
        else:
            await status_message.edit(final_output)


async def progress_for_pyrogram(current, total, bot, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        pro_bar = "{0}{1}".format(''.join([FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 10))]), ''.join([UN_FINISHED_PROGRESS_STR for i in range(10 - math.floor(percentage / 10))]))
        perc_b = '{0}'.format(round(percentage, 2))
        done_mb = '{0}'.format(humanbytes(current))
        total_mb = '{0}'.format(humanbytes(total))
        spid = '{0}'.format(humanbytes(speed))
        messg = f"{ud_type}\n➣ **Ꮲᴇrᴄᴇnᴛ** 🗿 : {perc_b} \n➣ **Ꭲᴏᴛᴀl Ꮪizᴇ** 🎯 : {total_mb}\n➣ **Ꮯᴏʍᴩlᴇᴛᴇd** 🏗 : {done_mb}\n➣ **Ꭲiʍᴇ Ꮮᴇfᴛ** ⌛️ : {estimated_total_time if estimated_total_time != '' else '0 s'}\n➣ **Ꮪᴩᴇᴇd** 🚀 : {spid}\n➢ {pro_bar}"
        try:
         if not message.photo:
          await message.edit_text(text=messg)
         else:
          await message.edit_caption(caption=messg)
        except:
         pass

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]
  
  
async def progress_for_pyrogram1(current, total, bot, ud_type, message, start, size):
    now = time.time()
    total = size
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        pro_bar = "{0}{1}".format(''.join([FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 10))]), ''.join([UN_FINISHED_PROGRESS_STR for i in range(10 - math.floor(percentage / 10))]))
        perc_b = '{0}'.format(round(percentage, 2))
        done_mb = '{0}'.format(humanbytes(current))
        total_mb = '{0}'.format(humanbytes(total))
        spid = '{0}'.format(humanbytes(speed))
        messg = f"{ud_type}\n➣ **Ꮲᴇrᴄᴇnᴛ** 🗿 : {perc_b} \n➣ **Ꭲᴏᴛᴀl Ꮪizᴇ** 🎯 : {total_mb}\n➣ **Ꮯᴏʍᴩlᴇᴛᴇd** 🏗 : {done_mb}\n➣ **Ꭲiʍᴇ Ꮮᴇfᴛ** ⌛️ : {estimated_total_time if estimated_total_time != '' else '0 s'}\n➣ **Ꮪᴩᴇᴇd** 🚀 : {spid}\n➢ {pro_bar}"
        try:
         if not message.photo:
          await message.edit_text(text=messg)
         else:
          await message.edit_caption(caption=messg)
        except:
         pass  

