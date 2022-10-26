from datetime import datetime
import json
from unittest import result
from urllib import request
from flask import Flask, jsonify, request, session, render_template, redirect
from .. import catalog_db
from bson import ObjectId

class Catalog_Item():
    def fetch_catalog_item(id):
        #print('------mark----')

        result = catalog_db.find_one({'_id': id})

        #print('***********')
        #print(result)
        #print('***********')

        catalog_item = {
        "_id": str(result['_id']),
        "item_status": result['item_status'],
        "checkedout_to": result['checkedout_to'],
        "title": result['title'],
        "desc": result['desc'],
        "isbn": result['isbn'],
        "item_type": result['item_type'],
        "modified_user": result['modified_user'],
        "create_time": result['create_time'],
        "modified_time": result['modified_time']
        }

        #print('***********')
        #print(ticket)
        #print('***********')

        return render_template('edit_ticket.html', title='Edit Ticket', catalog_item=catalog_item, year=datetime.now().year)

    def fetch_catalog():
        
        for x in catalog_db.find():
            #print(x)
            x['_id'] = str(x['_id'])
        return catalog_db.find()        

    def create_catalog_item(self):

        #create ticket object
        catalog_item = {
            #"_id": uuid.uuid4().hex,
            "item_status": request.form.get('item_status'),
            "checkedout_to": request.form.get('checkedout_to'),
            "title": request.form.get('title'),
            "desc": request.form.get('desc'),
            "isbn": request.form.get('isbn'),
            "item_type": request.form.get('item_type'),
            "modified_user": session['user']['email'],
            "create_time": datetime.now().strftime('%x %X'),
            "modified_time": datetime.now().strftime('%x %X')
            }


        #database
        result = catalog_db.insert_one(catalog_item)
        if result.inserted_id:
            return jsonify(str(result.inserted_id)), 200
        
        return jsonify({ "error": "Process failed" }), 400

    def edit_ticket(self):

        catalog_item = {
            "_id": request.form.get('id'),
            "item_status": request.form.get('item_status'),
            "checkedout_to": request.form.get('checkedout_to'),
            "title": request.form.get('title'),
            "desc": request.form.get('desc'),
            "isbn": request.form.get('isbn'),
            "item_type": request.form.get('item_type'),
            "modified_user": session['user']['email'],
            "create_time": request.form.get('create_time'),
            "modified_time": datetime.now().strftime('%x %X')
            }
        #print(ticket['_id'])
        x = catalog_db.find_one({'_id': catalog_item['_id']})
        print('------------')
        print(x)
        print('------------')
        #return jsonify(x), 418

        result = catalog_db.update_one({'_id': ObjectId(catalog_item['_id'])}, {
            '$set':
                {
                    'item_status':catalog_item['item_status'],
                    'checkedout_to':catalog_item['checkedout_to'],
                    'title':catalog_item['title'],
                    'desc':catalog_item['desc'],
                    'isbn':catalog_item['isbn'],
                    'item_type':catalog_item['item_type'],
                    "modified_user": session['user']['email'],
                    'create_time':catalog_item['create_time'],
                    'modified_time':datetime.now().strftime('%x %X')
                    }
            }
                                )
        if result.modified_count == 1:

            #print('------------')
            #print(ticket)
            #print('------------')
            return jsonify(catalog_item), 200

        return jsonify({ "error": "Process failed" }), 400


