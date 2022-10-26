import json
from urllib import request
from flask import Flask, jsonify, request, session, render_template, redirect
from passlib.hash import pbkdf2_sha256
from .. import db

import uuid

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user

        return jsonify(user), 200


    def signup(self):

        #create user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "user_type": 0,
            "password": request.form.get('password'),
            }

        #encrypt
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #check for existing user
        if db.users.find_one({"email": user['email'] }):
            return jsonify({ "error": "Email address already in use" }), 400

        #database
        if db.users.insert_one(user):
            return self.start_session(user)
        
        return jsonify({ "error": "Signup failed" }), 400

    def signout(self):
        session.clear()
        return redirect('/')
        return render_template('index.html', year=datetime.now().year)

    def login(self):

        user = db.users.find_one({
            "email": request.form.get('email')
            })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        else:
            return jsonify({"error": "Invaild login credentials"}), 401

    def get_users(self):
        if (session['user']['user_type'] != 2):
            return jsonify({ "error": "Invalid User Type" }), 401