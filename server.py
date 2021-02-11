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

# @app.route('/')
# def homepage():
#         """Homepage/Login/SignUp Display"""
        
#         return render_template('homepage.html')

# @app.route('/users')

# #user profiles /sign-in 

# @app.route('/group_dances')


# @app.route('/dance_events')

# #link to calendars 




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)