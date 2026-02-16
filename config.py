"""
Save Restricted Content Bot Configuration

Developed by: LastPerson07Xcantarella
Telegram: @cantarellabots X @THEUPDATEDGUYS
"""

import os


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "15529802"))
API_HASH = os.environ.get("API_HASH", "92bcb6aa798a6f1feadbc917fccb54d3")

ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "821215952").split(",") if admin]

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted2")

PUBLIC_COOLDOWN = int(os.environ.get("PUBLIC_COOLDOWN", 5))
PRIVATE_COOLDOWN = int(os.environ.get("PRIVATE_COOLDOWN", 5))

START_IMG_URL = os.environ.get("START_IMG_URL", "")  # leave empty for default

AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", 300))  # seconds (0 = disable)

PUBLIC_DAILY_LIMIT = int(os.environ.get("PUBLIC_DAILY_LIMIT", 10))
PRIVATE_DAILY_LIMIT = int(os.environ.get("PRIVATE_DAILY_LIMIT", 10))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003747465902"))
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
