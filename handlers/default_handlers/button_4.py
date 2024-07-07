from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from handlers.default_handlers.state_handler import handle_state
import gspread

# Авторизация в Google Sheets
gc = gspread.service_account(filename='API_FILE') 

# Открытие Google таблицы
wks = gc.open("table_for_bot").sheet1

# Получение значения из ячейки А2
cell_value = wks.cell(2,1).value

# Функция для отправки сообщения с данными из Google Sheets
def send_google_sheets(message: Message):
    bot.send_message(message.chat.id, 'Получить значение А2 из гугл таблички \nЗначение: {}'.format(cell_value))
