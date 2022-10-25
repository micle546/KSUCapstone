"""
The flask application package.
"""

from mongita import MongitaClientDisk
from os import environ
from flask import Flask

app = Flask(__name__)
dev = b'\xf7\xd1\xd6\x80\xc6Vl\xd3\x0bs5\xf2*a3\x03' #Invalidated
app.secret_key = environ.get('FLASK_SECRET_KEY', 'dev')

#database
client = MongitaClientDisk(host="./.mongita")
db = client.db
user_db = db.users
ticket_db = db.tickets
#counter_db = db.counters

from . import views
