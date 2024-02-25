import json
import telebot
from telebot import types
import random

bot = telebot.TeleBot('7140219652:AAGd6EAxI3N_MW6rmDB4cOzo20SlGTRNBxM')

with open('phrases.json', 'r', encoding='utf-8') as file:
    phrases = json.load(file)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Меню")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Рад что ты написал мне! Ты мне тему, а я тебе латинскую крылатую фразу на эту тему. Если готов то открывай меню!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Меню')
def menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Тема 1: Мудрость')
    btn2 = types.KeyboardButton('Тема 2: Любовь')
    btn3 = types.KeyboardButton('Тема 3: Сила и мощь')
    btn4 = types.KeyboardButton('Тема 4: Время и его ценность')
    btn5 = types.KeyboardButton('Тема 5: Успех и цели')
    btn6 = types.KeyboardButton('Тема 6: Дружба и отношения')
    btn7 = types.KeyboardButton('Тема 7: Истина и знание')
    btn8 = types.KeyboardButton('Тема 8: Жизненная философия')
    btn9 = types.KeyboardButton('Тема 9: Воля и решимость')
    btn10 = types.KeyboardButton('Тема 10: Свобода и независимость')
    btnExit = types.KeyboardButton('Выход')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btnExit)
    bot.send_message(message.from_user.id, 'На какую тему хочешь крылатую фразу?', reply_markup=markup)

@bot.message_handler(regexp=r"Тема (\d+): (.+)")
def send_phrase(message):
    phrase = get_random_phrase(message.text)
    bot.send_message(message.from_user.id, phrase)

@bot.message_handler(func=lambda message: message.text == 'Выход')
def exit_menu(message):
    remove_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Жаль что уходите, надеюсь на ваше скорейшее возвращение!", reply_markup=remove_markup)

def get_random_phrase(theme):
    r = random.randint(0, 9)
    return f"{phrases[theme][r]}"

bot.polling(none_stop=True, interval=0)