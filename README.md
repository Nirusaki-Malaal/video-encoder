<h1 align="center">🚀 Video Encoder Bot</h1>
<h3 align="center">⚡ A Super-Powered Telegram Bot That Encodes Videos Using Custom FFMPEG Settings ⚙️</h3>

<p align="center">
  <img src="https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif" width="200" alt="Naruto running">
  <img src="https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif" width="200" alt="Hello Kitty typing">
</p>

---

### 🧠 What’s This?
A beast of a bot that can **encode videos using your custom FFMPEG commands** 🧩  
Even after a restart, this bot **keeps working like Naruto chasing his dream** — all thanks to its persistent database!

---

## 💪 Features
- 🎥 Encode videos with **your own FFMPEG settings**
- 🔄 **Persistent queue** — doesn’t lose progress even after restart
- 🧰 Admin utilities like bash, eval, and system info
- 🐳 Easy Docker deployment or manual setup
- 🧾 Fully customizable via `config.env`
- 💾 Auto-save + database persistence = no rage-quits

---

<p align="center">
  <img src="https://media.giphy.com/media/26xBI73gWquCBBCDe/giphy.gif" width="250" alt="Naruto believe it">
  <br>
  <b>"Believe it!" - Naruto, probably while encoding videos at 2AM</b>
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
Put all your bot credentials inside:

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

> ⚠️ **Note:** Start the bot before running encoding or you’ll face:  
> `"Client Has Not Met Error"` 😭

---

<p align="center">
  <img src="https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif" width="200" alt="Hello Kitty coding">
  <br>
  <b>Even Hello Kitty codes FFMPEG now 💅</b>
</p>

---

## 🛠️ Tech Stack
- 🐍 **Python 3**
- 🎞️ **FFMPEG**
- 💾 **Database** (for queue persistence)
- 🤖 **Telegram Bot API**
- 🐳 **Docker** (for easy deployment)

---

## 💖 Support the Project
If you vibe with this project, please **⭐ star the repo**  
It took me *days of sleep deprivation + ramen* to make this work 🌀

<p align="center">
  <img src="https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif" width="200" alt="Naruto thumbs up">
</p>

---

## 📸 Demo
_Add your Telegram bot screenshots or GIF demos here!_

---

### Made with ❤️, 🦾, and too much caffeine by [YourNameHere]
