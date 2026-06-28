# 🧮 Telegram Calculator Bot

A simple Telegram bot that calculates arithmetic expressions.  
Just send a message like `10 + 5` and get the result instantly.

## ✨ Features

- Supports four basic operations: `+`, `-`, `*`, `/`
- Handles invalid inputs and division by zero
- Clean and user-friendly responses
- Shows integers without decimal points (e.g., `10` instead of `10.0`)

## 🚀 How to Use

1. Start the bot with `/start`
2. Send a message in this format: `number operator number`

## 🛠️ Technologies

- Python 3
- pyTelegramBotAPI (telebot)
- python-dotenv

## 🔧 Setup

1. Clone the repository:
```bash
git clone https://github.com/Maryam2002-ch/telegram-calculator-bot.git
```
2. Install dependencies:
```bash
pip install pyTelegramBotAPI python-dotenv
```
3. Create a .env file in the project root: <br>
`token=YOUR_BOT_TOKEN` 
4. Run the bot:
```bash
python calculator_bot.py
```
## 📝 Error Handling
❌ Invalid format → "Please send numbers in this format: 10 + 5"

❌ Division by zero → "Cannot divide by zero!"

## 📁 Project Structure
telegram-calculator-bot/ <br>
├── calculator_bot.py &nbsp; &nbsp; # Main bot code <br>
├── .env &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Bot token (excluded from git) <br>
└── README.md &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Project documentation

---
⭐ If you found this useful, give it a star!
