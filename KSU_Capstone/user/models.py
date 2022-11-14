import json
from urllib import request
from flask import Flask, jsonify, request, session, render_template, redirect
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from .. import db
from bson import ObjectId

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
            #"_id": uuid.uuid4().hex,
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
        #return jsonify({'User': session['user']['user_type']}), 200
        if (session['user']['user_type'] != 0):
            return jsonify({ "error": "Invalid User Type" }), 401

        for x in db.users.find():
            #print(x)
            x['_id'] = str(x['_id'])
        return db.users.find()
    def get_user(id):
        result = db.users.find_one({'_id': id})

        user = {
            "_id": str(result['_id']),
            "name": result['name'],
            "email": result['email'],
            "user_type": result['user_type'],
            }
        return render_template('edit_user.html', title='Edit User', user=user, year=datetime.now().year)

    def edit_user(self):
        user = {
            "_id": request.form.get('id'),
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "user_type": request.form.get('user_type'),
            }

        #print(user['_id'])
        x = db.users.find_one({'_id': user['_id']})
        print('------------')
        print(x)
        print('------------')
        #return jsonify(x), 418

        result = db.users.update_one({'_id': ObjectId(user['_id'])}, {
            '$set':
                {
                    'name':user['name'],
                    'email':user['email'],
                    'user_type':user['user_type']
                    }
        }
        )
        if result.modified_count == 1:

            #print('------------')
            #print(user)
            #print('------------')
            return jsonify(user), 200

        return jsonify({ "error": "Process failed" }), 400
