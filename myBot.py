# pip install python-telegram-bot==13.11
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackContext
API_KEY="6409569557:AAGs279Akazn_Yk6haI97aKQA32roMIZWjo"
updater = Updater(token=API_KEY, use_context=True)
def fn_diary(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    if '종료' in user_text:
        context.bot.send_message(chat_id=user_id, text='다이어리 종료')
    else:
        print("메모 쓰는 기능")
        f = open('diary.txt', 'a', encoding='utf-8')
        msg = user_text.replace('/d', '').strip()   # 파일저장하기
        f.write(msg)
        f.writelines('\n')
        f.close()
        context.bot.send_message(chat_id=user_id, text="내용을 추가함.")
import os
from datetime import datetime
def fn_save_photo(update, context:CallbackContext): # 사진 저장하기 함수
    img_dir = './img/'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    current = datetime.now()
    str_date = current.strftime('%Y%m%d%H%M%S')     # 년월일시분초
    file_path = os.path.join('./img', str_date + '.png')
    bot = context.bot
    photo = bot.getFile(update.message.photo[-1].file_id)
    photo.download(file_path)
    update.message.reply_text('photo save')

def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id=user_id, text=user_text)
echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)
updater.dispatcher.add_handler(echo_handler)

diary_handler = CommandHandler('d', fn_diary)
updater.dispatcher.add_handler(diary_handler)

photo_handler = MessageHandler(Filters.photo, fn_save_photo)
updater.dispatcher.add_handler(photo_handler)
updater.start_polling()
updater.idle()