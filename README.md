# Telegram-bot-web-scraping
A Telegram bot that returns the top 10 car listings from the auto.am. The project uses web scraping to gather real-time data. Built with Python, this bot delivers quick and relevant results directly in Telegram.

This is a Python-based Telegram bot that provides users with the **top 10 listings** from the Armenian vehicle market, including **cars**, **motorcycles**, **buses**, and **trucks**.

The bot uses **web scraping** to gather real-time vehicle data and returns it directly in Telegram. Images from listings are downloaded and saved in categorized folders.

---

## ⚙️ How It Works

- The bot scrapes vehicle listings from Armenian websites using **Selenium** and a web browser driver.
- Users interact with the bot via Telegram commands.
- Images and listing information are fetched and organized by category.

---

## 🧰 Requirements

- Add `chromedriver` or other compatible WebDriver
- Add Telegram bot token from **@BotFather** in auto_bot.py "TOKEN = your_token"
- Install dependencies:
  ```bash
  pip install -r requirements.txt
