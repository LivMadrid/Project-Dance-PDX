"""Server for Dance Anywhere App"""

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db 
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = '123abc'
app.jinja_env.undefined = StrictUndefined


# #Routes here 
@app.route('/')
def homepage():
    """Homepage"""
        
    return render_template('homepage.html')

#takes user to login form or redirects to sign

@app.route('/log_in', )
def log_in():
    """Login to app""" 

    return render_template('log_in.html')

@app.route('/user_profile')
def profile():
        """User Profile Page"""
        user = request.args.get('username')


        return render_template('/user_profile', dancer=user)

# @app.route('/sign_up')
# def create_user():
#     """User sign up""" 


# @app.route('/calendar_map')
# def calendar_map():

# @app.route('/add_event')
# def create_dance_event():

# @app.route('/all_events')
# def all_events():
#     """Display all events (list)"""
# event = crud.return_all_dance_events


# # @app.route('/users')
# # def all_users():
# #     """Display All Users"""
# #     user = crud.return_all_users

# #     return render_template('all_users.html', users=users)

# @app.route('/group_dances_page')
# def group_dance_page():

# @app.route('/add_group_dance')
# def create_group_dance():






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)