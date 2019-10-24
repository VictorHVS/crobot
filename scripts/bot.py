import logging
import os
import random
import sys

from telegram.ext import Updater, CommandHandler

# Enabling logging
from core.models import User, Item
from crobot import settings

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup

if settings.MODE == "dev":
    def start_bot(updater):
        updater.start_polling()
elif settings.MODE == "prod":
    def start_bot(updater):
        PORT = int(os.environ.get("PORT", "8442"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=settings.TELEGRAM_TOKEN)
        updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{settings.TELEGRAM_TOKEN}")
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def get_user(update):
    chat_id = update.message.chat_id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    user = User.objects.filter(telegram_chat_id=chat_id).first()

    if user:
        user.telegram_username = username
        user.first_name = first_name
        user.save()
    else:
        user = User.objects.update_or_create(telegram_chat_id=chat_id,
                                             telegram_username=username,
                                             name=first_name)

    return user


def start_handler(bot, update):
    # Creating a handler-function for /start command 
    logger.info("User {} started bot".format(update.effective_user["id"]))
    user = get_user(update)
    update.message.reply_text("Hello from Python!\nPress /random to get random number")


def mode_handler(bot, update):
    # Creating a handler-function for /start command
    logger.info("{} Enviroment".format(settings.MODE))
    update.message.reply_text("{} Enviroment".format(settings.MODE))


def random_handler(bot, update):
    # Creating a handler-function for /random command
    number = random.randint(0, 10)
    logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
    update.message.reply_text("Random number: {}".format(number))


def cadastrar_item(bot, update):
    itens = update.message.text.split(" ")

    name = itens[1]
    amount = itens[2]
    user = get_user(update)
    item = Item(creator=user,
                name=name,
                amount=amount)
    item.save()
    update.message.reply_text("{} cadastrado com sucesso".format(name))


def deletar_item(bot, update):
    pass


def finalizar_item(bot, update):
    pass


def listar_itens(bot, update):
    pass


def run():
    logger.info("Starting bot")
    updater = Updater(settings.TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("random", random_handler))
    updater.dispatcher.add_handler(CommandHandler("mode", mode_handler))
    updater.dispatcher.add_handler(CommandHandler("cadastrar_item", cadastrar_item))

    start_bot(updater)

