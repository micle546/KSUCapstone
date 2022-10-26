from datetime import datetime
from flask import Flask, render_template, session, redirect
from functools import wraps
from .. import app
from .models import Catalog_Item

#decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/user/login')
    return wrap


#routes
@app.route('/catalog/', methods=['GET'])
def get_catalog():
    return render_template('catalog.html', title='View Catalog', catalog=get_catalog_list(), year=datetime.now().year)

@app.route('/catalog/create/', methods=['GET'])
@login_required
def get_catalog_create():
    return render_template('create_catalog_item.html', title='Create Catalog Item', year=datetime.now().year, time_now=datetime.now().strftime('%x %X'))

@app.route('/catalog/create/', methods=['POST'])
@login_required
def post_catalog_create():
    return Catalog_Item.create_catalog_item()

@app.route('/catalog/view/', methods=['GET'])
def get_catalog_list():
    return Catalog_Item.fetch_catalog()

@app.route('/catalog/view/<id>', methods=['GET'])
@login_required
def get_catalog_item_by_id(id):
    return Catalog_Item.fetch_catalog_item(id)

@app.route('/catalog/edit/', methods=['POST'])
@login_required
def post_catalog_edit():
    return Catalog_Item().edit_ticket()
