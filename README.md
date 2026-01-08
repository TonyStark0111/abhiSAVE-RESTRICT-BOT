# 🤖 Save Restricted Content Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pyrogram-v2-yellow?style=for-the-badge&logo=telegram">
</p>

An advanced Telegram bot by **RexBots** designed to save restricted content (Text, Media, Files) from both private and public channels. This bot supports batch downloading, user login via session strings, and advanced customization options.

## 🚀 Features

*   **Save Restricted Content**: Download text, media, and files from channels where saving is restricted.
*   **Batch Mode**: Bulk download messages from a channel (Public/Private) using `/batch`.
*   **User Login**: Login with your Telegram account using `/login` to enable downloading capabilities.
*   **Customization**:
    *   Set custom captions (`/set_caption`).
    *   Set custom thumbnails (`/set_thumb`).
    *   Auto-delete or replace specific words in filenames/captions.
*   **Premium System**: Built-in system for free and premium user plans.
*   **Admin Tools**: Broadcast messages, ban/unban users, manage premium status.
*   **Persistent Storage**: Uses MongoDB to store user data and settings.
*   **Keep-Alive**: Built-in keep-alive mechanism for deployment on platforms like Render/Heroku.

## 🛠 Deployment

### Prerequisites

*   Python 3.10+
*   MongoDB Database
*   Telegram API ID and Hash
*   Bot Token

### Environment Variables

To run the bot, you need to set the following environment variables:

| Variable | Description |
| :--- | :--- |
| `BOT_TOKEN` | Your Telegram Bot Token from @BotFather |
| `API_ID` | Your Telegram API ID from my.telegram.org |
| `API_HASH` | Your Telegram API Hash from my.telegram.org |
| `ADMINS` | Comma-separated list of Admin User IDs (e.g., `12345678,87654321`) |
| `DB_URI` | Your MongoDB Connection String |
| `DB_NAME` | Database Name (default: `SaveRestricted2`) |
| `LOG_CHANNEL` | Channel ID for logging new users and errors |
| `ERROR_MESSAGE` | `True` or `False` (Send error messages to user) |
| `KEEP_ALIVE_URL` | URL to ping for keep-alive (e.g., your Render service URL) |
| `INVITE_LINK` | Invite link to log channel (for troubleshooting) |

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abhinai2244/SAVE-RESTRICT-BOT.git
    cd SAVE-RESTRICT-BOT
    ```

2.  **Install dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

3.  **Run the bot:**
    ```bash
    python3 bot.py
    ```

### Docker

```bash
docker build -t rexbots-save-content .
docker run -d --env-file .env rexbots-save-content
```

## 📝 Deployment on Render.com

### Render Deployment Steps

#### 1. Prepare Your Repository
Ensure your repository is pushed to GitHub with the following files properly configured:

- **Procfile**: Configured to run as a `worker` (not `web`) for Telegram bots
- **config.py**: Environment variables set correctly
- **app.py**: Flask app for health checks (optional)

#### 2. Create a Web Service on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the build settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: Leave empty (will use Procfile)

#### 3. Environment Variables

Add these environment variables in the Render dashboard:

| Variable | Value |
|----------|-------|
| `BOT_TOKEN` | Your Telegram Bot Token |
| `API_ID` | Your Telegram API ID |
| `API_HASH` | Your Telegram API Hash |
| `ADMINS` | Admin user IDs (comma-separated) |
| `DB_URI` | MongoDB connection string |
| `DB_NAME` | Database name |
| `LOG_CHANNEL` | `-100XXXXXXXXXXXXX` (Channel ID) |
| `ERROR_MESSAGE` | `True` |
| `KEEP_ALIVE_URL` | `https://your-service.onrender.com` |
| `INVITE_LINK` | `https://t.me/+XXXXXXXXXXXX` |

**Important:** The `KEEP_ALIVE_URL` should be your own Render service URL, not the URL of another service.

### ⚠️ Troubleshooting Common Issues

#### Issue 1: PEER_ID_INVALID Error

```
[WARNING] Failed to cache Log Channel: Telegram says: [400 PEER_ID_INVALID]
```

**Cause:** The bot is not a member of the log channel or the channel ID is incorrect.

