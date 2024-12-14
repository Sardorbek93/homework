import telebot
from telebot import types

token = "7897435329:AAG4Z69ikbBUHfH3sL5lCYwESFio_2vLfaw"

bot = telebot.TeleBot(token=token)

def create_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1 USD")
    btn2 = types.KeyboardButton("1 000 000 сум в USD")
    markup.add(btn1, btn2)
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.username
    print(message)
    bot.send_message(
        user_id,
        f'Привет {name}! Это бот-конвертер USD-UZS. Выберите опцию:',
        reply_markup=create_main_menu()
    )

@bot.message_handler(content_types=["text"])
def text(message):
    user_id = message.from_user.id
    user_text = message.text.lower()
    if user_text == "1 usd":
        bot.send_message(user_id, "1$ сегодня = 1 280 000 UZS")
    elif user_text == "1 000 000 сум в usd":
        bot.send_message(user_id, "1 000 000 сум = 78 USD")
    else:
        bot.send_message(user_id, "Я вас не понял. Пожалуйста, выберите одну из опций в меню.")

bot.infinity_polling()
