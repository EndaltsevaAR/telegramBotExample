# for import library at the terminal from https://pypi.org/project/pyTelegramBotAPI/
# pip install pyTelegramBotAPI
import telebot
from telebot import types

bot = telebot.TeleBot("5275642230:AAHMdVvO28bHPjuFI-ZtD1rQqBU0ZukY3kw")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://vk.com/schastye_na_ladoshke"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup
    website = types.KeyboardButton("Сайт")
    start = types.KeyboardButton("Старт")
    markup.add(website, start)
    bot.send_message(message.chat.id, "Помощь в пути", reply_markup=markup)



@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "hello":
        bot.send_message(message.chat.id, "И тебе", parse_mode="html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой id {message.from_user.id}", parse_mode="html")
    elif message.text == "photo":
        photo = open("иконка.jpg", "rb")
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Cool")


bot.polling(none_stop=True)
