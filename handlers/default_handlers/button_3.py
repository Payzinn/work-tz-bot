from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from handlers.default_handlers.state_handler import handle_state

# Функция для отправки изображения
def show_image(message: Message):
    # Открываем файл изображения
    with open('images/img1.jpg', 'rb') as photo:
        bot.send_message(message.chat.id, 'Вот картинка')
        bot.send_photo(message.chat.id, photo)