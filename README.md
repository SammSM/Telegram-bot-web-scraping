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

## 🛠️ Setup Guide

## 1. Clone the repository
Open your environment and clone the repository
```bash
git clone https://github.com/SammSM/Telegram-bot-web-scraping.git
```
## 2. Change to Telegram-bot-web-scraping directory
```bash
cd Telegram-bot-web-scraping
```
## 3. Add webdriver in folder with files

## 4. Create a virtual environment and activate it

- ### Create a virtual environment
On Windows:
```bash
python -m venv venv
```
On macOS / Linux:
```bash
python3 -m venv venv
```
- ### Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
```
On macOS / Linux:
```bash
source venv/bin/activate
```

## 5. Install PIP package manager for Python
```bash
py -m pip install --upgrade pip
```
### Or
```bash
python -m pip install --upgrade pip
```

## 6. Install requirements
```bash
pip install -r requirements.txt
```

## 7. Get token from BotFather in Telegram.
- Enter /start in BotFather and follow the instruction
- Paste the generated token in auto_bot.py

## 8. Run auto_bot.py
```bash
py auto_bot.py
```
Open the bot and enter /start
