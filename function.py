from telegram import Update,InputFile
from telegram.ext import Application,CommandHandler,ContextTypes,MessageHandler,filters
from random import randint, random, choice
import math_function
import os

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text('Привет я новый бот')

async def help(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text('test')

async def msgtest(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    user_msg = update.message.text
    await update.message.reply_text(f'Вы написали сообщение:{user_msg}')

async def roll(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    dice = randint(1,6)
    print(dice)
    await update.message.reply_text(f'Выпало число: {dice}')

async def emoji(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    emojis = ["😊", "😂", "🥳", "🙃", "😎", "🤔", "😜"]
    await update.message.reply_text(choice(emojis))

async def factorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_says = " ".join(context.args)
    f= math_function.factorial(int(user_says))
    await update.message.reply_text(f)

async def random_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    import random
    mdir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(mdir,'images')

    try:
        images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder,f))]
        if not images:
            await update.message.reply_text('empty request')
            return

        random.shuffle(images)
        rand_image = os.path.join(image_folder,choice(images))

        print((f'pictname:{rand_image}'))

        with open(rand_image,'rb') as photo:
            await context.bot.send_photo(update.message.chat_id,photo=photo)

    except Exception as e:
        await update.message.reply_text(f'{e}')