import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"


async def start(update, context):
    await update.message.reply_text("Hello! ✅ Your bot is working fine.")

async def help_command(update, context):
    await update.message.reply_text(
        "📌 Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show available commands\n"
        "/about - Learn about this bot"
    )

async def about(update, context):
    await update.message.reply_text(
        "🤖 This is a Crypto Signals Bot.\n"
        "It will give you updates about trading signals 📈\n"
        "Powered by Python + Telegram Bot API."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    print("Bot is running... send /start, /help or /about in Telegram to test.")
    app.run_polling()

if __name__ == "__main__":
    main()
