from telegram import Update
from telegram.ext import ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # logging(update,context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    # logging(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging(update,context)
    await update.message.reply_text(f'/hi\n/time\n/help')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # logging(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'sum = {x+y}')