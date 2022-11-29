from datetime import datetime
from gettext import Catalog
import json
from re import search
from flask import Flask, render_template, session, redirect, request, jsonify, url_for
from functools import wraps
from .. import app
from .models import Catalog_Item
from .book_data import get_book_data

#decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/user/login')
    return wrap

def elevateduser_required(f): #
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_type' in session['user']:
            if session['user']['user_type'] == '2' or session['user']['user_type'] == '3':
                return f(*args, **kwargs)
            else:
                print (session['user']['user_type'])
                return jsonify({ "error": "Invalid User Type" }), 401
        else:
            print (session['user']['user_type'])
            return jsonify({ "error": "Session error, please relogin, if issue persists contact admin" }), 401
    return wrap


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_type' in session['user']:
            if session['user']['user_type'] == '3':
                return f(*args, **kwargs)
            else:
                print (session['user']['user_type'])
                return jsonify({ "error": "Invalid User Type" }), 401
        else:
            print (session['user']['user_type'])
            return jsonify({ "error": "Session error, please relogin, if issue persists contact admin" }), 401
    return wrap


#routes
@app.route('/catalog/', methods=['GET'])
def get_catalog():
    return render_template('catalog.html', title='View Catalog', catalog=get_catalog_list(), year=datetime.now().year)

@app.route('/catalog/create/', methods=['GET'])
@login_required
@elevateduser_required
def get_catalog_create():
    return render_template('create_catalog_item.html', title='Create Catalog Item', year=datetime.now().year, time_now=datetime.now().strftime('%x %X'))

@app.route('/catalog/create/<isbn>', methods=['GET'])
@login_required
@elevateduser_required
def get_catalog_create_isbn(isbn):
    #catalog_item = get_book_data(isbn)
    #print(catalog_item)
    print('test_hit')
    return render_template('create_catalog_item_quickfill.html', catalog_item=get_book_data(isbn), title='Create Catalog Item', year=datetime.now().year, time_now=datetime.now().strftime('%x %X'))


@app.route('/catalog/create/', methods=['POST'])
@app.route('/catalog/create/<isbn>', methods=['POST'])
@login_required
@elevateduser_required
def post_catalog_create():
    print(request.form)
    if 'isbn-auto' in request.form:
        print('easyfill')
        print(request.form.get('isbn-auto'))

        return jsonify({"redirect": "/catalog/create/"+request.form.get('isbn-auto')})
    
        return redirect('/catalog/create/'+request.form.get('isbn-auto'),303)
        return redirect(url_for('get_catalog_create_isbn',isbn=request.form.get('isbn-auto')))
        #return get_catalog_create_isbn(isbn=request.form['isbn-auto'])
    elif 'isbn' in request.form:
        return Catalog_Item().create_catalog_item()
    else:
         return jsonify({ "error": "Unknown Error" }), 401
    #else: print(request.form)

@app.route('/catalog/view/', methods=['GET'])
def get_catalog_list():
    return Catalog_Item.fetch_catalog()

@app.route('/catalog/view/<id>', methods=['GET'])
@login_required
def get_catalog_item_by_id(id):
    return Catalog_Item.fetch_catalog_item(id)

@app.route('/catalog/edit/', methods=['POST'])
@login_required
@elevateduser_required
def post_catalog_edit():
    return Catalog_Item().edit_catalog_item()

@app.route('/catalog/search')
def catalog_search():
    searchTerm = request.args.get('q')
    #return Catalog_Item.searchCatalog(searchTerm)
    return render_template('catalog.html', title='Search Catalog', catalog=Catalog_Item.searchCatalog(searchTerm), year=datetime.now().year)