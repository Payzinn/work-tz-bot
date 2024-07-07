from telebot.types import Message
from telebot import types
from config_data.config import DEFAULT_COMMANDS
from loader import bot

from telebot.types import Message
from loader import bot
from handlers.default_handlers.state_handler import handle_state, welcome

@bot.message_handler(commands=["start"])
def start_command(message: Message):
    welcome(message)

@bot.message_handler(func=lambda message: True)
def all_messages(message: Message):
    handle_state(message)
