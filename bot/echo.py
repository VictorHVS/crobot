import logging
import os
import random
import sys

from telegram.ext import Updater, CommandHandler

# Enabling logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8442"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def start_handler(bot, update):
    # Creating a handler-function for /start command 
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("Hello from Python!\nPress /random to get random number")


def mode_handler(bot, update):
    # Creating a handler-function for /start command
    logger.info("{} Enviroment".format(mode))
    update.message.reply_text("{} Enviroment".format(mode))


def random_handler(bot, update):
    # Creating a handler-function for /random command
    number = random.randint(0, 10)
    logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
    update.message.reply_text("Random number: {}".format(number))


# new functions
def cadastrar_item(bot, update):
   itens=update.message.text.split(" ")
   update.message.reply_text(f"Item name:{itens[1]} Item Amount:{itens[2]}")

def deletar_item(bot, update):
    pass

def finalizar_item(bot, update):
    pass

def listar_itens(bot, update):
    pass 
 




if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("random", random_handler))
    updater.dispatcher.add_handler(CommandHandler("mode", mode_handler))
    updater.dispatcher.add_handler(CommandHandler("cadastrar_item", cadastrar_item))

    run(updater)
