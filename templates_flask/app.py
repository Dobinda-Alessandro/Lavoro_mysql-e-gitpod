from flask import render_template
from flask import Flask
import mysql.connector              #devo connettere la tabella clash royale 

app = Flask(__name__)

#connettere a mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()


@app.route('/')
def hello():
    return render_template('hello.html', name='Alessandro')

@app.route('/units')
def unitList():
    mycursor.execute("Select * FROM Clash_Unit")
    myresult = mycursor.fetchall()
    return render_template('Clash_units.html', units=myresult)
