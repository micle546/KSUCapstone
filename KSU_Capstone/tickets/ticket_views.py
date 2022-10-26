from datetime import datetime
from flask import Flask, render_template, session, redirect
from functools import wraps
from .. import app
from .models import Ticket

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
@app.route('/tickets/', methods=['GET'])
@login_required
def get_tickets():
    return render_template('tickets.html', title='View Tickets', ticket_list=get_tickets_list(), year=datetime.now().year)

@app.route('/tickets/create/', methods=['GET'])
@login_required
def get_ticket_create():
    return render_template('create_ticket.html', title='Create Ticket', year=datetime.now().year, time_now=datetime.now().strftime('%x %X'))

@app.route('/tickets/create/', methods=['POST'])
@login_required
def post_ticket_create():
    return Ticket().create_ticket()

@app.route('/tickets/view/', methods=['GET'])
@login_required
def get_tickets_list():
    return Ticket.fetch_tickets()

@app.route('/tickets/view/<id>', methods=['GET'])
@login_required
def get_ticket_by_id(id):
    return Ticket.fetch_ticket(id)

@app.route('/tickets/edit/', methods=['POST'])
@login_required
def post_ticket_edit():
    return Ticket().edit_ticket()