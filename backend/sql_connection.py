import mysql.connector
import datetime
__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
     __cnx = mysql.connector.connect(user='root', password='Nidhi2410@', database='gs')

  return __cnx