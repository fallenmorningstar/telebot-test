import telebot
import sqlite3
import keyboards
import code_sql
import config

# Проверка наличия базы данных
code_sql.check_db()

# Активизация токена телеграм бота
bot = telebot.TeleBot(config.token)


# Проверка на существования пользователя в БД
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE user_id=?"
    cursor.execute(sql, [(message.from_user.id)])
    user = cursor.fetchone()
    if not user:
        bot.send_message(message.chat.id,
                         'Привет, мы с тобой еще не знакомы!\n' +
                         'Для дальнейшего взаимодействия отправь номер :3',
                         reply_markup=keyboards.NewUser)
    else:
        bot.send_message(message.chat.id,
                         '🍕🍣 С точки зрения питания мы живём в лучшее и одновременно в худшее из времён. 🥑🍆\n\n' +
                         '🖌 Пол Фридман\n' +
                         '📚 Еда: история вкуса\n',
                         reply_markup=keyboards.start_keyboard)


# Авторизация пользователя через отправку своего контакта

@bot.message_handler(content_types=['contact'])
def add_user(message):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    newdata = [
        (message.contact.user_id, message.contact.first_name, message.contact.last_name, message.contact.phone_number)]
    cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", newdata)
    conn.commit()
    bot.send_message(message.chat.id,
                     '👏 Приветствую ' + message.from_user.first_name + ' 👏\n'
                                                                        '💢 Перестань кушать что попало 💢\n' +
                     '😼 Создай свое меню или подтяни уже готовое 😼\n\n',
                     reply_markup=keyboards.start_keyboard)


# Функционал бота в главном меню

@bot.message_handler(content_types=['text'])
def send_text(message):
    text = message.text.lower()  # Присваеваем переменной "text" текст сообщения в нижнем регистре

    if text == "🔍 поиск меню":
        bot.send_message(message.chat.id,
                         'Ну что, ' + message.from_user.first_name + ' поехали 🌝\n' + 'ты определенно нажал 🔍 Поиск меню')
    elif text == "📚 категории питания":
        bot.send_message(message.chat.id,
                         'Ну что, ' + message.from_user.first_name + ' поехали 🌝\n' + 'ты определенно нажал 📚 Категории питания')
    elif text == "🏘 мое меню":
        bot.send_message(message.chat.id,
                         'Ну что, ' + message.from_user.first_name + ' поехали 🌝\n' + 'ты определенно нажал 🏘 Мое меню')
    elif text == "📝 обратная связь":
        bot.send_message(message.chat.id,
                         'Ну что, ' + message.from_user.first_name + ' поехали 🌝\n' + 'ты определенно нажал 📝 Обратная связь')


print("\n----------------------\nNicolas Bot за работой\n----------------------\n")

bot.polling()
