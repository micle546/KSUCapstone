"""
The flask application package.
"""

#from mongita import MongitaClientDisk
from pymongo import MongoClient
from os import environ
from flask import Flask

app = Flask(__name__)
dev = b'\xf7\xd1\xd6\x80\xc6Vl\xd3\x0bs5\xf2*a3\x03' #Invalidated
app.secret_key = environ.get('FLASK_SECRET_KEY', 'dev')

#database

#client = MongitaClientDisk(host="./.mongita")
#client = MongoClient(environ.get('DATABASE_URL', 'localhost'), 27017)

#client = MongoClient(environ.get('DATABASE_URL', 'localhost'), 27017)

local = 'mongodb://localhost:27017/'
#db_user = environ.get('DATABASE_USER')
db_url = environ.get('DATABASE_URL', local)


#conn_str = "mongodb+srv://" + db_user + "@"+ db_url


client = MongoClient(db_url, serverSelectionTimeoutMS=5000)


db = client.db
user_db = db.users
ticket_db = db.tickets
catalog_db = db.catalog


from . import views
