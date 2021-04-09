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
  
  
  update.message.reply_text(
    text = 'Haz click en un boton',
    reply_markup=InlineKeyboardMarkup([
      [button1],
      [button2]
    ])
  )


if __name__ == '__main__':
  updater = Updater(token = '1736125265:AAGvnWFOUspKJxZa0hyLtqf9sGwcNzzNSms', use_context = True)
  
  dp = updater.dispatcher
  
  dp.add_handler(CommandHandler('start', start))
  
  updater.start_polling()
  updater.idle()