from telebot.types import Message
from loader import bot
from telebot import types
from datetime import datetime
import gspread

# Инициализация подключения к Google Sheets
try:
    gc = gspread.service_account(filename='API_FILE')
    wks = gc.open("table_for_bot").sheet1
except Exception as e:
    print(f"Ошибка при инициализации Google Sheets: {str(e)}")

# Создание клавиатуры с кнопками
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
first_button = types.KeyboardButton('🌤️ Кнопка 1')
second_button = types.KeyboardButton('💵 Кнопка 2')
third_button = types.KeyboardButton('🏬 Кнопка 3')
fourth_button = types.KeyboardButton('🎃 Кнопка 4')
markup.add(first_button, second_button, third_button, fourth_button)

# Установка формата даты
date_format = "%d.%m.%y"

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message: Message):
    if message.text == "/start" or message.text == '🌤️ Кнопка 1' or message.text == '💵 Кнопка 2' or message.text == '🏬 Кнопка 3' or message.text == '🎃 Кнопка 4':
        handle_state(message)
    else:
        check_date(message)

# Обработка состояний бота
def handle_state(message: Message):
    text = message.text
    if text == "/start":
        welcome(message)
    elif text == '🌤️ Кнопка 1':
        from handlers.default_handlers.button_1 import hello
        hello(message)
    elif text == '💵 Кнопка 2':
        from handlers.default_handlers.button_2 import payment
        payment(message)
    elif text == '🏬 Кнопка 3':
        from handlers.default_handlers.button_3 import show_image
        show_image(message)
    elif text == '🎃 Кнопка 4':
        from handlers.default_handlers.button_4 import send_google_sheets
        send_google_sheets(message)
    else:
        bot.send_message('Неизвестная команда.')

# Проверка формата даты и запись в Google Sheets
def check_date(message: Message):
    user_date = message.text
    try:
        # Проверка формата даты на соответствие дд.мм.гг
        datetime.strptime(user_date, date_format)
        
        last_row = len(wks.col_values(2))  
        next_row = last_row + 1
        
        # Запись даты в Google Sheets
        wks.update_cell(next_row, 2, user_date)
        bot.reply_to(message, "Дата верна")
    except ValueError:
        bot.reply_to(message, "Дата неверна")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")
        print(f"Ошибка при обработке даты: {str(e)}")  

# Приветственное сообщение
def welcome(message: Message):
    print(f'{message.from_user.username} Вхождение в функцию welcome')
    bot.send_message(message.chat.id, f'''Привет {message.from_user.username}, 
я бот, мой функционал представлен ниже.''', reply_markup=markup)