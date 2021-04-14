import pymysql

class DataBase:
# Realizando conexion a la bdd
  def __init__(self):
    self.connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db=""
    )

    self.cursor = self.connection.cursor()
  
  #CAVAS ACTIVAS PLURAL
  def consult(self):
    sql = 'SELECT * FROM temperatura.cavas WHERE status = 1'
    self.cursor.execute(sql)
    row = self.cursor.fetchall()
    return row

  #CAVAS ACTIVAS EN ESPECIFICO
  def cava_active(self, cava): 
    
    
    sql = """SELECT tc.nombre, tc.min_temp, tc.max_temp, ta.nombre, tg.simbolo, tz.nombre, tt.temperatura, tz.sensor_id FROM temperatura.cavas tc 
              INNER JOIN temperatura.areas ta ON ta.id = tc.area_id 
              INNER JOIN temperatura.grados tg ON tg.id = tc.grado_id
              INNER JOIN temperatura.zonas tz ON tz.cava_id = tc.id
              INNER JOIN temperatura.temperaturas tt ON tt.zona_id = tz.id 
              WHERE tc.status = 1 AND tc.nombre = '{0}' ORDER BY tt.id desc""".format(cava)

    self.cursor.execute(sql)
    row = self.cursor.fetchone()
    return row

  #CAVAS ACTIVAS PERO SI REGISTROS
  def cavas_only(self, cava):
    sql = "SELECT * FROM temperatura.cavas WHERE status = 1 AND nombre = '{0}'".format(cava)

    self.cursor.execute(sql)
    count = self.cursor.rowcount
    return count