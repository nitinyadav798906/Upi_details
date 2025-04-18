import telebot

# Set your bot token directly here
API_TOKEN = "7854424887:AAF1Mhu6tPz6rkso5eW1IHKGq8cYx9QCBhY"  # Replace with your actual bot token

# Initialize the bot with your token
bot = telebot.TeleBot(API_TOKEN)

# Dictionary to store UPI details
upi_details = {}

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please send your UPI details in the following format:\n"
                          "Name: \nUPI Id: \nFull Details: \nMICR:")

# Message handler for collecting UPI details
@bot.message_handler(func=lambda message: True)
def collect_upi_details(message):
    details = message.text.split('\n')
    for detail in details:
        try:
            key, value = detail.split(':', 1)
            upi_details[key.strip()] = value.strip()
        except ValueError:
            continue

    # Format the response to send back to the user
    response = "Thank you! Here are the details you provided:\n"
    response += "\n".join(f"{key}: {value}" for key, value in upi_details.items())
    bot.reply_to(message, response)

if __name__ == '__main__':
    bot.polling(none_stop=True)
