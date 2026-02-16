"""
Save Restricted Content Bot Configuration

Developed by: LastPerson07Xcantarella
Telegram: @cantarellabots X @THEUPDATEDGUYS

Please retain this credit if you use or modify this project.
"""

import os


# ==============================
# Telegram Bot Credentials
# ==============================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "27050683"))
API_HASH = os.environ.get("API_HASH", "013a5c0b1f2c320b98236cf212835d59")


# ==============================
# Admin Configuration
# ==============================

ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "6048003536").split(",") if admin]


# ==============================
# Database Configuration
# ==============================

DB_URI = os.environ.get("DB_URI", "mongodb+srv://SAVERESTRICTED:SAVERESTRICTED@cluster0.iqhud5q.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted2")


# ==============================
# Cooldown Settings (Anti‑Spam)
# ==============================

PUBLIC_COOLDOWN = int(os.environ.get("PUBLIC_COOLDOWN", 30))      # seconds between public requests
PRIVATE_COOLDOWN = int(os.environ.get("PRIVATE_COOLDOWN", 50))    # seconds between private requests


# ==============================
# Start Image Configuration
# ==============================

START_IMG_URL = os.environ.get("START_IMG_URL", "https://files.catbox.moe/waqs33.jpg")   # leave empty to use default fallback


# ==============================
# Auto‑Delete Settings (Anti‑Copyright)
# ==============================

AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", 1800))   # seconds (0 = disable)


# ==============================
# Daily Limits (Free Users)
# ==============================

PUBLIC_DAILY_LIMIT = int(os.environ.get("PUBLIC_DAILY_LIMIT", 20))     # public saves per 24h
PRIVATE_DAILY_LIMIT = int(os.environ.get("PRIVATE_DAILY_LIMIT", 10))   # private saves per 24h


# ==============================
# Logging Configuration
# ==============================

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003747465902"))


# ==============================
# Error Handling
# ==============================

ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
