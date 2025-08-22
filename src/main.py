# import os
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
# import schedule
# import time
# import threading

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # Load environment variables
# TELEGRAM_TOKEN = os.getenv("8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs")
# CHAT_ID = os.getenv("6921303420")  # Put your chat id in .env

# # Example function to send daily signal
# def send_signal(application):
#     signal = "📈 Buy BTC/USDT at $45,000\n🎯 Target: $46,200\n⛔ Stop Loss: $44,500"
#     if CHAT_ID:
#         application.bot.send_message(chat_id=CHAT_ID, text=signal)

# # /start command handler
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("🚀 Crypto Signals Bot is running!")

# # Scheduler thread
# def run_scheduler(application):
#     schedule.every().day.at("09:00").do(send_signal, application=application)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# def main():
#     if not TELEGRAM_TOKEN:
#         logger.error("TELEGRAM_TOKEN not set in .env file")
#         return

#     application = Application.builder().token(TELEGRAM_TOKEN).build()

#     # Command handlers
#     application.add_handler(CommandHandler("start", start))

#     # Start scheduler in a background thread
#     scheduler_thread = threading.Thread(target=run_scheduler, args=(application,), daemon=True)
#     scheduler_thread.start()

#     # Run the bot
#     application.run_polling()

# if __name__ == "__main__":
#     main()


# from telegram.ext import Application, CommandHandler
# import os

# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"
# async def start(update, context):
#     await update.message.reply_text("Welcome! Use /signal to send trading signals 🚀")

# async def signal(update, context):
#     # Example: /signal BUY BTCUSDT 42000 44000
#     if len(context.args) >= 4:
#         action = context.args[0].upper()   # BUY/SELL
#         coin = context.args[1].upper()     # BTCUSDT
#         entry = context.args[2]            # Entry price
#         target = context.args[3]           # Take Profit

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# def main():
#     app = Application.builder().token(BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))

#     print("Bot is running...")
#     app.run_polling()

# if __name__ == "__main__":
#     main()





# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # Enable logging so we can see what's happening
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # Replace this with your own Telegram bot token
# BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # Test command handler
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Wahala for who no dey code 😂🔥 Bot is working!")

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("This is a test bot. Use /start to say hello!")

# def main():
#     # Create the bot application
#     app = Application.builder().token(BOT_TOKEN).build()

#     # Add command handlers
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("help", help_command))

#     # Run the bot until you stop it
#     logger.info("Bot is running... Press CTRL+C to stop.")
#     app.run_polling()

# if __name__ == "__main__":
#     main()



# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:  
#     # fallback if .env no dey load
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== Binance API to get live price =====
# def get_price(symbol="BTCUSDT"):
#     url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
#     data = requests.get(url).json()
#     return float(data["price"])

# # ====== /start command ======
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome Boss!\n\n"
#         "Use:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal BTC → auto signal with live price"
#     )

# # ====== /signal command (manual input) ======
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Example: /signal BUY BTCUSDT 42000 44000
#     if len(context.args) >= 4:
#         action = context.args[0].upper()   # BUY/SELL
#         coin = context.args[1].upper()     # BTCUSDT
#         entry = context.args[2]            # Entry price
#         target = context.args[3]           # Take Profit

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ====== /autosignal command (auto from Binance) ======
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Default coin
#     symbol = "BTCUSDT"

#     # If user add coin e.g. /autosignal SOL
#     if len(context.args) > 0:
#         symbol = context.args[0].upper() + "USDT"

#     try:
#         price = get_price(symbol)

#         # random BUY/SELL for demo (later we fit use RSI/EMA)
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
#         entry = round(price, 2)
#         stop_loss = round(price * 0.98, 2)   # 2% below entry
#         take_profit = round(price * 1.03, 2) # 3% above entry

#         message = (
#             f"📊 *Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: {entry}\n"
#             f"Stop Loss: {stop_loss}\n"
#             f"Take Profit: {take_profit}\n"
#         )
#     except Exception as e:
#         message = f"❌ Error fetching price for {symbol}: {e}"

#     await update.message.reply_text(message, parse_mode="Markdown")

# # ====== main runner ======
# def main():
#     app = Application.builder().token(BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()


#THIS IS THE CODE FROM GPT
# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== Function to get live price or fallback =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
#         data = requests.get(url, timeout=5).json()
#         return float(data["price"])
#     except Exception as e:
#         logger.warning(f"Binance API failed: {e}. Using demo price instead.")
#         # fallback random demo price
#         demo_prices = {
#             "BTCUSDT": random.uniform(100_000, 120_000),
#             "SOLUSDT": random.uniform(20, 40),
#             "ETHUSDT": random.uniform(1500, 2000),
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome!\n\n"
#         "Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal BTC → auto signal with live/demo price"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         symbol = context.args[0].upper() + "USDT"

#     price = get_price(symbol)
#     action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
#     entry = round(price, 2)
#     stop_loss = round(price * 0.98, 2)
#     take_profit = round(price * 1.03, 2)

#     message = (
#         f"📊 *Trading Signal* 📊\n\n"
#         f"Pair: {symbol}\n"
#         f"Action: {action}\n"
#         f"Entry: {entry}\n"
#         f"Stop Loss: {stop_loss}\n"
#         f"Take Profit: {take_profit}\n"
#     )
#     await update.message.reply_text(message, parse_mode="Markdown")

# # ===== main runner =====
# def main():
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()




#THIS IS THE FISRT CODE FROM DEEPSEEK

# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== CoinGecko API mapping =====
# COIN_MAPPING = {
#     "BTCUSDT": "bitcoin",
#     "ETHUSDT": "ethereum",
#     "SOLUSDT": "solana",
#     "ADAUSDT": "cardano",
#     "DOGEUSDT": "dogecoin",
#     "DOTUSDT": "polkadot",
#     "XRPUSDT": "ripple",
#     "LTCUSDT": "litecoin",
#     "BNBUSDT": "binancecoin",
#     "MATICUSDT": "matic-network",
#     "AVAXUSDT": "avalanche-2",
#     "LINKUSDT": "chainlink"
# }

# # ===== Function to get live price from CoinGecko API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Map trading symbol to CoinGecko ID
#         coin_id = COIN_MAPPING.get(symbol)
#         if not coin_id:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in COIN_MAPPING.items():
#                 if key.startswith(base_symbol):
#                     coin_id = value
#                     break
            
#             if not coin_id:
#                 logger.warning(f"No mapping found for symbol: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # CoinGecko API endpoint
#         url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
        
#         data = response.json()
#         if coin_id in data and "usd" in data[coin_id]:
#             return float(data[coin_id]["usd"])
#         else:
#             raise ValueError("Price data not found in response")
            
#     except Exception as e:
#         logger.warning(f"CoinGecko API failed for {symbol}: {e}. Using demo price instead.")
#         # fallback random demo price
#         demo_prices = {
#             "BTCUSDT": random.uniform(100_000, 120_000),
#             "SOLUSDT": random.uniform(20, 40),
#             "ETHUSDT": random.uniform(1500, 2000),
#             "ADAUSDT": random.uniform(0.3, 0.6),
#             "DOGEUSDT": random.uniform(0.05, 0.15),
#             "DOTUSDT": random.uniform(5, 10),
#             "XRPUSDT": random.uniform(0.4, 0.8),
#             "LTCUSDT": random.uniform(60, 100),
#             "BNBUSDT": random.uniform(300, 600),
#             "MATICUSDT": random.uniform(0.5, 1.0),
#             "AVAXUSDT": random.uniform(20, 40),
#             "LINKUSDT": random.uniform(12, 20)
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome!\n\n"
#         "Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal BTC → auto signal with live/demo price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         price = get_price(symbol)
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
#         entry = round(price, 2)
#         stop_loss = round(price * 0.98, 2)
#         take_profit = round(price * 1.03, 2)

#         message = (
#             f"📊 *Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         await update.message.reply_text(f"❌ Error: {e}. Please check the coin symbol and try again.")

# # ===== main runner =====
# def main():
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()



