import os
import telebot
from telebot import types

# Initialize the bot with your token
API_TOKEN = os.getenv('7854424887:AAF1Mhu6tPz6rkso5eW1IHKGq8cYx9QCBhY')  # Alternatively, replace it with your token directly
bot = telebot.TeleBot(API_TOKEN)

# UPI details dictionary
upi_details = {}

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please send your UPI details in the following format:\n"
                          "Name: \nUPI Id: \nFull Details: \nMICR: ...")

# Message handler for collecting UPI details
@bot.message_handler(func=lambda message: True)
def collect_upi_details(message):
    details = message.text.split('\n')
    for detail in details:
        try:
            key, value = detail.split(':', 1)
            key = key.strip()
            value = value.strip()
            upi_details[key] = value
        except ValueError:
            continue

    bot.reply_to(message, "Thank you! Here are the details you provided:\n" + 
                          "\n".join(f"{key}: {value}" for key, value in upi_details.items()))

if __name__ == '__main__':
    bot.polling()
