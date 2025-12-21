# 🤖 Save Restricted Content Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pyrogram-v2-yellow?style=for-the-badge&logo=telegram">
  <img src="https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge&logo=mongodb">
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
| `KEEP_ALIVE_URL` | URL to ping for keep-alive (optional) |

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

## 📝 Commands

### User Commands
*   `/start` - Start the bot
*   `/help` - Get help information
*   `/login` - Login to your account
*   `/logout` - Logout from your account
*   `/batch` - Bulk save messages
*   `/cancel` - Cancel ongoing batch process
*   `/set_caption` - Set a custom caption
*   `/set_thumb` - Set a custom thumbnail
*   `/myplan` - Check your current plan status
*   `/premium` - View premium plan details

### Admin Commands
*   `/broadcast` - Broadcast a message to all users
*   `/ban` / `/unban` - Manage user access
*   `/add_premium` / `/remove_premium` - Manage premium users
*   `/users` - View total user count
*   `/dblink` - Get database connection string

## 🤝 Contributors

A huge thanks to the developers who made this project possible:

<div align="center">

| [**Abhi**](https://t.me/about_zani/143) | [**Abhinav**](https://t.me/adityaabhinav) | [**Bharat**](https://t.me/Bharath_boy) | [**Master**](https://t.me/V_Sbotmaker) |
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