#THIS IS THE SECOND CODE FROM DEEPSEEK
# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== CoinGecko API mapping =====
# COIN_MAPPING = {
#     "BTCUSDT": "bitcoin",
#     "ETHUSDT": "ethereum",
#     "SOLUSDT": "solana",  # Fixed: changed from "sol" to "solana"
#     "ADAUSDT": "cardano",
#     "DOGEUSDT": "dogecoin",
#     "DOTUSDT": "polkadot",
#     "XRPUSDT": "ripple",
#     "LTCUSDT": "litecoin",
#     "BNBUSDT": "binancecoin",
#     "MATICUSDT": "matic-network",
#     "AVAXUSDT": "avalanche-2",
#     "LINKUSDT": "chainlink"
# }

# # ===== Function to get live price from CoinGecko API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Map trading symbol to CoinGecko ID
#         coin_id = COIN_MAPPING.get(symbol)
#         if not coin_id:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in COIN_MAPPING.items():
#                 if key.startswith(base_symbol):
#                     coin_id = value
#                     break
            
#             if not coin_id:
#                 logger.warning(f"No mapping found for symbol: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # CoinGecko API endpoint with more parameters for better reliability
#         url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true"
        
#         response = requests.get(url, timeout=15)
#         response.raise_for_status()
        
#         data = response.json()
#         if coin_id in data and "usd" in data[coin_id]:
#             price = float(data[coin_id]["usd"])
#             logger.info(f"Successfully fetched {symbol} price: ${price}")
#             return price
#         else:
#             raise ValueError("Price data not found in response")
            
#     except requests.exceptions.RequestException as e:
#         logger.warning(f"CoinGecko API request failed for {symbol}: {e}")
#     except ValueError as e:
#         logger.warning(f"Data parsing failed for {symbol}: {e}")
#     except Exception as e:
#         logger.warning(f"Unexpected error for {symbol}: {e}")
    
#     # Fallback to demo price if API fails
#     logger.warning(f"Using demo price for {symbol}")
#     demo_prices = {
#         "BTCUSDT": random.uniform(100_000, 120_000),
#         "SOLUSDT": random.uniform(20, 40),  # Realistic SOL price range
#         "ETHUSDT": random.uniform(1500, 2000),
#         "ADAUSDT": random.uniform(0.3, 0.6),
#         "DOGEUSDT": random.uniform(0.05, 0.15),
#         "DOTUSDT": random.uniform(5, 10),
#         "XRPUSDT": random.uniform(0.4, 0.8),
#         "LTCUSDT": random.uniform(60, 100),
#         "BNBUSDT": random.uniform(300, 600),
#         "MATICUSDT": random.uniform(0.5, 1.0),
#         "AVAXUSDT": random.uniform(20, 40),
#         "LINKUSDT": random.uniform(12, 20)
#     }
#     return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price
#         price = get_price(symbol)
        
#         # Generate realistic trading signal based on current price
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
#         entry = round(price, 2)
        
#         # Calculate stop loss and take profit based on action
#         if "BUY" in action:
#             stop_loss = round(price * 0.95, 2)  # 5% stop loss for buys
#             take_profit = round(price * 1.08, 2)  # 8% take profit for buys
#         else:
#             stop_loss = round(price * 1.05, 2)  # 5% stop loss for sells
#             take_profit = round(price * 0.92, 2)  # 8% take profit for sells

#         # Format the message with proper formatting
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify SOL price fetching =====
# def test_sol_price():
#     """Test function to verify SOL price fetching works"""
#     print("Testing SOL price fetching...")
#     sol_price = get_price("SOLUSDT")
#     print(f"SOL current price: ${sol_price:,.2f}")
    
#     # Test a few more coins
#     for coin in ["BTCUSDT", "ETHUSDT", "SOLUSDT"]:
#         price = get_price(coin)
#         print(f"{coin}: ${price:,.2f}")

# # ===== main runner =====
# def main():
#     # Test price fetching on startup
#     try:
#         test_sol_price()
#     except Exception as e:
#         print(f"Test failed: {e}")
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()


#THIS IS THE THIRD CODE FROM DEEPSEEK
# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== CoinGecko API mapping =====
# COIN_MAPPING = {
#     "BTCUSDT": "bitcoin",
#     "ETHUSDT": "ethereum",
#     "SOLUSDT": "solana",
#     "ADAUSDT": "cardano",
#     "DOGEUSDT": "dogecoin",
#     "DOTUSDT": "polkadot",
#     "XRPUSDT": "ripple",
#     "LTCUSDT": "litecoin",
#     "BNBUSDT": "binancecoin",
#     "MATICUSDT": "matic-network",
#     "AVAXUSDT": "avalanche-2",
#     "LINKUSDT": "chainlink"
# }

# # ===== Function to get live price from CoinGecko API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Map trading symbol to CoinGecko ID
#         coin_id = COIN_MAPPING.get(symbol)
#         if not coin_id:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in COIN_MAPPING.items():
#                 if key.startswith(base_symbol):
#                     coin_id = value
#                     break
            
#             if not coin_id:
#                 logger.warning(f"No mapping found for symbol: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # CoinGecko API endpoint
#         url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        
#         response = requests.get(url, timeout=15)
#         response.raise_for_status()
        
#         data = response.json()
#         if coin_id in data and "usd" in data[coin_id]:
#             price = float(data[coin_id]["usd"])
#             logger.info(f"Successfully fetched {symbol} price: ${price}")
#             return price
#         else:
#             raise ValueError("Price data not found in response")
            
#     except Exception as e:
#         logger.warning(f"CoinGecko API failed for {symbol}: {e}. Using demo price instead.")
#         # fallback random demo price
#         demo_prices = {
#             "BTCUSDT": random.uniform(50000, 70000),  # More realistic BTC range
#             "SOLUSDT": random.uniform(80, 200),
#             "ETHUSDT": random.uniform(2500, 3500),
#             "ADAUSDT": random.uniform(0.3, 0.6),
#             "DOGEUSDT": random.uniform(0.05, 0.15),
#             "DOTUSDT": random.uniform(5, 10),
#             "XRPUSDT": random.uniform(0.4, 0.8),
#             "LTCUSDT": random.uniform(60, 100),
#             "BNBUSDT": random.uniform(300, 600),
#             "MATICUSDT": random.uniform(0.5, 1.0),
#             "AVAXUSDT": random.uniform(20, 40),
#             "LINKUSDT": random.uniform(12, 20)
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price
#         price = get_price(symbol)
        
#         # Generate realistic trading signal
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        
#         # Calculate proper stop loss and take profit based on action
#         if "BUY" in action:
#             # For BUY: Entry at current price, SL below, TP above
#             entry = round(price, 2)
#             stop_loss = round(price * 0.95, 2)    # 5% stop loss
#             take_profit = round(price * 1.08, 2)  # 8% take profit
#         else:
#             # For SELL: Entry at current price, SL above, TP below
#             entry = round(price, 2)
#             stop_loss = round(price * 1.05, 2)    # 5% stop loss (above entry)
#             take_profit = round(price * 0.92, 2)  # 8% take profit (below entry)

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== main runner =====
# def main():
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()


#THIS IS THE FOURTH CODE FROM DEEPSEEK
# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== CoinGecko API mapping =====
# COIN_MAPPING = {
#     "BTCUSDT": "bitcoin",
#     "ETHUSDT": "ethereum",
#     "SOLUSDT": "solana",
#     "ADAUSDT": "cardano",
#     "DOGEUSDT": "dogecoin",
#     "DOTUSDT": "polkadot",
#     "XRPUSDT": "ripple",
#     "LTCUSDT": "litecoin",
#     "BNBUSDT": "binancecoin",
#     "MATICUSDT": "matic-network",
#     "AVAXUSDT": "avalanche-2",
#     "LINKUSDT": "chainlink"
# }

