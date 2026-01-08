# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official

import asyncio
import datetime
import sys
import platform
from datetime import timezone, timedelta
import aiohttp
from pyrogram import Client, filters, __version__ as pyrogram_version
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, KEEP_ALIVE_URL
from logger import LOGGER

logger = LOGGER(__name__)

# ✅ Indian Standard Time
IST = timezone(timedelta(hours=5, minutes=30))


async def keep_alive():
    """Send a request every 100 seconds to keep the bot alive."""
    logger.info(f"KEEP_ALIVE_URL set to: {KEEP_ALIVE_URL}")
    async with aiohttp.ClientSession() as session:
        while True:
            if KEEP_ALIVE_URL:
                try:
                    logger.info("Sending keep-alive request to keep the web app alive.")
                    await session.get(KEEP_ALIVE_URL)
                    logger.info("Sent keep-alive request successfully.")
                except Exception as e:
                    logger.error(f"Keep-alive request failed: {type(e).__name__}: {e}")
            await asyncio.sleep(100)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Rexbots Login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Rexbots"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        await super().start()
        me = await self.get_me()

        # Start keep-alive
        self.keep_alive_task = asyncio.create_task(keep_alive())

        # Cache Log Channel Peer
        logger.info(f"Attempting to cache LOG_CHANNEL: {LOG_CHANNEL}")
        try:
            chat = await self.get_chat(LOG_CHANNEL)
            logger.info(f"Successfully cached LOG_CHANNEL: {chat.title} (ID: {chat.id})")
        except Exception as e:
            logger.warning(f"Failed to cache Log Channel: {e}")
            logger.warning(f"LOG_CHANNEL value: {LOG_CHANNEL}. Ensure the bot is added to this channel as admin.")

        # Bot startup log
        now = datetime.datetime.now(IST)
        py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        
        text = (
            f"**__🤖 Bot Deployed / Restarted ♻️__**\n"
            f"**__- @{me.username}__**\n\n"
            f"**__📅 Date:** {now.strftime('%d-%b-%Y')}__\n"
            f"**__🕒 Time:** {now.strftime('%I:%M %p')}__\n"
            f"**🐍 Python:** `{py_ver}`\n"
            f"**🔥 Pyrogram:** `{pyrogram_version}`\n"
            f"**__@RexBots_Official__**"
        )
# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official

        try:
            await self.send_message(LOG_CHANNEL, text)
        except Exception as e:
            logger.error(f"Log send failed: {e}")

        logger.info(f"Bot Powered By @{me.username}")
        logger.info(f"Python Version: {py_ver}")
        logger.info(f"Pyrogram Version: {pyrogram_version}")

    async def stop(self, *args):
        me = await self.get_me()

        # Stop keep-alive loop
        if self.keep_alive_task:
            self.keep_alive_task.cancel()
            try:
                await self.keep_alive_task
            except asyncio.CancelledError:
                pass

        try:
            await self.send_message(LOG_CHANNEL, f"❌ Bot @{me.username} Stopped")
        except Exception as e:
            logger.error(f"Stop log failed: {e}")

        await super().stop()
        logger.info("Bot Stopped - Bye")


BotInstance = Bot()


BotInstance.run()


# Rexbots
# Don't Remove Credit 🥺
# Telegram Channel @RexBots_Official

# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official
