from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from sql import DataBase
import response as R
INPUT_TEXT = 0

db = DataBase()

def cavas_command_handler(update, context):

  update.message.reply_text('Cavas Activas:') #FUNCION PARA RESPONDER EN TELEGRAM
  for cavas in db.consult():
    update.message.reply_text(cavas[1])

def start_command_handler(update, context):
  bot = context.bot
  chatId = update.message.chat.id
  first_name = update.message.chat.first_name
  last_name = update.message.chat.last_name
  
  bot.sendMessage(
    chat_id = chatId,
    parse_mode = "HTML",
    text = f'Bienvenido <b>{first_name} {last_name}</b> Somo un bot creado por Freddy y Gabriel para Gonavi'
  )

def handle_message(update, context):
  bot = context.bot
  chatId = update.message.chat.id
  text = str(update.message.text).lower()
  response = R.sample_responses(text)
  
  bot.sendMessage(
    chat_id = chatId,
    parse_mode = 'HTML',
    text = response
  )

if __name__ == '__main__':
  updater = Updater(token = '1744556777:AAEXPIy4hNeqJRpenhe8oQu1W-fvTjPB4Jg', use_context = True)
  dp = updater.dispatcher
  
  dp.add_handler(CommandHandler('start', start_command_handler)) #INICIO
  dp.add_handler(CommandHandler('cavas', cavas_command_handler)) #CAVAS ACTIVAS
  dp.add_handler(MessageHandler(Filters.text, handle_message)) #CONSULTA DE CAVAS
  
  updater.start_polling()
  updater.idle()