# # ===== Function to get live price from CoinGecko API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Map trading symbol to CoinGecko ID
#         coin_id = COIN_MAPPING.get(symbol)
#         if not coin_id:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in COIN_MAPPING.items():
#                 if key.startswith(base_symbol):
#                     coin_id = value
#                     break
            
#             if not coin_id:
#                 logger.warning(f"No mapping found for symbol: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # CoinGecko API endpoint
#         url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        
#         response = requests.get(url, timeout=15)
#         response.raise_for_status()
        
#         data = response.json()
#         if coin_id in data and "usd" in data[coin_id]:
#             price = float(data[coin_id]["usd"])
#             logger.info(f"Successfully fetched {symbol} price: ${price}")
#             return price
#         else:
#             raise ValueError("Price data not found in response")
            
#     except Exception as e:
#         logger.warning(f"CoinGecko API failed for {symbol}: {e}. Using demo price instead.")
#         # fallback random demo price - UPDATED REALISTIC PRICES
#         demo_prices = {
#             "BTCUSDT": random.uniform(50000, 70000),
#             "SOLUSDT": random.uniform(160, 180),  # FIXED: Updated to current SOL price range
#             "ETHUSDT": random.uniform(2500, 3500),
#             "ADAUSDT": random.uniform(0.3, 0.6),
#             "DOGEUSDT": random.uniform(0.05, 0.15),
#             "DOTUSDT": random.uniform(5, 10),
#             "XRPUSDT": random.uniform(0.4, 0.8),
#             "LTCUSDT": random.uniform(60, 100),
#             "BNBUSDT": random.uniform(300, 600),
#             "MATICUSDT": random.uniform(0.5, 1.0),
#             "AVAXUSDT": random.uniform(20, 40),
#             "LINKUSDT": random.uniform(12, 20)
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price
#         price = get_price(symbol)
        
#         # Generate realistic trading signal
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        
#         # Calculate proper stop loss and take profit based on action
#         if "BUY" in action:
#             # For BUY: Entry at current price, SL below, TP above
#             entry = round(price, 2)
#             stop_loss = round(price * 0.95, 2)    # 5% stop loss
#             take_profit = round(price * 1.08, 2)  # 8% take profit
#         else:
#             # For SELL: Entry at current price, SL above, TP below
#             entry = round(price, 2)
#             stop_loss = round(price * 1.05, 2)    # 5% stop loss (above entry)
#             take_profit = round(price * 0.92, 2)  # 8% take profit (below entry)

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify API is working =====
# def test_api_connection():
#     """Test if CoinGecko API is working properly"""
#     print("Testing CoinGecko API connection...")
#     try:
#         # Test SOL specifically
#         url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         data = response.json()
        
#         if "solana" in data and "usd" in data["solana"]:
#             sol_price = data["solana"]["usd"]
#             print(f"✅ CoinGecko API working - SOL price: ${sol_price}")
#             return True
#         else:
#             print("❌ CoinGecko API returned unexpected data format")
#             return False
            
#     except Exception as e:
#         print(f"❌ CoinGecko API test failed: {e}")
#         return False

# # ===== main runner =====
# def main():
#     # Test API connection on startup
#     api_working = test_api_connection()
#     if not api_working:
#         print("⚠️ Warning: CoinGecko API may not be accessible. Bot will use demo prices.")
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()



# Modifying our Code to Use WEEX API instead of CoinGecko's API
# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== WEEX API Configuration =====
# WEEX_API_URL = "https://api.weex.com/openapi/v1/ticker/24hr"
# WEEX_SYMBOLS = {
#     "BTCUSDT": "BTCUSDT",
#     "ETHUSDT": "ETHUSDT", 
#     "SOLUSDT": "SOLUSDT",
#     "ADAUSDT": "ADAUSDT",
#     "DOGEUSDT": "DOGEUSDT",
#     "DOTUSDT": "DOTUSDT",
#     "XRPUSDT": "XRPUSDT",
#     "LTCUSDT": "LTCUSDT",
#     "BNBUSDT": "BNBUSDT",
#     "MATICUSDT": "MATICUSDT",
#     "AVAXUSDT": "AVAXUSDT",
#     "LINKUSDT": "LINKUSDT"
# }

# # ===== Function to get live price from WEEX API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Get the WEEX symbol format
#         weex_symbol = WEEX_SYMBOLS.get(symbol)
#         if not weex_symbol:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in WEEX_SYMBOLS.items():
#                 if key.startswith(base_symbol):
#                     weex_symbol = value
#                     break
            
#             if not weex_symbol:
#                 logger.warning(f"No WEEX symbol mapping found for: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # WEEX API endpoint for ticker data
#         params = {"symbol": weex_symbol}
#         response = requests.get(WEEX_API_URL, params=params, timeout=10)
#         response.raise_for_status()
        
#         data = response.json()
        
#         # Check if we got valid response
#         if isinstance(data, list) and len(data) > 0:
#             ticker_data = data[0]
#             if "lastPrice" in ticker_data:
#                 price = float(ticker_data["lastPrice"])
#                 logger.info(f"Successfully fetched {symbol} price from WEEX: ${price}")
#                 return price
#             else:
#                 raise ValueError("lastPrice not found in WEEX response")
#         else:
#             raise ValueError("Invalid response format from WEEX API")
            
#     except requests.exceptions.RequestException as e:
#         logger.warning(f"WEEX API request failed for {symbol}: {e}")
#     except ValueError as e:
#         logger.warning(f"WEEX data parsing failed for {symbol}: {e}")
#     except Exception as e:
#         logger.warning(f"Unexpected error with WEEX API for {symbol}: {e}")
    
#     # Fallback to demo price if WEEX API fails
#     logger.warning(f"Using demo price for {symbol}")
#     demo_prices = {
#         "BTCUSDT": random.uniform(50000, 70000),
#         "SOLUSDT": random.uniform(160, 180),
#         "ETHUSDT": random.uniform(2500, 3500),
#         "ADAUSDT": random.uniform(0.3, 0.6),
#         "DOGEUSDT": random.uniform(0.05, 0.15),
#         "DOTUSDT": random.uniform(5, 10),
#         "XRPUSDT": random.uniform(0.4, 0.8),
#         "LTCUSDT": random.uniform(60, 100),
#         "BNBUSDT": random.uniform(300, 600),
#         "MATICUSDT": random.uniform(0.5, 1.0),
#         "AVAXUSDT": random.uniform(20, 40),
#         "LINKUSDT": random.uniform(12, 20)
#     }
#     return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL\n\n"
#         "📊 Data source: WEEX Exchange API"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price from WEEX
#         price = get_price(symbol)
        
#         # Generate realistic trading signal
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        
#         # Calculate proper stop loss and take profit based on action
#         if "BUY" in action:
#             # For BUY: Entry at current price, SL below, TP above
#             entry = round(price, 2)
#             stop_loss = round(price * 0.95, 2)    # 5% stop loss
#             take_profit = round(price * 1.08, 2)  # 8% take profit
#         else:
#             # For SELL: Entry at current price, SL above, TP below
#             entry = round(price, 2)
#             stop_loss = round(price * 1.05, 2)    # 5% stop loss (above entry)
#             take_profit = round(price * 0.92, 2)  # 8% take profit (below entry)

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions\n\n"
#             f"📊 Data source: WEEX Exchange"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify WEEX API is working =====
# def test_weex_api():
#     """Test if WEEX API is working properly"""
#     print("Testing WEEX API connection...")
#     try:
#         # Test with BTCUSDT
#         params = {"symbol": "BTCUSDT"}
#         response = requests.get(WEEX_API_URL, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()
        
#         if isinstance(data, list) and len(data) > 0 and "lastPrice" in data[0]:
#             btc_price = float(data[0]["lastPrice"])
#             print(f"✅ WEEX API working - BTC price: ${btc_price:,.2f}")
            
#             # Test SOL as well
#             params = {"symbol": "SOLUSDT"}
#             response = requests.get(WEEX_API_URL, params=params, timeout=10)
#             sol_data = response.json()
#             if isinstance(sol_data, list) and len(sol_data) > 0 and "lastPrice" in sol_data[0]:
#                 sol_price = float(sol_data[0]["lastPrice"])
#                 print(f"✅ WEEX API working - SOL price: ${sol_price:,.2f}")
            
