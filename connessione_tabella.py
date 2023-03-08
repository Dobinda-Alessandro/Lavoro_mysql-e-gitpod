#mi permette di connettermi ad una tabella , se non esiste mi da errore 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)