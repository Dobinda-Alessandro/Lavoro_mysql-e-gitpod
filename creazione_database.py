# crea una connessione tra python e il database in mysql
import mysql.connector

mydb = mysql.connector.connect(          #connettere database
  host="localhost",                      #chi riceve ilcomando dovesta ilrepository inquesto caso e la nostra stessa macchina  
  user="root",                #nome utente root è il nomeautomatico 
  password=""
)

mycursor = mydb.cursor()            #crea uncursoree sulla consolee e scrivi quello che ce tra virgolette , simula cursore 

mycursor.execute("CREATE DATABASE mydatabase")#questomipermettere crearedatabese 
#ora possiamo interrogare il nostro database usando le istruzioni di sql