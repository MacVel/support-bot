import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import logging
from log import configure_logger
from dotenv import load_dotenv
from dialog_flow_connect import detect_intent_texts
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
PROJECT_ID=os.getenv('PROJECT_ID')
GOOGLE_APPLICATION_CREDENTIALS=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

logger = logging.getLogger(__name__)

def start(bot,update):
    update.message.reply_text('Здравствуйте!\nВас приветствует бот поддержки! Чем мы можем помочь вам?')

def echo(bot,update):
    #Connect bot to Dialogflow and answering on the any messages
    text = detect_intent_texts(PROJECT_ID,update.message.chat.id,update.message.text)
    update.message.reply_text(text)




def main():
    configure_logger(__name__,level=logging.INFO,bot_token=TOKEN,chat_id=os.getenv('CHAT_ID'))
    while True:
        try:
            updater = Updater(TOKEN)
            dp = updater.dispatcher
            dp.add_handler(CommandHandler('start',start))
            dp.add_handler(MessageHandler(Filters.text, echo))
            updater.start_polling()
            logging.info('Бот запущен')
            updater.idle()
        except Exception as exc:
            logger.error('Bot has been crashed')
            logger.exception(err)

    

if __name__ == "__main__":
    main()