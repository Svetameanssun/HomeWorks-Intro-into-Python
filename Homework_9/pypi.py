# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5854999062:AAFHGHZZPAq0LNGU164gP5vVdr2vYTlxsIE").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server_start')

app.run_polling()