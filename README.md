<h1 align="center">🍥 Video Encoder Bot</h1>
<h3 align="center">⚡ The Ultimate FFMPEG-Powered Telegram Bot — Encodes Like a Hokage ⚙️</h3>

<p align="center">
  <img src="https://i.giphy.com/y5efFpqW5knlu.webp" width="250" alt="Naruto running">
  <img src="https://i.giphy.com/kZqbBT64ECtjy.webp" width="200" alt="Hello Kitty coding">
</p>

---

### 🧠 What’s This?
A **supercharged Telegram bot** that lets you encode videos using **your own FFMPEG commands** 🎞️  
Even if your server restarts, it **keeps encoding** 💪  
All thanks to a persistent database that remembers your queue!

---

## 💪 Features
- 🍥 Encode videos with **your own FFMPEG settings**
- 🌀 **Persistent queue** — keeps working through restarts
- 💻 **Admin tools:** bash, eval, sysinfo, mediainfo
- 🐳 Deploy easily using **Docker** or manual setup
- 🧾 Fully configurable via `config.env`
- 💾 Reliable database = zero progress loss

---

<p align="center">
  <img src="https://i.giphy.com/rw3oHXGVUuUE0.webp" width="250" alt="Urahra">
  <br>
  <b>Smart Like Urahara Kisuke</b>
</p>

---

## 💬 Commands

| Command | Description |
|----------|-------------|
| `/start` | Start the bot |
| `/encode` | Manually add a video to the queue |
| `/simp` | Get a sample encode |
| `/getcode` | Show current FFMPEG command |
| `/setcode` | Set your FFMPEG code |
| `/renew` | Renew bot session |
| `/clear` | Clear encoding queue |
| `/setul` | Change upload mode (`document` / `video`) |
| `/ulmode` | Get current upload mode |
| `/ul` | Upload manually |
| `/dl` | Download manually |
| `/bash` | Run Linux commands (admin only) |
| `/eval` | Execute Python code |
| `/vshot <num>` | Take a video screenshot |
| `/info` | Get video metadata |
| `/sysinfo` | Show system info |
| `/uptime` | Display uptime |

---

## 🧰 Deployment Guide

### 🧾 1. Fill in `config.env`
Add your credentials like this:

```env
BOT_TOKEN=your_bot_token_here
OWNER_ID=123456789
DATABASE_URL=your_database_url
FFMPEG_CODE=-preset veryfast -crf 23 -c:v libx264 -c:a aac
```

---

### 🐳 2. Deploy with Docker
```bash
docker build -t video-encoder-bot .
docker run -d video-encoder-bot
```

---

### 💻 3. Or Run Manually
```bash
pip install -r requirements.txt
python3 -m bot
```

> ⚠️ **Note:** Start the bot before encoding or you'll face:  
> `"Client Has Not Met Error"` 😭

---

<p align="center">
  <img src="https://i.giphy.com/L1FJH5qxESFwpuTgIB.webp" width="220" alt="Hello Kitty laptop">
  <br>
  <b>Even Hello Kitty is debugging your FFMPEG args 💅</b>
</p>

---

## 🛠️ Tech Stack
- 🐍 **Python 3**
- 🎞️ **FFMPEG**
- 💾 **Database** (persistent queue)
- 🤖 **Telegram Bot API**
- 🐳 **Docker** (for deployment)

---

## 💖 Support the Project
If this bot saved your encoding sanity, please **⭐ star the repo**  
Made with sleepless nights, coffee , and a little willpower 🍃

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHdmdWlyc2o0aXVnM2M3NHBpbHBuYWNodzltbXQ5ZzlhOG93c290aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iJ7GTWl4VusjMGeqOV/giphy.gif" width="200" alt="hare krishna">
  <br>
  <b>Thanks for supporting, हरे कृष्ण</b>
</p>


### Made with ❤️, 🦾, and way too much caffeine by [Nirusaki]
I have fixed Everything one in for all
