from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

INPUT_TEXT = 0



def start(update, context):
  
  button1 = InlineKeyboardButton(
    text = 'Sobre el autor',
    url = 'google.com' 
  )
  
  button2 = InlineKeyboardButton(
    text = 'Twitter',
    url = 'Twitter.com' 
  )
  
  
  update.message.reply_text( #FUNCION PARA RESPONDER EN TELEGRAM
    text = 'Haz click en un boton',
    reply_markup=InlineKeyboardMarkup([
      [button1],
      [button2]
    ])
  )


if __name__ == '__main__':
  updater = Updater(token = '1736125265:AAGvnWFOUspKJxZa0hyLtqf9sGwcNzzNSms', use_context = True) #FUNCION PARA CONECTARSE A TELEGRAM CON EL TOKEN
  
  dp = updater.dispatcher #PARA USAR LAS FUNCIONES DE LA LIBRERIA
  
  dp.add_handler(CommandHandler('start', start)) #EJECUTAR UNA FUNCION
  
  # EJECUTAR EL SCRIPT
  updater.start_polling()
  updater.idle()