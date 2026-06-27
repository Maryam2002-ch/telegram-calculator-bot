import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('token')

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(chat_id=message.chat.id, 
        text="Hello👋! I'm a simple calculator.\nEnter your two numbers in this form: 10 + 5")

@bot.message_handler(func=lambda msg:True)
def calculate_numbers(message):
    parts = message.text.split()

    try:
        number1 = float(parts[0])
        number2 = float(parts[2])
        operatore = parts[1]

        if operatore == '+':
            answer = number1 + number2

        elif operatore == '-':
            answer = number1 - number2

        elif operatore == '*':
            answer = number1 * number2

        elif operatore == '/':
            answer = number1 / number2

        if answer.is_integer():
            answer = int(answer)
        
        bot.reply_to(message=message, text=f"✅the answer is {round(answer, 2)}")

    except ValueError:
        bot.reply_to(message=message, text="❌Please just send valid numbers in right format! (Format: 10 + 5) ")

    except ZeroDivisionError:
        bot.reply_to(message=message, text="❌Can't division by zero! (Format: 10 + 5)")

bot.infinity_polling()