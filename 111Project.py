import telebot
from datetime import time
from apscheduler.schedulers.background import BackgroundScheduler

# Ваш токен от BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки сообщения
def send_reminder():
    bot.send_message(chat_id=CHAT_ID, text="Не забудьте принять витамины!")

# Запускаем планировщик задач
scheduler = BackgroundScheduler()
scheduler.add_job(send_reminder, 'cron', hour='10')  # Устанавливаем время напоминания на 10 утра
scheduler.start()

# Обработчик команд
@bot.message_handler(commands=['start'])
def start(message):
    CHAT_ID = message.chat.id
    bot.reply_to(message, "Привет! Я буду напоминать вам принимать витамины.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
