# Telegram Channel Parser Bot

[![GitHub stars](https://img.shields.io/github/stars/yourusername/your-repo?style=flat-square)](https://github.com/yourusername/your-repo/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

![image](https://telegram.org/img/t_logo.png)

---

## 🚀 Overview
This repository contains two Python scripts: `tg_parser.py` and `app.py`. Together, they let you **parse posts from Telegram channels** and deliver them through a **Telegram bot**. No need to add the bot as an admin—just pure parsing power at your fingertips! 🔥

---

### 🤔 What is it?
`tg_parser.py` is a Python script powered by the **[Telethon](https://docs.telethon.dev/)** library. It logs into Telegram as a user and fetches posts from any public channel you choose.

### 🎯 What is it for?
- 🌐 Monitor posts in public Telegram channels (news, updates, etc.).
- 📊 Collect data like text, dates, and media for analysis or personal use.
- 🛠️ Test Telegram API features without bot restrictions.

### 🛠️ How to use?
1. **Install the required library with the specified version:**
   ```bash
   pip install aiogram==3.17.0
   pip install telethon==1.36.0
   ```

### 🔑 Get API Credentials

To connect to Telegram via Telethon, you need API credentials (`api_id` and `api_hash`). Follow these steps to obtain them:

1. **Visit the Telegram API Portal**  
   Open your browser and go to [my.telegram.org](https://my.telegram.org).

2. **Log In**  
   - Enter your phone number in international format, e.g., `+79991234567`.
   - Click "Next" (or similar).
   - You’ll receive a confirmation code in your Telegram app.
   - Input the code on the website to log in.

3. **Create an App**  
   - Once logged in, find and select **"API development tools"** (it might be under a menu or listed directly).
   - Fill out the form to create a new application:
     - **App name**: Enter a name, e.g., `"ChannelParser"`. This can be anything you like.
     - **Short name**: Provide a shorter version, e.g., `"Parser"`.
     - **Platform**: Choose `"Desktop"` (or another option if preferred; "Desktop" works fine for this).
     - **URL**: Leave it blank (optional field).
     - **Description**: Optional; you can write something like `"For parsing Telegram channels"`.
   - Click **"Create application"** (or similar) to submit.

4. **Save Your Credentials**  
   - After creating the app, you’ll see:
     - `api_id`: A unique number, e.g., `12345678`.
     - `api_hash`: A long string of letters and numbers, e.g., `aa11bb22cc33dd44`.
   - Copy these values and store them securely (e.g., in a text file or your script).
   - You’ll use them in `tg_parser.py` to authenticate your connection.

**Note**: Keep your `api_id` and `api_hash` private. Don’t share them publicly, as they give access to your Telegram account through the API.

### 🚀 How to Run?

  ```bash
  python tg_parser.py
  ```

### 🛑 Stopping  
- Hit `Ctrl+C` in the terminal to pause the action.
- Rest easy—it won’t kick you out of Telegram on your phone or PC.

