from telegram.ext import *
import constants as key
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import requests
import constants as key
import celebrate as celebrate


print("Bot has been initiated...")
def start_command(update, context):
    update.message.reply_text('Enter Firstname of the person to get a card')

def help_command(update, context):
    update.message.reply_text('I dont usually help people!')

def handle_message(update, context):
    fname=str(update.message.text)
    print(fname)
    print('second function!!!')
    hbdcard(fname)

def error(update,context):
    print(update, context.error)

def hbdcard(name):
    print("Executed")
    image = cv2.imread("bday test.png")
    print("second function called")
    fontpath = "./SCRIPTIN.ttf" 
    font = ImageFont.truetype(fontpath, 80)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text((700, 850), name, font = font, fill = (0, 0, 0, 100))
    img = np.array(img_pil)
    cv2.imwrite("thecard.png", img)
    card={'photo' :open('thecard.png', 'rb')}
    requests.post('https://api.telegram.org/bot{bot}/sendPhoto?chat_id={chatid}'.format(chatid=key.CHAT_ID, bot=key.API_KEY),files=card)

def main():
    updater=Updater(key.API_KEY, use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()

