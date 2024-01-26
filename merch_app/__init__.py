from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'jaira'


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "onepiece_db"


mysql = MySQL(app)

from merch_app import routes