**Solution:**
1. **Add Bot to Channel:**
   - Open Telegram and go to your channel
   - Go to Channel Settings → Administrators → Add Administrator
   - Search for your bot and add it as an admin

2. **Create an Invite Link:**
   - Generate a permanent invite link for the channel
   - Add this link to `INVITE_LINK` environment variable in Render

3. **Bot Must Interact with Channel:**
   - Have the bot send a message in the channel first
   - Or have an admin forward a message from the channel to the bot
   - This allows Pyrogram to "meet" the peer

4. **Verify Channel ID:**
   - Make sure the `LOG_CHANNEL` ID starts with `-100` for supergroups
   - Forward a message from the channel to @username_to_id_bot to get the correct ID

#### Issue 2: No Open Ports Detected (Render Timeout)

```
No open ports detected, continuing to scan...
Port scan timeout reached, no open ports detected.
```

**Cause:** Render's web service expects the process to bind to a port, but Telegram bots don't need ports.

**Solution:**
1. **Change to Background Worker:**
   - In Render dashboard, change your service type from "Web Service" to "Background Worker"
   - Or use the `worker: python3 bot.py` command in Procfile

2. **Alternative: Run as Web Service with Flask:**
   - Keep as "Web Service" but use `web: python3 app.py` in Procfile
   - This runs the Flask health check app on port 10000
   - The bot still runs as a background task

#### Issue 3: Bot Keeps Restarting / Timeout

**Solution:**
1. Use `KEEP_ALIVE_URL` to ping the service every 100 seconds
2. Set the environment variable `KEEP_ALIVE_URL` to your Render service URL
3. The bot will automatically send HTTP requests to keep itself alive

### 📌 Quick Fix Summary

| Issue | Fix |
|-------|-----|
| PEER_ID_INVALID | Add bot as admin to channel, use INVITE_LINK |
| Port timeout | Use "Background Worker" or Flask web service |
| Bot restarts | Set KEEP_ALIVE_URL in environment variables |

### 🔗 Useful Links

- [Render Port Binding Docs](https://render.com/docs/web-services#port-binding)
- [Render Troubleshooting](https://render.com/docs/troubleshooting-deploys)
- [Pyrogram Documentation](https://docs.pyrogram.org/)
- [Get Channel ID](https://t.me/username_to_id_bot)

### User Commands
*   `/start` - Start the bot
*   `/help` - Get help information
*   `/login` - Login to your account
*   `/logout` - Logout from your account
*   `/cancel` - Cancel ongoing batch process
*   `/settings` - Open settings menu
*   `/myplan` - Check your current plan status
*   `/premium` - View premium plan details

#### Customization & Settings
*   `/set_caption` - Set a custom caption
*   `/see_caption` - View your custom caption
*   `/del_caption` - Delete your custom caption
*   `/set_thumb` - Set a custom thumbnail (reply to photo)
*   `/view_thumb` - View your custom thumbnail
*   `/del_thumb` - Delete your custom thumbnail
*   `/thumb_mode` - Toggle thumbnail mode (Custom/Default)
*   `/set_del_word` - Set words to auto-delete
*   `/rem_del_word` - Remove words from auto-delete list
*   `/set_repl_word` - Set words to auto-replace
*   `/rem_repl_word` - Remove replacement word pair
*   `/setchat` - Set dump chat ID

### Admin Commands
*   `/broadcast` - Broadcast a message to all users
*   `/ban` / `/unban` - Manage user access
*   `/add_premium` / `/remove_premium` - Manage premium users
*   `/users` - View total user count
*   `/premium_users` - View active premium users
*   `/set_dump` - Set dump chat for a user
*   `/dblink` - Get database connection string

## 🤝 Contributors

A huge thanks to the developers who made this project possible:

<div align="center">

| [**Abhi**](https://t.me/about_zani/143) | [**Abhinav**](https://t.me/adityaabhinav) | [**Bharath**](https://t.me/Bharath_boy) | [**Master**](https://t.me/V_Sbotmaker) |
| :---: | :---: | :---: | :---: |
| Owner | Developer | Developer | Developer |

</div>

## 📞 Support

For queries, feature requests, or bug reports, join our official channel:

<div align="center">
  <a href="https://t.me/RexBots_Official">
    <img src="https://img.shields.io/badge/RexBots-Official%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
</div>
