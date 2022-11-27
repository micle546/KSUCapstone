from datetime import datetime
from flask import Flask, render_template, session, redirect, jsonify
from functools import wraps
from .. import app
from .models import User

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
@app.route('/user/login/', methods=['GET'])
def get_login():
    return render_template('login.html', title='Login', year=datetime.now().year)

@app.route('/user/signup_user/', methods=['POST'])
def post_signup():
    return User().signup()

@app.route('/user/login_user/', methods=['POST'])
def post_login():
    return User().login()

@app.route('/user/page/', methods=['GET'])
def page():
    return render_template('page.html')

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/users/', methods=['GET'])
@login_required
@admin_required
def get_users():
    return render_template('users.html', title='View Users', user_list=User.get_users_list(), year=datetime.now().year)
    #return User().get_users()

@app.route('/users/<id>', methods=['GET'])
@login_required
@admin_required
def get_user_by_id(id):
    return User.get_user(id)

@app.route('/users/edit/', methods=['POST'])
@login_required
@admin_required
def post_user_edit():
    return User().edit_user()