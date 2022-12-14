import logging
from telegram.ext import *
import long_responses



bot = ('5825650071:AAH96FpxwcArIxjvuV86PMeoSpLKHcIb9Ig')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello! I am a bot Felix. What\'s up?')


def help_command(update, context):
    update.message.reply_text('Try to print something!')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here. ')



def handle_message(update, context):
    text = str(update.message.text).lower()
    response = long_responses.get_response(text)
    logging.info(f'User ({update.message.chat.id})says:{text}')

    update.message.reply_text(response)

def error(update, context):
    logging.error(f'Update{update} caused error {context.error}')

if __name__ == '__main__':
    updater = Updater(bot, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler('help', help_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))


    dp.add_error_handler(error)

    updater.start_polling(2)
    updater.idle()
