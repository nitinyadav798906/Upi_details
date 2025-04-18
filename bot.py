import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Replace 'YOUR_API_KEY' with your NumVerify API key
NUMVERIFY_API_KEY = 'YOUR_API_KEY'

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a mobile number to get its details.')

def get_number_info(number: str) -> str:
    response = requests.get(f'http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={number}')
    data = response.json()
    
    if 'valid' in data and data['valid']:
        details = [
            f"Number: {data['number']}",
            f"Country: {data['country_name']}",
            f"Location: {data['location']}",
            f"Carrier: {data['carrier']}",
            f"Line Type: {data['line_type']}"
        ]
        return "\n".join(details)
    else:
        return "Invalid number or no details found."

def handle_message(update: Update, _: CallbackContext) -> None:
    text = update.message.text
    if text.isdigit():
        number_info = get_number_info(text)
        update.message.reply_text(number_info)
    else:
        update.message.reply_text('Please send a valid mobile number.')

def main() -> None:
    updater = Updater("7854424887:AAF1Mhu6tPz6rkso5eW1IHKGq8cYx9QCBhY")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
        
