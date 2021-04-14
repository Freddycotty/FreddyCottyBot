import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton

INPUT_TEXT = 0 #CONSTANTE



def start(update, context):
  button1 = InlineKeyboardButton( #PERMITE DEFINIR LOS BOTONES
    text = 'Generar qr',
    callback_data = 'qr' 
  )
  
  button2 = InlineKeyboardButton( #PERMITE DEFINIR LOS BOTONES
    text = 'Sobre el autor',
    url = 'google.com' 
  )
  update.message.reply_text(  #FUNCION PARA RESPONDER EN TELEGRAM
    text = 'Hola, bienvenido, que deseas hacer?\n\nUsa /qr para generar un codigo qr.',
    reply_markup=InlineKeyboardMarkup([ #PERMITE DEFINIR EL TECLADO DE BOTONES
       [button1], [button2]
    ])
  )

def qr_command_handler(update, context):
  update.message.reply_text('Enviame el texto para generar un codigo QR.') #FUNCION PARA RESPONDER EN TELEGRAM
  
  return INPUT_TEXT #RETORNA LA CONSTANTE

def qr_callback_handler(update, context):
  query = update.callback_query #OBTENEMOS LA INFORMACION
  query.answer() #MANERA DE RESPONDER LA INFORMACION QUE LLEGA SIN DEVOLVER NADA A CAMBIO
  query.edit_message_text( #REEMPLAZAR EL MENSAJE DEL BOTON POR EL TEXTO
    text = 'Enviame el texto para generarte un codigo QR'
  )
  return INPUT_TEXT

def generate_qr(text):
  filename = text + '.jpg' #CREAMOS EL NOMBRE DE COMO SE VA A GUARDAR
  img = qrcode.make(text) #CONVERTIR TEXTO EN QR
  img.save(filename) #GUARDAR IMAGEN

  return filename
    
def send_qr(filename, chat):
  #METODO PARA CAMBIAR STATUS DEL BOT
  chat.send_action( 
    action = ChatAction.UPLOAD_PHOTO,
    timeout = None
  )
  #METODO PARA ENVIAR FOTO
  chat.send_photo( 
    photo = open(filename, 'rb') 
  )
  #METODO PARA ELIMINAR EL ARCHIVO DE MI PC
  os.unlink(filename)

def input_text(update, context):
  text = update.message.text #OBTENEMOS LO QUE ENVIO EL USUARIO
  filename = generate_qr(text) #FUNCION PARA GENERAR QR
  chat = update.message.chat #OBTIENE LOS VALORES UNICOS DEL USUARIO
  send_qr(filename, chat)

  return ConversationHandler.END




if __name__ == '__main__':
  updater = Updater(token = '1736125265:AAGvnWFOUspKJxZa0hyLtqf9sGwcNzzNSms', use_context = True)
  
  dp = updater.dispatcher
  
  dp.add_handler(CommandHandler('start', start))
  
  #INICIAR UNA CONVERSACION CON EL BOT
  dp.add_handler(ConversationHandler(  
    #PUNTOS DE ENTRADAS
    entry_points = [ 
      CommandHandler('qr', qr_command_handler), #LA CONVERSACION COMIENZA DESDE QUE EJECUTAN ESTE COMANDO
      CallbackQueryHandler(pattern='qr', callback = qr_callback_handler) #LA CONVERSACION COMIENZA DESDE QUE LE DA CLICK A ESTE BOTON
    ],
    #ESTADOS
    states = { 
      INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
    },
    
    fallbacks = []
    
  ))
  
  updater.start_polling()
  updater.idle()