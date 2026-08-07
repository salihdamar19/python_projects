from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8937279105:AAHf-xQ1Hs5bUhWyErJzRsrU7CaZTuLt9ic"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()