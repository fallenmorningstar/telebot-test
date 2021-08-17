import telebot
from telebot import types

work_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
work_keyboard_but = types.KeyboardButton(text='/work')
work_keyboard.add(work_keyboard_but)

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
start_keyboard.row('🔍 Поиск меню', '📚 Категории питания')
start_keyboard.row('🏘 Мое меню', '📝 Обратная связь')

NewUser = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
key_b = types.KeyboardButton(text='Отправить контакт', request_contact=True)
NewUser.add(key_b)
