import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

telegram_bot_token = "2072054362:AAExWxrWHbKhETT_T_rjc23y_c0kkagCrsA"

updater = Updater(token = telegram_bot_token, use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effetive_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello world")

dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()