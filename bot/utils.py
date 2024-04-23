import logging
from telegram import ParseMode

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def send_message(update, context, text):
    """Send a text message to the user"""
    update.message.reply_text(text)

def send_photo(update, context, photo_url, caption=None):
    """Send a photo to the user"""
    update.message.reply_photo(photo=photo_url, caption=caption, parse_mode=ParseMode.HTML)

def send_document(update, context, document_url, caption=None):
    """Send a document to the user"""
    update.message.reply_document(document=document_url, caption=caption, parse_mode=ParseMode.HTML)

def send_video(update, context, video_url, caption=None):
    """Send a video to the user"""
    update.message.reply_video(video=video_url, caption=caption, parse_mode=ParseMode.HTML)

def send_error(update, context, error_message):
    """Send an error message to the user"""
    logging.error(f"Error: {error_message}")
    update.message.reply_text(f"An error occurred: {error_message}")

def log_message(update, context):
    """Log received messages"""
    logging.info(f"Message from {update.message.chat_id}: {update.message.text}")