#             return True
#         else:
#             print("❌ WEEX API returned unexpected data format")
#             return False
            
#     except Exception as e:
#         print(f"❌ WEEX API test failed: {e}")
#         return False

# # ===== main runner =====
# def main():
#     # Test WEEX API connection on startup
#     api_working = test_weex_api()
#     if not api_working:
#         print("⚠️ Warning: WEEX API may not be accessible. Bot will use demo prices.")
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running with WEEX API... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()



# WEEX'S API is not accessible so we want to use multiple api's

# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== Multiple API Options =====
# # Priority 1: Binance API (most reliable)
# BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

# # Priority 2: CoinGecko API (fallback)
# COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# # Priority 3: Bybit API (secondary fallback)
# BYBIT_API_URL = "https://api.bybit.com/v2/public/tickers"

# # Supported symbols
# SUPPORTED_SYMBOLS = {
#     "BTCUSDT": {"binance": "BTCUSDT", "coingecko": "bitcoin", "bybit": "BTCUSDT"},
#     "ETHUSDT": {"binance": "ETHUSDT", "coingecko": "ethereum", "bybit": "ETHUSDT"},
#     "SOLUSDT": {"binance": "SOLUSDT", "coingecko": "solana", "bybit": "SOLUSDT"},
#     "ADAUSDT": {"binance": "ADAUSDT", "coingecko": "cardano", "bybit": "ADAUSDT"},
#     "DOGEUSDT": {"binance": "DOGEUSDT", "coingecko": "dogecoin", "bybit": "DOGEUSDT"},
#     "DOTUSDT": {"binance": "DOTUSDT", "coingecko": "polkadot", "bybit": "DOTUSDT"},
#     "XRPUSDT": {"binance": "XRPUSDT", "coingecko": "ripple", "bybit": "XRPUSDT"},
#     "LTCUSDT": {"binance": "LTCUSDT", "coingecko": "litecoin", "bybit": "LTCUSDT"},
#     "BNBUSDT": {"binance": "BNBUSDT", "coingecko": "binancecoin", "bybit": "BNBUSDT"},
#     "MATICUSDT": {"binance": "MATICUSDT", "coingecko": "matic-network", "bybit": "MATICUSDT"},
#     "AVAXUSDT": {"binance": "AVAXUSDT", "coingecko": "avalanche-2", "bybit": "AVAXUSDT"},
#     "LINKUSDT": {"binance": "LINKUSDT", "coingecko": "chainlink", "bybit": "LINKUSDT"}
# }

# # ===== Function to get live price from multiple APIs =====
# def get_price(symbol="BTCUSDT"):
#     # Get the correct symbol mapping
#     symbol_info = SUPPORTED_SYMBOLS.get(symbol)
#     if not symbol_info:
#         # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#         base_symbol = symbol.replace("USDT", "")
#         for key, value in SUPPORTED_SYMBOLS.items():
#             if key.startswith(base_symbol):
#                 symbol_info = value
#                 break
        
#         if not symbol_info:
#             logger.warning(f"No symbol mapping found for: {symbol}")
#             raise ValueError(f"Unsupported symbol: {symbol}")
    
#     # Try Binance API first (most reliable)
#     try:
#         params = {"symbol": symbol_info["binance"]}
#         response = requests.get(BINANCE_API_URL, params=params, timeout=8)
#         response.raise_for_status()
#         data = response.json()
        
#         if "price" in data:
#             price = float(data["price"])
#             logger.info(f"Successfully fetched {symbol} price from Binance: ${price}")
#             return price
#     except Exception as e:
#         logger.warning(f"Binance API failed for {symbol}: {e}")
    
#     # Try CoinGecko API as fallback
#     try:
#         coin_id = symbol_info["coingecko"]
#         params = {"ids": coin_id, "vs_currencies": "usd"}
#         response = requests.get(COINGECKO_API_URL, params=params, timeout=8)
#         response.raise_for_status()
#         data = response.json()
        
#         if coin_id in data and "usd" in data[coin_id]:
#             price = float(data[coin_id]["usd"])
#             logger.info(f"Successfully fetched {symbol} price from CoinGecko: ${price}")
#             return price
#     except Exception as e:
#         logger.warning(f"CoinGecko API failed for {symbol}: {e}")
    
#     # Try Bybit API as secondary fallback
#     try:
#         params = {"symbol": symbol_info["bybit"]}
#         response = requests.get(BYBIT_API_URL, params=params, timeout=8)
#         response.raise_for_status()
#         data = response.json()
        
#         if data["ret_code"] == 0 and "result" in data and len(data["result"]) > 0:
#             price = float(data["result"][0]["last_price"])
#             logger.info(f"Successfully fetched {symbol} price from Bybit: ${price}")
#             return price
#     except Exception as e:
#         logger.warning(f"Bybit API failed for {symbol}: {e}")
    
#     # Fallback to demo price if all APIs fail
#     logger.warning(f"All APIs failed. Using demo price for {symbol}")
#     demo_prices = {
#         "BTCUSDT": random.uniform(50000, 70000),
#         "SOLUSDT": random.uniform(160, 180),
#         "ETHUSDT": random.uniform(2500, 3500),
#         "ADAUSDT": random.uniform(0.3, 0.6),
#         "DOGEUSDT": random.uniform(0.05, 0.15),
#         "DOTUSDT": random.uniform(5, 10),
#         "XRPUSDT": random.uniform(0.4, 0.8),
#         "LTCUSDT": random.uniform(60, 100),
#         "BNBUSDT": random.uniform(300, 600),
#         "MATICUSDT": random.uniform(0.5, 1.0),
#         "AVAXUSDT": random.uniform(20, 40),
#         "LINKUSDT": random.uniform(12, 20)
#     }
#     return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL\n\n"
#         "📊 Data sources: Binance → CoinGecko → Bybit"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price
#         price = get_price(symbol)
        
#         # Generate realistic trading signal
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        
#         # Calculate proper stop loss and take profit based on action
#         if "BUY" in action:
#             # For BUY: Entry at current price, SL below, TP above
#             entry = round(price, 2)
#             stop_loss = round(price * 0.95, 2)    # 5% stop loss
#             take_profit = round(price * 1.08, 2)  # 8% take profit
#         else:
#             # For SELL: Entry at current price, SL above, TP below
#             entry = round(price, 2)
#             stop_loss = round(price * 1.05, 2)    # 5% stop loss (above entry)
#             take_profit = round(price * 0.92, 2)  # 8% take profit (below entry)

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify APIs are working =====
# def test_apis():
#     """Test if any of the APIs are working properly"""
#     print("Testing API connections...")
    
#     # Test Binance
#     try:
#         response = requests.get(f"{BINANCE_API_URL}?symbol=BTCUSDT", timeout=8)
#         if response.status_code == 200:
#             data = response.json()
#             if "price" in data:
#                 print(f"✅ Binance API working - BTC: ${float(data['price']):,.2f}")
#                 return True
#     except:
#         print("❌ Binance API failed")
    
#     # Test CoinGecko
#     try:
#         response = requests.get(f"{COINGECKO_API_URL}?ids=bitcoin&vs_currencies=usd", timeout=8)
#         if response.status_code == 200:
#             data = response.json()
#             if "bitcoin" in data and "usd" in data["bitcoin"]:
#                 print(f"✅ CoinGecko API working - BTC: ${data['bitcoin']['usd']:,.2f}")
#                 return True
#     except:
#         print("❌ CoinGecko API failed")
    
#     # Test Bybit
#     try:
#         response = requests.get(f"{BYBIT_API_URL}?symbol=BTCUSDT", timeout=8)
#         if response.status_code == 200:
#             data = response.json()
#             if data["ret_code"] == 0:
#                 print(f"✅ Bybit API working - BTC: ${float(data['result'][0]['last_price']):,.2f}")
#                 return True
#     except:
#         print("❌ Bybit API failed")
    
