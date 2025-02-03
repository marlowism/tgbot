import function
from telegram.ext import Application,CommandHandler,ContextTypes,MessageHandler,filters
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')



def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start',function.start))
    application.add_handler(CommandHandler('help',function.help))
    application.add_handler(CommandHandler('roll', function.roll))
    application.add_handler(CommandHandler('emoji', function.emoji))
    application.add_handler(CommandHandler('factorial',function.factorial))
    application.add_handler(CommandHandler('pictures',function.random_image))
    application.add_handler(MessageHandler(filters.TEXT,function.msgtest))
    application.run_polling()

main()


