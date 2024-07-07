from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from handlers.default_handlers.state_handler import handle_state

# URL адрес для карты Яндекса с меткой на Ленина 1
url = 'https://yandex.ru/maps/2/saint-petersburg/house/prospekt_lenina_1/Z0kYdg9pQUIOQFtjfXRycHpnZw==/?ll=30.092443%2C59.831503&z=17'

# Функция для отправки приветственного сообщения и ссылки на карту
def hello(message: Message):
    bot.send_message(message.chat.id, 'Привет, вот ссылка на Ленина 1\n {}'.format(url))