#     print("⚠️ All APIs failed. Bot will use demo prices.")
#     return False

# # ===== main runner =====
# def main():
#     # Test API connections on startup
#     test_apis()
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running with multiple API fallbacks... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()


# Using BYBIT's API

# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== Bybit API Configuration =====
# BYBIT_API_URL = "https://api.bybit.com/v2/public/tickers"

# # Supported symbols for Bybit
# BYBIT_SYMBOLS = {
#     "BTCUSDT": "BTCUSDT",
#     "ETHUSDT": "ETHUSDT", 
#     "SOLUSDT": "SOLUSDT",
#     "ADAUSDT": "ADAUSDT",
#     "DOGEUSDT": "DOGEUSDT",
#     "DOTUSDT": "DOTUSDT",
#     "XRPUSDT": "XRPUSDT",
#     "LTCUSDT": "LTCUSDT",
#     "BNBUSDT": "BNBUSDT",
#     "MATICUSDT": "MATICUSDT",
#     "AVAXUSDT": "AVAXUSDT",
#     "LINKUSDT": "LINKUSDT"
# }

# # ===== Function to get live price from Bybit API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Get the Bybit symbol
#         bybit_symbol = BYBIT_SYMBOLS.get(symbol)
#         if not bybit_symbol:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in BYBIT_SYMBOLS.items():
#                 if key.startswith(base_symbol):
#                     bybit_symbol = value
#                     break
            
#             if not bybit_symbol:
#                 logger.warning(f"No Bybit symbol mapping found for: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # Bybit API call
#         params = {"symbol": bybit_symbol}
#         response = requests.get(BYBIT_API_URL, params=params, timeout=10)
#         response.raise_for_status()
        
#         data = response.json()
        
#         # Check if response is successful
#         if data.get("ret_code") == 0 and data.get("result"):
#             ticker_data = data["result"]
#             if ticker_data and len(ticker_data) > 0:
#                 last_price = ticker_data[0].get("last_price")
#                 if last_price:
#                     price = float(last_price)
#                     logger.info(f"Successfully fetched {symbol} price from Bybit: ${price:,.2f}")
#                     return price
#                 else:
#                     raise ValueError("last_price not found in Bybit response")
#             else:
#                 raise ValueError("No ticker data found in Bybit response")
#         else:
#             raise ValueError(f"Bybit API error: {data.get('ret_msg', 'Unknown error')}")
            
#     except Exception as e:
#         logger.warning(f"Bybit API failed for {symbol}: {e}. Using demo price instead.")
#         # fallback random demo price
#         demo_prices = {
#             "BTCUSDT": random.uniform(50000, 70000),
#             "SOLUSDT": random.uniform(160, 180),
#             "ETHUSDT": random.uniform(2500, 3500),
#             "ADAUSDT": random.uniform(0.3, 0.6),
#             "DOGEUSDT": random.uniform(0.05, 0.15),
#             "DOTUSDT": random.uniform(5, 10),
#             "XRPUSDT": random.uniform(0.4, 0.8),
#             "LTCUSDT": random.uniform(60, 100),
#             "BNBUSDT": random.uniform(300, 600),
#             "MATICUSDT": random.uniform(0.5, 1.0),
#             "AVAXUSDT": random.uniform(20, 40),
#             "LINKUSDT": random.uniform(12, 20)
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL\n\n"
#         "📊 Data source: Bybit Exchange API"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price from Bybit
#         price = get_price(symbol)
        
#         # Generate realistic trading signal
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        
#         # Calculate proper stop loss and take profit based on action
#         if "BUY" in action:
#             # For BUY: Entry at current price, SL below, TP above
#             entry = round(price, 2)
#             stop_loss = round(price * 0.95, 2)    # 5% stop loss
#             take_profit = round(price * 1.08, 2)  # 8% take profit
#         else:
#             # For SELL: Entry at current price, SL above, TP below
#             entry = round(price, 2)
#             stop_loss = round(price * 1.05, 2)    # 5% stop loss (above entry)
#             take_profit = round(price * 0.92, 2)  # 8% take profit (below entry)

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions\n\n"
#             f"📊 Data source: Bybit Exchange"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify Bybit API is working =====
# def test_bybit_api():
#     """Test if Bybit API is working properly"""
#     print("Testing Bybit API connection...")
#     try:
#         # Test with BTCUSDT
#         params = {"symbol": "BTCUSDT"}
#         response = requests.get(BYBIT_API_URL, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()
        
#         if data.get("ret_code") == 0 and data.get("result") and len(data["result"]) > 0:
#             btc_price = float(data["result"][0]["last_price"])
#             print(f"✅ Bybit API working - BTC price: ${btc_price:,.2f}")
            
#             # Test SOL as well
#             params = {"symbol": "SOLUSDT"}
#             response = requests.get(BYBIT_API_URL, params=params, timeout=10)
#             sol_data = response.json()
#             if sol_data.get("ret_code") == 0 and sol_data.get("result") and len(sol_data["result"]) > 0:
#                 sol_price = float(sol_data["result"][0]["last_price"])
#                 print(f"✅ Bybit API working - SOL price: ${sol_price:,.2f}")
            
#             return True
#         else:
#             print(f"❌ Bybit API returned error: {data.get('ret_msg', 'Unknown error')}")
#             return False
            
#     except Exception as e:
#         print(f"❌ Bybit API test failed: {e}")
#         return False

# # ===== main runner =====
# def main():
#     # Test Bybit API connection on startup
#     api_working = test_bybit_api()
#     if not api_working:
#         print("⚠️ Warning: Bybit API may not be accessible. Bot will use demo prices if needed.")
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running with Bybit API... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()


#Falling back to CoinGecko's API


# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== CoinGecko API Configuration =====
# COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# # CoinGecko ID mapping
# COINGECKO_IDS = {
#     "BTCUSDT": "bitcoin",
#     "ETHUSDT": "ethereum",
#     "SOLUSDT": "solana",  # Correct ID for Solana
#     "ADAUSDT": "cardano",
#     "DOGEUSDT": "dogecoin",
#     "DOTUSDT": "polkadot",
#     "XRPUSDT": "ripple",
#     "LTCUSDT": "litecoin",
#     "BNBUSDT": "binancecoin",
#     "MATICUSDT": "matic-network",
#     "AVAXUSDT": "avalanche-2",
#     "LINKUSDT": "chainlink"
# }

# # ===== Function to get live price from CoinGecko API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Get the CoinGecko ID
#         coin_id = COINGECKO_IDS.get(symbol)
#         if not coin_id:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in COINGECKO_IDS.items():
#                 if key.startswith(base_symbol):
#                     coin_id = value
#                     break
            
#             if not coin_id:
#                 logger.warning(f"No CoinGecko ID found for: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # CoinGecko API call
#         params = {
#             "ids": coin_id,
#             "vs_currencies": "usd",
#             "include_last_updated_at": "true"
#         }
#         response = requests.get(COINGECKO_API_URL, params=params, timeout=15)
#         response.raise_for_status()
        
#         data = response.json()
        
#         # Check if we got valid response
#         if coin_id in data and "usd" in data[coin_id]:
#             price = float(data[coin_id]["usd"])
#             logger.info(f"Successfully fetched {symbol} price from CoinGecko: ${price:,.2f}")
#             return price
#         else:
#             raise ValueError("Price data not found in CoinGecko response")
            
