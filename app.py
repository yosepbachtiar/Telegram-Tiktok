from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from io import BytesIO
import os
import requests
from douyin_tiktok_scraper.scraper import Scraper
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()  # Load environment variables from .env file
token = os.getenv("TOKEN")

if not token:
    logger.error("Token not found. Please check your .env file.")
    exit(1)
else:
    logger.debug(f"Token loaded: {token}")

api = Scraper()
BOT_USERNAME = '@ManukaAI_Bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Support me on : https://www.paypal.me/ardha27')

# ... (rest of your code)

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
