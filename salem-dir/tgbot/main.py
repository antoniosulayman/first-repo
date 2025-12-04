from telebot import TeleBot
from telebot.types import Message

TG_TOKEN = "8418490898:AAGINviMI_pbgsDz2s14NTqiWUoYMnZ3Hbw"
bot = TeleBot(TG_TOKEN)

ALLOWED_USERS = [8420004567]

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    print('Message from ', message.from_user.id, message.from_user.username, message.from_user.full_name)

    if message.from_user.id not in ALLOWED_USERS:
        return
    
    bot.reply_to(message, "Привет! Я простой бот 👋")



@bot.message_handler(commands=['whoami'])
def send_welcome(message: Message):
    user = message.from_user
    bot.reply_to(message, f"First name: {user.first_name}\nLast name: {user.last_name}\nUsername: {user.username}\nID: {user.id}")


@bot.message_handler(func=lambda message: True)
def echo_all(message: Message):
    # print(f"User {user.full_name} ({user.id}) send '{message.text}'")
    bot.reply_to(message, message.text)



print("Start polling...")
bot.infinity_polling()
