<p align="center">
  <img src="assets/logo.svg" alt="video-encoder logo" width="540">
</p>

# video-encoder

Queue-based video encoding daemon with persistent MongoDB state, custom FFMPEG parameter pipelines, and Telegram bot control.

## Architecture

* **Worker Daemon**: Asynchronous task runner consuming encoding jobs sequentially.
* **Persistent Queue**: MongoDB storage maintaining job states, input parameters, and file references across process restarts.
* **Media Engine**: Native FFMPEG runtime with custom libfdk_aac compilation and multi-track audio/subtitle preservation.
* **Control Plane**: Telegram Bot API client for remote job dispatch, progress telemetry, and shell administration.

## Prerequisites

* Docker and Docker Compose (recommended) or a Linux environment with:
  * Python 3.10+
  * FFMPEG (built with libfdk_aac)
  * MongoDB 5.0+

## Configuration

Set environment variables in `config.env` or pass them via container runtime:

| Variable | Description |
| :--- | :--- |
| `API_ID` | Telegram API ID from my.telegram.org |
| `API_HASH` | Telegram API Hash from my.telegram.org |
| `BOT_TOKEN` | Bot token from @BotFather |
| `OWNER_ID` | Telegram user ID of authorized administrator |
| `DATABASE_URL` | MongoDB connection URI |
| `DOWNLOAD_DIR` | Working scratch directory for downloads |

## Deployment

### Docker (Recommended)

```bash
docker build -t video-encoder .
docker run -d --env-file config.env video-encoder
```

### Manual Host Execution

```bash
chmod +x install.sh start.sh
./install.sh
pip install -r requirements.txt
./start.sh
```

## License

GPL-3.0-or-later. See LICENSE for details.
