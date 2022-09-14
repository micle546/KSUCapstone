"""
The flask application package.
"""
from os import environ
from flask import Flask

app = Flask(__name__)

dev = b'\xf7\xd1\xd6\x80\xc6Vl\xd3\x0bs5\xf2*a3\x03' #Invalidated
app.secret_key = environ.get('FLASK_SECRET_KEY', 'dev')

import KSU_Capstone.views
