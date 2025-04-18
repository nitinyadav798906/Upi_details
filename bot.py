import telebot
import re

# Set your bot token directly here
API_TOKEN = "7854424887:AAF1Mhu6tPz6rkso5eW1IHKGq8cYx9QCBhY"  # Replace with your actual bot token

# Initialize the bot with your token
bot = telebot.TeleBot(API_TOKEN)

# Function to extract details from UPI ID
def extract_upi_details(upi_id):
    # Sample logic for extracting details (modify as needed)
    details = {
        "Bank": "Sample Bank",  # Replace with actual bank extraction logic
        "Account Holder": "Sample Holder",  # Replace with actual holder extraction logic
        "UPI ID": upi_id
    }
    return details

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please send your UPI ID for details.")

# Message handler for processing UPI IDs
@bot.message_handler(func=lambda message: True)
def handle_upi_id(message):
    upi_id_pattern = r'\w+@\w+'  # Basic regex for UPI ID
    if re.match(upi_id_pattern, message.text):
        details = extract_upi_details(message.text)
        response = "\n".join(f"{key}: {value}" for key, value in details.items())
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Please enter a valid UPI ID.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
