from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
Updater = Updater(token='742436892:AAFbXa-lJFdSJ-km1NdFqfr8pMO9pthAw6E') 
dispatcher = Updater.dispatcher
import requests
info_company = input('Введите УНП: ')
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
response = requests.get('https://api.telegram.org/bot742436892:AAFbXa-lJFdSJ-km1NdFqfr8pMO9pthAw6E/sendMessage?chat_id=251325174&text=Информация по запрошенному контррагенту:\n'+info_company)
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)