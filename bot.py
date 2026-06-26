import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '8802480550:AAHgPSDumYu3QIEt3agoJ5cSIQLsk8-trIg'
bot = telebot.TeleBot(TOKEN)

# Получаем последние обновления
updates = bot.get_updates()

if updates:
    last_update = updates[-1]
    if last_update.message and last_update.message.text == '/start':
        chat_id = last_update.message.chat.id
        
        # Ссылка на твое мини-приложение
        web_app_url = 'https://sosnovdanya1710-ux.github.io/banan/' 
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Открыть профиль', web_app=WebAppInfo(url=web_app_url)))
        
        bot.send_message(chat_id, "Привет! Добро пожаловать в Retro Company.", reply_markup=markup)
      
