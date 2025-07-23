from telegram import Bot
import os

# Токен и ID
TOKEN = os.environ.get("8094752756:AAFUdZn4XFlHiZOtV-TXzMOhYFlXKCFVoEs")
CHAT_ID = os.environ.get("5556108366")

bot = Bot(token=TOKEN)

def send_signal(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")