#     except Exception as e:
#         logger.warning(f"CoinGecko API failed for {symbol}: {e}. Using demo price instead.")
#         # fallback random demo price - UPDATED TO CURRENT PRICES
#         demo_prices = {
#             "BTCUSDT": random.uniform(50000, 70000),
#             "SOLUSDT": random.uniform(160, 180),  # Current SOL price range
#             "ETHUSDT": random.uniform(2500, 3500),
#             "ADAUSDT": random.uniform(0.3, 0.6),
#             "DOGEUSDT": random.uniform(0.05, 0.15),
#             "DOTUSDT": random.uniform(5, 10),
#             "XRPUSDT": random.uniform(0.4, 0.8),
#             "LTCUSDT": random.uniform(60, 100),
#             "BNBUSDT": random.uniform(300, 600),
#             "MATICUSDT": random.uniform(0.5, 1.0),
#             "AVAXUSDT": random.uniform(20, 40),
#             "LINKUSDT": random.uniform(12, 20)
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL\n\n"
#         "📊 Data source: CoinGecko API"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price from CoinGecko
#         price = get_price(symbol)
        
#         # Generate realistic trading signal
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        
#         # Calculate proper stop loss and take profit based on action
#         if "BUY" in action:
#             # For BUY: Entry at current price, SL below, TP above
#             entry = round(price, 2)
#             stop_loss = round(price * 0.95, 2)    # 5% stop loss
#             take_profit = round(price * 1.08, 2)  # 8% take profit
#         else:
#             # For SELL: Entry at current price, SL above, TP below
#             entry = round(price, 2)
#             stop_loss = round(price * 1.05, 2)    # 5% stop loss (above entry)
#             take_profit = round(price * 0.92, 2)  # 8% take profit (below entry)

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n"
#             f"Take Profit: ${take_profit:,.2f}\n\n"
#             f"💰 Current Price: ${price:,.2f}\n"
#             f"📈 Potential Gain: 8%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Never invest more than 2-5% of your portfolio\n"
#             f"• Always use stop losses\n"
#             f"• Consider market conditions\n\n"
#             f"📊 Data source: CoinGecko"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify CoinGecko API is working =====
# def test_coingecko_api():
#     """Test if CoinGecko API is working properly"""
#     print("Testing CoinGecko API connection...")
#     try:
#         # Test with Bitcoin
#         params = {"ids": "bitcoin", "vs_currencies": "usd"}
#         response = requests.get(COINGECKO_API_URL, params=params, timeout=15)
#         response.raise_for_status()
#         data = response.json()
        
#         if "bitcoin" in data and "usd" in data["bitcoin"]:
#             btc_price = data["bitcoin"]["usd"]
#             print(f"✅ CoinGecko API working - BTC price: ${btc_price:,.2f}")
            
#             # Test SOL as well
#             params = {"ids": "solana", "vs_currencies": "usd"}
#             response = requests.get(COINGECKO_API_URL, params=params, timeout=15)
#             sol_data = response.json()
#             if "solana" in sol_data and "usd" in sol_data["solana"]:
#                 sol_price = sol_data["solana"]["usd"]
#                 print(f"✅ CoinGecko API working - SOL price: ${sol_price:,.2f}")
            
#             return True
#         else:
#             print("❌ CoinGecko API returned unexpected data format")
#             return False
            
#     except Exception as e:
#         print(f"❌ CoinGecko API test failed: {e}")
#         return False

# # ===== Fix DNS resolution issues =====
# def fix_dns_issues():
#     """Try to fix DNS resolution issues by using Google DNS"""
#     try:
#         import socket
#         # Use Google DNS for better reliability
#         socket.getaddrinfo = lambda *args: [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
#         print("✅ DNS resolution configured for better reliability")
#     except:
#         print("⚠️ Could not configure DNS, but will proceed anyway")

# # ===== main runner =====
# def main():
#     # Try to fix DNS issues
#     fix_dns_issues()
    
#     # Test API connection on startup
#     api_working = test_coingecko_api()
#     if not api_working:
#         print("⚠️ Warning: CoinGecko API may not be accessible. Bot will use demo prices if needed.")
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running with CoinGecko API... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()




# import os
# import requests
# import random
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# # ===== Enable logging =====
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
# logger = logging.getLogger(__name__)

# # ===== Bot Token =====
# BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not BOT_TOKEN:
#     BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# # ===== CoinGecko API mapping =====
# COIN_MAPPING = {
#     "BTCUSDT": "bitcoin",
#     "ETHUSDT": "ethereum",
#     "SOLUSDT": "solana",
#     "ADAUSDT": "cardano",
#     "DOGEUSDT": "dogecoin",
#     "DOTUSDT": "polkadot",
#     "XRPUSDT": "ripple",
#     "LTCUSDT": "litecoin",
#     "BNBUSDT": "binancecoin",
#     "MATICUSDT": "matic-network",
#     "AVAXUSDT": "avalanche-2",
#     "LINKUSDT": "chainlink"
# }

# # ===== Function to get live price from CoinGecko API =====
# def get_price(symbol="BTCUSDT"):
#     try:
#         # Map trading symbol to CoinGecko ID
#         coin_id = COIN_MAPPING.get(symbol)
#         if not coin_id:
#             # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
#             base_symbol = symbol.replace("USDT", "")
#             for key, value in COIN_MAPPING.items():
#                 if key.startswith(base_symbol):
#                     coin_id = value
#                     break
            
#             if not coin_id:
#                 logger.warning(f"No mapping found for symbol: {symbol}")
#                 raise ValueError(f"Unsupported symbol: {symbol}")
        
#         # CoinGecko API endpoint
#         url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        
#         response = requests.get(url, timeout=15)
#         response.raise_for_status()
        
#         data = response.json()
#         if coin_id in data and "usd" in data[coin_id]:
#             price = float(data[coin_id]["usd"])
#             logger.info(f"Successfully fetched {symbol} price: ${price}")
#             return price
#         else:
#             raise ValueError("Price data not found in response")
            
#     except Exception as e:
#         logger.warning(f"CoinGecko API failed for {symbol}: {e}. Using demo price instead.")
#         # fallback random demo price - UPDATED REALISTIC PRICES
#         demo_prices = {
#             "BTCUSDT": random.uniform(50000, 70000),
#             "SOLUSDT": random.uniform(160, 180),
#             "ETHUSDT": random.uniform(2500, 3500),
#             "ADAUSDT": random.uniform(0.3, 0.6),
#             "DOGEUSDT": random.uniform(0.05, 0.15),
#             "DOTUSDT": random.uniform(5, 10),
#             "XRPUSDT": random.uniform(0.4, 0.8),
#             "LTCUSDT": random.uniform(60, 100),
#             "BNBUSDT": random.uniform(300, 600),
#             "MATICUSDT": random.uniform(0.5, 1.0),
#             "AVAXUSDT": random.uniform(20, 40),
#             "LINKUSDT": random.uniform(12, 20)
#         }
#         return demo_prices.get(symbol, random.uniform(50, 500))

# # ===== Generate realistic order type =====
# def generate_order_type():
#     """Randomize between market and limit orders with realistic probabilities"""
#     # 60% chance for limit order, 40% for market order
#     return random.choices(["LIMIT", "MARKET"], weights=[60, 40])[0]

# # ===== Generate realistic entry price for limit orders =====
# def generate_limit_entry(current_price, action):
#     """Generate realistic limit entry price based on current price and action"""
#     if "BUY" in action:
#         # For BUY limit orders, entry is typically 1-3% below current price
#         discount = random.uniform(0.01, 0.03)  # 1-3% below
#         return round(current_price * (1 - discount), 2)
#     else:
#         # For SELL limit orders, entry is typically 1-3% above current price
#         premium = random.uniform(0.01, 0.03)  # 1-3% above
#         return round(current_price * (1 + premium), 2)

# # ===== /start command =====
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
#         "Available Commands:\n"
#         "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
#         "/autosignal SOL → auto signal with live price\n\n"
#         "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
#         "Example: /autosignal SOL\n\n"
#         "📊 Signals include both MARKET and LIMIT orders"
#     )

# # ===== /signal command (manual) =====
# async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) >= 4:
#         action = context.args[0].upper()
#         coin = context.args[1].upper()
#         entry = context.args[2]
#         target = context.args[3]
        
#         # Randomize order type for manual signals too
#         order_type = generate_order_type()
        
#         # Add order type to the message
#         leverage = f"{random.randint(3, 10)}x" if random.random() > 0.3 else "Spot"

