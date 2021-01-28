from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import telegram
from telegram import Update
load_dotenv()
import os
import logging
import search
TOKEN = os.getenv("TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(TOKEN, use_context=True)
j = updater.job_queue

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! \n /traccia per tracciare instantaneamente i prezzi \n /check per far partire il check periodico  \n /stopcheck per far fermare il check periodico')



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help! \n /traccia per tracciare instantaneamente i prezzi \n /check per far partire il check periodico  \n /stopcheck per far fermare il check periodico')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def check1(context):
    result = search.check_ig()
    if result != "":
        context.bot.send_message(context.job.context,result)

def check2(context):
    result = search.check_of()
    if result != "":
        context.bot.send_message(context.job.context,result)

def checkperiod(context):
    result = search.period()
    context.bot.send_message(context.job.context, result)

def track(update,context):
    update.message.reply_text(search.prices())

def check(update, context):
    context.job_queue.run_repeating(check1, interval=120, context=update.message.chat_id, first=1)
    context.job_queue.run_repeating(check2, interval=120, context=update.message.chat_id, first=1)
    context.job_queue.run_repeating(checkperiod, interval=3600, context=update.message.chat_id, first=1)

def shutdown():
    updater.stop()
    updater.is_idle = False

def stop(bot, update):
    threading.Thread(target=shutdown).start()

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("traccia", track))
    dp.add_handler(CommandHandler("check",check))
    dp.add_handler(CommandHandler("stop", stop))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
