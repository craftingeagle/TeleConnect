import logging
from telegram.ext import Updater
from bot import handlers
from bot.config import TOKEN

def main():
    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(handlers.start_handler)
    dp.add_handler(handlers.help_handler)
    dp.add_handler(handlers.convert_image_handler)
    dp.add_handler(handlers.process_video_handler)

    # Start the Bot
    updater.start_polling()
    logging.info("Bot started polling...")

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
