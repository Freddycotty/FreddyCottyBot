from sql import DataBase
db = DataBase()

def sample_responses(input_text):
  user_message = str(input_text).lower()
  
  query = db.cava_active(user_message)
  count = db.cavas_only(user_message)
  
  if query and count > 0:
    message_in = f"Temperatura en: {query[6]} {query[4]} \nRango desde {query[1]} {query[4]} hasta {query[2]} {query[4]} \n{query[0]} ( {query[3]} ) \nZona: {query[5]} \nSensor: {query[7]}"
  elif query == None and count > 0:
    message_in = '{0} existe pero no tiene registros'.format(user_message)
  else:
    message_in = '{0} no existe'.format(user_message)
  
  return message_in