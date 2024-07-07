from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from handlers.default_handlers.state_handler import handle_state
from config_data.config import YOO_MONEY_TOKEN
from yoomoney import Client, Quickpay
from uuid import uuid4

# Инициализация YooMoney токена
client = Client(YOO_MONEY_TOKEN)

# Генерация уникального идентификатора для платежа
label = str(uuid4)

# Создание объекта платежа
quickpay = Quickpay(
    receiver='410011161616877',  
    quickpay_form='shop',        
    targets='Тестовый платёж',  
    paymentType='SB',            
    sum=2,                       
    label=label                  
)

# Получение URL для перенаправления на страницу оплаты
payment_url = quickpay.redirected_url

# Функция для отправки сообщения с ссылкой на оплату
def payment(message: Message):
    bot.send_message(message.chat.id, "Привет, вот форма на оплату Юмани на 2 рубля \n{}".format(payment_url))