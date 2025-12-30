#!/bin/bash
set -e

echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt --break-system-packages

echo "Installing ffmpeg..."
curl -fsSL https://raw.githubusercontent.com/maravento/ffmpeg-install/master/install.sh | bash

echo "Installing mediainfo..."
if command -v apt >/dev/null 2>&1; then
    sudo apt install -y mediainfo
elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y mediainfo
elif command -v pacman >/dev/null 2>&1; then
    sudo pacman -S --noconfirm mediainfo
elif command -v zypper >/dev/null 2>&1; then
    sudo zypper install -y mediainfo
elif command -v apk >/dev/null 2>&1; then
    sudo apk add mediainfo
else
    echo "❌ No supported package manager found"
    exit 1
fi

echo "✅ All dependencies installed successfully!"