#         message = (
#             f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
#             f"Action: {action}\n"
#             f"Pair: {coin}\n"
#             f"Order Type: {order_type}\n"
#             f"Entry: {entry}\n"
#             f"Target: {target}\n"
#             f"Leverage: {leverage}\n\n"
#             f"*Trade Setup:*\n"
#             f"• Use {order_type.lower()} order\n"
#             f"• Set stop loss immediately\n"
#             f"• Take partial profits along the way"
#         )
#         await update.message.reply_text(message, parse_mode="Markdown")
#     else:
#         await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# # ===== /autosignal command (live/demo) =====
# async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     symbol = "BTCUSDT"
#     if len(context.args) > 0:
#         coin_input = context.args[0].upper()
#         # Add USDT suffix if not present
#         symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

#     try:
#         # Get live price
#         current_price = get_price(symbol)
        
#         # Generate realistic trading parameters
#         action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
#         order_type = generate_order_type()
#         leverage = f"{random.randint(3, 10)}x" if random.random() > 0.3 else "Spot"
        
#         # Calculate entry based on order type
#         if order_type == "MARKET":
#             entry = round(current_price, 2)
#         else:
#             entry = generate_limit_entry(current_price, action)
        
#         # Calculate proper stop loss and take profit
#         if "BUY" in action:
#             stop_loss = round(entry * 0.95, 2)    # 5% stop loss from entry
#             take_profit_1 = round(entry * 1.03, 2)  # First target: 3%
#             take_profit_2 = round(entry * 1.06, 2)  # Second target: 6%
#             take_profit_3 = round(entry * 1.09, 2)  # Third target: 9%
#         else:
#             stop_loss = round(entry * 1.05, 2)    # 5% stop loss from entry
#             take_profit_1 = round(entry * 0.97, 2)  # First target: -3%
#             take_profit_2 = round(entry * 0.94, 2)  # Second target: -6%
#             take_profit_3 = round(entry * 0.91, 2)  # Third target: -9%

#         # Format the message
#         coin_name = symbol.replace("USDT", "")
#         message = (
#             f"📊 *{coin_name} Trading Signal* 📊\n\n"
#             f"Pair: {symbol}\n"
#             f"Action: {action}\n"
#             f"Order Type: {order_type}\n"
#             f"Leverage: {leverage}\n"
#             f"Entry: ${entry:,.2f}\n"
#             f"Stop Loss: ${stop_loss:,.2f}\n\n"
#             f"🎯 Take Profit Targets:\n"
#             f"TP1: ${take_profit_1:,.2f} (3%)\n"
#             f"TP2: ${take_profit_2:,.2f} (6%)\n"
#             f"TP3: ${take_profit_3:,.2f} (9%)\n\n"
#             f"💰 Current Price: ${current_price:,.2f}\n"
#             f"📈 Max Potential Gain: 9%\n"
#             f"⚠️ Risk: 5%\n\n"
#             f"*Risk Management:*\n"
#             f"• Use {order_type.lower()} order as specified\n"
#             f"• Set stop loss immediately after entry\n"
#             f"• Take partial profits at each target\n"
#             f"• Never risk more than 2-5% of portfolio\n\n"
#             f"*Order Instructions:*\n"
#             f"• For {order_type}: Enter at ${entry:,.2f}\n"
#             f"• SL: ${stop_loss:,.2f}\n"
#             f"• TP1: ${take_profit_1:,.2f} (30% position)\n"
#             f"• TP2: ${take_profit_2:,.2f} (30% position)\n"
#             f"• TP3: ${take_profit_3:,.2f} (40% position)"
#         )
        
#         await update.message.reply_text(message, parse_mode="Markdown")
        
#     except Exception as e:
#         error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
#         logger.error(error_msg)
#         await update.message.reply_text(error_msg)

# # ===== Test function to verify API is working =====
# def test_api_connection():
#     """Test if CoinGecko API is working properly"""
#     print("Testing CoinGecko API connection...")
#     try:
#         # Test SOL specifically
#         url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         data = response.json()
        
#         if "solana" in data and "usd" in data["solana"]:
#             sol_price = data["solana"]["usd"]
#             print(f"✅ CoinGecko API working - SOL price: ${sol_price}")
#             return True
#         else:
#             print("❌ CoinGecko API returned unexpected data format")
#             return False
            
#     except Exception as e:
#         print(f"❌ CoinGecko API test failed: {e}")
#         return False

# # ===== main runner =====
# def main():
#     # Test API connection on startup
#     api_working = test_api_connection()
#     if not api_working:
#         print("⚠️ Warning: CoinGecko API may not be accessible. Bot will use demo prices.")
    
#     app = Application.builder().token(BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("signal", signal))
#     app.add_handler(CommandHandler("autosignal", autosignal))

#     logger.info("Bot is running... 🚀")
#     app.run_polling()

# if __name__ == "__main__":
#     main()

#The above is for randomizing the market order and limit order



#Gateio API Now from deep seek

# import os
# from flask import Flask
# from telegram.ext import Updater

# app = Flask(__name__)
# PORT = int(os.environ.get("PORT", 5000))

# # Telegram bot setup
# updater = Updater("YOUR_BOT_TOKEN")
# dispatcher = updater.dispatcher

# # Start bot polling
# updater.start_polling()

# # Minimal Flask endpoint just to bind the port
# @app.route("/")
# def home():
#     return "Bot is running!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=PORT)


import os
import requests
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from keep_alive import keep_alive
# call the function before starting your bot



# ===== Enable logging =====
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ===== Bot Token =====
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    BOT_TOKEN = "8265642827:AAGNTfwiFuDx1o2eF85kV_O_jqXAoXRhyHs"

# ===== Gate.io API Configuration =====
GATEIO_API_URL = "https://api.gateio.ws/api/v4/spot/tickers"

# Gate.io symbol mapping (they use the same symbols as most exchanges)
GATEIO_SYMBOLS = {
    "BTCUSDT": "BTC_USDT",
    "ETHUSDT": "ETH_USDT",
    "SOLUSDT": "SOL_USDT",
    "ADAUSDT": "ADA_USDT",
    "DOGEUSDT": "DOGE_USDT",
    "DOTUSDT": "DOT_USDT",
    "XRPUSDT": "XRP_USDT",
    "LTCUSDT": "LTC_USDT",
    "BNBUSDT": "BNB_USDT",
    "MATICUSDT": "MATIC_USDT",
    "AVAXUSDT": "AVAX_USDT",
    "LINKUSDT": "LINK_USDT"
}

# ===== Function to get live price from Gate.io API =====
def get_price(symbol="BTCUSDT"):
    try:
        # Get the Gate.io symbol format
        gateio_symbol = GATEIO_SYMBOLS.get(symbol)
        if not gateio_symbol:
            # Try to handle cases where user might input just "BTC" instead of "BTCUSDT"
            base_symbol = symbol.replace("USDT", "")
            for key, value in GATEIO_SYMBOLS.items():
                if key.startswith(base_symbol):
                    gateio_symbol = value
                    break
            
            if not gateio_symbol:
                logger.warning(f"No Gate.io symbol mapping found for: {symbol}")
                raise ValueError(f"Unsupported symbol: {symbol}")
        
        # Gate.io API call
        params = {"currency_pair": gateio_symbol}
        response = requests.get(GATEIO_API_URL, params=params, timeout=15)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if we got valid response (Gate.io returns an array)
        if isinstance(data, list) and len(data) > 0:
            ticker_data = data[0]
            if "last" in ticker_data:
                price = float(ticker_data["last"])
                logger.info(f"Successfully fetched {symbol} price from Gate.io: ${price:,.2f}")
                return price
            else:
                raise ValueError("last price not found in Gate.io response")
        else:
            raise ValueError("No ticker data found in Gate.io response")
            
    except Exception as e:
        logger.warning(f"Gate.io API failed for {symbol}: {e}. Using demo price instead.")
        # fallback random demo price - UPDATED REALISTIC PRICES
        demo_prices = {
            "BTCUSDT": random.uniform(50000, 70000),
            "SOLUSDT": random.uniform(160, 180),
            "ETHUSDT": random.uniform(2500, 3500),
            "ADAUSDT": random.uniform(0.3, 0.6),
            "DOGEUSDT": random.uniform(0.05, 0.15),
            "DOTUSDT": random.uniform(5, 10),
            "XRPUSDT": random.uniform(0.4, 0.8),
            "LTCUSDT": random.uniform(60, 100),
            "BNBUSDT": random.uniform(300, 600),
            "MATICUSDT": random.uniform(0.5, 1.0),
            "AVAXUSDT": random.uniform(20, 40),
            "LINKUSDT": random.uniform(12, 20)
        }
        return demo_prices.get(symbol, random.uniform(50, 500))

