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

@app.route('/log_in')
def log_in():
    """Login to app""" 
    # username, password
    # username = request.form.get['username']
    # email =  request.form.get['email']
    # password = request.form.get['password']
    return render_template('log_in.html')

#, methods=['POST']
#GET OR POST ? How to do it so it is unique username unique password --- if is good to go pass to user profile page other wise 
#if not a memeber then redirects to sign-up page... 
    # if password == '':  
    #     session['current_user'] = username
    #     flash(f'Logged in as {username}')
    #     return redirect('/user_profile')

    # else:
    #     flash('Wrong password!')
    #     return redirect('/login')




    return redirect('/user_profile.html')


@app.route('/sign_up')
def sign_up():
    """ User sign up """
    
    # user = crud.get_user_by_email(email)
    # if user:
    #     flash('Cannot create an account with that email. Try again.')
        
    # else:
    #     crud.create_user(email, password)
    #     flash('Account created! Please log in.')
    # return redirect('/log_in')

    # return render_template('user_profile.html')
    return render_template('sign_up.html')

@app.route('/user_profile')
def profile():
        """User Profile Page"""
        user = request.args.get('username')
# need this for all info but need to look into jquery/ajax for html

        return render_template('/user_profile', dancer=user)

# @app.route('/calendar_map')
# def calendar_map():
#need to make calendar and get google maps API done 
# @app.route('/all_events') this --
# def all_events():
#     """Display all events (list)"""
# event = crud.return_all_dance_events


# @app.route('/add_event')
# def create_dance_event():
# this html page is started - need to add js/ajax/jquery 




# # @app.route('/users')
# # def all_users():
# #     """Display All Users"""
# #     user = crud.return_all_users

# #     return render_template('all_users.html', users=users)

# @app.route('/group_dances_page')
# def group_dance_page():

# @app.route('/add_group_dance')
# def create_group_dance():

#app integration test
# def test_index(self):
#     client = server.app.test_client()
#     result= client.get('/')
#     self.assertIn('b<h1>Form</h1>, result.data')






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)