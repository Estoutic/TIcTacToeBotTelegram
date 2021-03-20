import telebot
from telebot import types
bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    yes_bt = types.InlineKeyboardButton(text='Да', callback_data='yes')
    no_bt = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(yes_bt)
    keyboard.add(no_bt)
    bot.send_message(message.chat.id, 'you wanna play tic tac toe?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'yes':
        keyboard = types.InlineKeyboardMarkup()
        first = types.InlineKeyboardButton(text = "a")
        second = types.InlineKeyboardButton(text = "s")
        three = types.InlineKeyboardButton(text = "d")
        four = types.InlineKeyboardButton(text = "d")
        five = types.InlineKeyboardButton(text = "d")
        six = types.InlineKeyboardButton(text = "d")
        seven = types.InlineKeyboardButton(text = "d")
        eight = types.InlineKeyboardButton(text = "d")
        nine = types.InlineKeyboardButton(text = "d")
        keyboard.add(first)
        keyboard.add (second)
        keyboard.add(three)
        keyboard.add(four)
        keyboard.add(five)
        keyboard.add(six)
        keyboard.add(seven)
        keyboar.add(eight)
        keyboard.add(nine)
        bot.send_message(call.message.chat.id, 'p', reply_markup=keyboard)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id,'пока')
bot.polling(none_stop=True, interval=0, timeout=0)

