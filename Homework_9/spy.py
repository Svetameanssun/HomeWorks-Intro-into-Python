from telegram import Update
from telegram.ext import ContextTypes
from aiofiles.os import *


# #  def logging(update: Update, context: ContextTypes.DEFAULT_TYPE):
# async with aiofiles.tempfile.db.csv('a') as f:
# await f.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')


async def logging(update, context):
    with aiofiles.open('db.csv', mode='wb') as f:
        await f.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')