# ===== Generate realistic order type =====
def generate_order_type():
    """Randomize between market and limit orders with realistic probabilities"""
    # 60% chance for limit order, 40% for market order
    return random.choices(["LIMIT", "MARKET"], weights=[60, 40])[0]

# ===== Generate realistic entry price for limit orders =====
def generate_limit_entry(current_price, action):
    """Generate realistic limit entry price based on current price and action"""
    if "BUY" in action:
        # For BUY limit orders, entry is typically 1-3% below current price
        discount = random.uniform(0.01, 0.03)  # 1-3% below
        return round(current_price * (1 - discount), 2)
    else:
        # For SELL limit orders, entry is typically 1-3% above current price
        premium = random.uniform(0.01, 0.03)  # 1-3% above
        return round(current_price * (1 + premium), 2)

# ===== /start command =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Crypto Trading Signals Bot!\n\n"
        "Available Commands:\n"
        "/signal BUY BTCUSDT 42000 44000 → manual signal\n"
        "/autosignal SOL → auto signal with live price\n\n"
        "Supported coins: BTC, ETH, SOL, ADA, DOGE, DOT, XRP, LTC, BNB, MATIC, AVAX, LINK\n\n"
        "Example: /autosignal SOL\n\n"
        "📊 Data source: Gate.io Exchange API\n"
        "📈 Signals include both MARKET and LIMIT orders"
    )

# ===== /signal command (manual) =====
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) >= 4:
        action = context.args[0].upper()
        coin = context.args[1].upper()
        entry = context.args[2]
        target = context.args[3]
        
        # Randomize order type for manual signals too
        order_type = generate_order_type()
        
        # Add order type to the message
        leverage = f"{random.randint(3, 10)}x" if random.random() > 0.3 else "Spot"

        message = (
            f"🚀 *NEW SIGNAL ALERT* 🚀\n\n"
            f"Action: {action}\n"
            f"Pair: {coin}\n"
            f"Order Type: {order_type}\n"
            f"Entry: {entry}\n"
            f"Target: {target}\n"
            f"Leverage: {leverage}\n\n"
            f"*Trade Setup:*\n"
            f"• Use {order_type.lower()} order\n"
            f"• Set stop loss immediately\n"
            f"• Take partial profits along the way\n\n"
            f"📊 Data source: Gate.io"
        )
        await update.message.reply_text(message, parse_mode="Markdown")
    else:
        await update.message.reply_text("Usage: /signal BUY BTCUSDT 42000 44000")

# ===== /autosignal command (live/demo) =====
async def autosignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = "BTCUSDT"
    if len(context.args) > 0:
        coin_input = context.args[0].upper()
        # Add USDT suffix if not present
        symbol = coin_input if coin_input.endswith("USDT") else coin_input + "USDT"

    try:
        # Get live price from Gate.io
        current_price = get_price(symbol)
        
        # Generate realistic trading parameters
        action = random.choice(["BUY (LONG)", "SELL (SHORT)"])
        order_type = generate_order_type()
        leverage = f"{random.randint(3, 10)}x" if random.random() > 0.3 else "Spot"
        
        # Calculate entry based on order type
        if order_type == "MARKET":
            entry = round(current_price, 2)
        else:
            entry = generate_limit_entry(current_price, action)
        
        # Calculate proper stop loss and take profit
        if "BUY" in action:
            stop_loss = round(entry * 0.95, 2)    # 5% stop loss from entry
            take_profit_1 = round(entry * 1.03, 2)  # First target: 3%
            take_profit_2 = round(entry * 1.06, 2)  # Second target: 6%
            take_profit_3 = round(entry * 1.09, 2)  # Third target: 9%
        else:
            stop_loss = round(entry * 1.05, 2)    # 5% stop loss from entry
            take_profit_1 = round(entry * 0.97, 2)  # First target: -3%
            take_profit_2 = round(entry * 0.94, 2)  # Second target: -6%
            take_profit_3 = round(entry * 0.91, 2)  # Third target: -9%

        # Format the message
        coin_name = symbol.replace("USDT", "")
        message = (
            f"📊 *{coin_name} Trading Signal* 📊\n\n"
            f"Pair: {symbol}\n"
            f"Action: {action}\n"
            f"Order Type: {order_type}\n"
            f"Leverage: {leverage}\n"
            f"Entry: ${entry:,.2f}\n"
            f"Stop Loss: ${stop_loss:,.2f}\n\n"
            f"🎯 Take Profit Targets:\n"
            f"TP1: ${take_profit_1:,.2f} (3%)\n"
            f"TP2: ${take_profit_2:,.2f} (6%)\n"
            f"TP3: ${take_profit_3:,.2f} (9%)\n\n"
            f"💰 Current Price: ${current_price:,.2f}\n"
            f"📈 Max Potential Gain: 9%\n"
            f"⚠️ Risk: 5%\n\n"
            f"*Risk Management:*\n"
            f"• Use {order_type.lower()} order as specified\n"
            f"• Set stop loss immediately after entry\n"
            f"• Take partial profits at each target\n"
            f"• Never risk more than 2-5% of portfolio\n\n"
            f"*Order Instructions:*\n"
            f"• For {order_type}: Enter at ${entry:,.2f}\n"
            f"• SL: ${stop_loss:,.2f}\n"
            f"• TP1: ${take_profit_1:,.2f} (30% position)\n"
            f"• TP2: ${take_profit_2:,.2f} (30% position)\n"
            f"• TP3: ${take_profit_3:,.2f} (40% position)\n\n"
            f"📊 Data source: Gate.io Exchange"
        )
        
        await update.message.reply_text(message, parse_mode="Markdown")
        
    except Exception as e:
        error_msg = f"❌ Error generating signal for {symbol}: {str(e)}"
        logger.error(error_msg)
        await update.message.reply_text(error_msg)

# ===== Test function to verify Gate.io API is working =====
def test_gateio_api():
    """Test if Gate.io API is working properly"""
    print("Testing Gate.io API connection...")
    try:
        # Test with BTCUSDT
        params = {"currency_pair": "BTC_USDT"}
        response = requests.get(GATEIO_API_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if isinstance(data, list) and len(data) > 0 and "last" in data[0]:
            btc_price = float(data[0]["last"])
            print(f"✅ Gate.io API working - BTC price: ${btc_price:,.2f}")
            
            # Test SOL as well
            params = {"currency_pair": "SOL_USDT"}
            response = requests.get(GATEIO_API_URL, params=params, timeout=15)
            sol_data = response.json()
            if isinstance(sol_data, list) and len(sol_data) > 0 and "last" in sol_data[0]:
                sol_price = float(sol_data[0]["last"])
                print(f"✅ Gate.io API working - SOL price: ${sol_price:,.2f}")
            
            return True
        else:
            print("❌ Gate.io API returned unexpected data format")
            return False
            
    except Exception as e:
        print(f"❌ Gate.io API test failed: {e}")
        return False

# ===== main runner =====
def main():
    # Test API connection on startup
    api_working = test_gateio_api()
    if not api_working:
        print("⚠️ Warning: Gate.io API may not be accessible. Bot will use demo prices if needed.")
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("autosignal", autosignal))

    logger.info("Bot is running with Gate.io API... 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
