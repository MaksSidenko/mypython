# import telebot
# import config
# import random

# from telebot import types

# bot = telebot.TeleBot(config.TOKEN)

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     sti = open("telegram_bot_start_img.webp", "rb")
#     bot.send_sticker(message.chat.id, sti)

#     # Keyboard    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("random number")
#     item2 = types.KeyboardButton("how\'s going?")

#     markup.add(item1, item2)

#     bot.send_message(message.chat.id, "Welcome dude, {0.first_name}!\nЯ - <b>{1.first_name}</b>, blah, blah, blah, blah".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    


# @bot.message_handler(content_types=['text'])
# def guess(message):
#     if message.chat.type == 'private':
#         if message.text == 'random number':
#             bot.send_message(message.chat.id, str(random.randint(0, 19)))
#         elif message.text == 'how\'s going?':
                
#             markup = types.InlineKeyboardMarkup(row_width=2)
#             item1 = types.InlineKeyboardButton('pretty good', callback_data='good')
#             item2 = types.InlineKeyboardButton('pretty bad', callback_data='bad')

#             markup.add(item1, item2)

#             bot.send_message(message.chat.id, 'how\'s going', reply_markup=markup)
#         else:
#             bot.send_message(message.chat.id, 'i have no answer') 


# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):   
#     try:
#         if call.message:
#             if call.data == 'good':
#                 bot.send_message(call.message.chat.id, 'nice')
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'nuh')  
#             # remote inline buttons 
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как дела?', reply_markup=None)    

#             # show alert
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='it\'s test message')             

#     except Exception as e:
#         print(repr(e))        
# # run

# bot.polling(none_stop=True)


# 2222222
import config
import  logging
from aiogram import Bot, Dispatcher, executor, types
from tg_db import Telegram_bot_db

logging.basicConfig(level=logging.INFO)

bot = Bot(token = config.API_TOKEN)
dp = Dispatcher(bot)

db = Telegram_bot_db('db.db')


#команда активации подписки 
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if(not db.subs_exists(message.from_user.id)):
        #если юзера нет в базе данных, добавляем его
        db.add_subs(message.from_user.id)
    else:
        #если он уже есть то просто обнавляем статус подписки
        db.update_subs(message.from_user.id, True)
    await message.answer("вы успешно подписались на рассылку! \nЖдите обновлений")

#команда отписки  
@dp.message_handler(commands=['unsubscribe'])   
async def unsubscribe(message: types.Message):
    if(not db.subs_exists(message.from_user.id)):
    #если юзера нет в базе, добавляем его с неактивно подпиской (запоминаем)
        db.add_subs(message.from_user.id, False)
        await message.answer("Вы и так не подписаны.")
    else:
        #если он уже есть то просто обновляем статус подписки
        db.update_subs(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки")


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)    

