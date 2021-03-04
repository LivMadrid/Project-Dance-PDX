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


#Displays homepage: A welcome statement and then two buttons for login/signup
@app.route('/')
def homepage():
    """Homepage"""
        
    return render_template('homepage.html')

#takes user to login form
@app.route('/login', methods=['POST'])
def get_login_info():
    """Get info from login form and return user profile"""

#gets requested info from form on login.html  using POST method
    username = request.form.get('username')

#-----------------------------------------------------------------------#
    print("#########################################")
    print(username)
#-----------------------------------------------------------------------#

    email =  request.form.get('email')
    password = request.form.get('password')

#-----------------------------------------------------------------------#
    print(email)
#-----------------------------------------------------------------------#
    session['user'] = username # make this a dictionary 
    print(session['user'])
#crud fucntion checks username against data base
    

    user = crud.return_user_profile(username)
    # send username to crud.check_user(name)
    # -> user = User.query.filter_by(username(<-- from model.py)=name(<- can be anything))
    # user.password <-- same name from model.py
    # user_profile_data = crud.return_user_profile(username)
    # #filter(User.username)
    # filter_by(username)
    groupuser = ' '
    groupnames = ' '
    # if request.methods == 'POST': #maybe redundant
    groups = []
    if user:
        flash('logged in as {username}')
        return render_template('user_profile.html', user= user, groups=groups, groupuser=groupuser, groupnames=groupnames)
    else:
        flash('incorrect password')
        return redirect('/login')


@app.route('/login')
def log_in():
    """Takes user to login page""" 
   
    return render_template('log_in.html')

#takes user from login in page -verifies email/pass and then either directs to user_profile or redirects to login form

#GET OR POST ? How to do it so it is unique username unique password --- if is good to go pass to user profile page other wise 
#if not a member then redirects to sign-up page... 
@app.route('/logout')
def logout():
    """User logs out of session"""
    
    
    return redirect('/')


 
@app.route('/sign_up')
def sign_up():
    """ Takes user to sign-up form page """

    return render_template('sign_up.html')

@app.route('/sign_up', methods=['POST'])
def get_sign_up_info():
    """ User sign up info verification"""
    
    username= request.form.get('username')
    print(username)
    fname = request.form.get('fname') # <--- name needs to be from HTML name
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    bio = request.form.get('bio')
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    events = request.form.get('events')

#     # user_groups = " " #user_groups=user_groups
#     user_groups = ' '
# user_groups=user_groups
    session['user'] = username # make this a dictionary 
    print(session['user'])
    existing_user = crud.return_user_profile(username) 
    # return True or False # True - if the user already exists
    print(username)

    if existing_user: #if True: if the user exists already
        flash(f'An account with that username already exists. Try again? Or Forgot Password?')
        return render_template('log_in.html')
    else:
        user = crud.create_user(username, fname, lname, email, password, bio, city, zipcode, events)
        flash('Account created! ')
        return render_template('user_profile.html', user=user)

@app.route('/user_profile')
def show_profile():
    """Display user profile page"""

 
    username = session['user']
    user = crud.return_user_profile(username)
    groupnames = crud.return_user_groups(user) 

    return render_template('user_profile.html', user=user, groupnames=groupnames)

@app.route('/user_profile', methods=['GET','POST'])
def profile():
    """User Profile Page"""
    
    
    username = session['user']
    user = crud.return_user_profile(username)
    print(user, '****************************************')
    # groups = request.form.getlist('name')
    # print(groups, '$$$$$$$$$$$$$$$$$$')
    # group_type = request.form.get('type')
    
   
    # if groups:
    #     print(groups)
    # #     print('Salsa')
    groupuser = ' '
    # user_groups = ' '
    if request.form.getlist('Salsa'):
        salsa = crud.get_group_id('Salsa')
        # print(salsa)
        #print(groups)
        salsa_id = salsa.group_dance_id #GROUP DANCE table 
        # print(salsa_id)
        userid = user.user_id
        # print(userid)
        groupuser = crud.creategroupuser(userid, salsa_id)

    
    if request.form.getlist('Swing'):
        swing = crud.get_group_id('Swing')

        print(swing)
        #print(groups)
        swing_id = swing.group_dance_id #GROUP DANCE table 

        print(swing_id)

        userid = user.user_id

        print(userid)
         
        groupuser = crud.creategroupuser(userid, swing_id)

   

    if request.form.getlist('Blues'):
        blues = crud.get_group_id('Blues')
        # print(blues)
        #print(groups)
        blues_id = blues.group_dance_id #GROUP DANCE table 
        # print(blues_id)
        userid = user.user_id
        # print(userid)
        groupuser = crud.creategroupuser(userid, blues_id) 
    
    

    if request.form.getlist('Tango'):
        tango = crud.get_group_id('Tango')
        # print(tango)
        #print(groups)
        tango_id = tango.group_dance_id #GROUP DANCE table 
        # print(tango_id)
        userid = user.user_id
        # print(userid)
        groupuser = crud.creategroupuser(userid, tango_id)

    

    if request.form.getlist('Hip Hop'):
        hiphop = crud.get_group_id('Hip Hop')
        # print(hiphop)
        #print(groups)
        hiphop_id = hiphop.group_dance_id #GROUP DANCE table 
        # print(hiphop_id)
        userid = user.user_id
        # print(userid)
        groupuser = crud.creategroupuser(userid, hiphop_id)

    
    groupnames = crud.return_user_groups(user) 

    # <group_id = 1 user_id = 1 event_id =1>
    
    # else:
    #     return f'You are not apart of any groups yet'
        # user_groups = crud.return_user_groups(groupuser) #user_groups=user_groups

    return render_template('user_profile.html', user=user, groupnames=groupnames)
    # groups = crud.get_user_groups(user.user_id)
    #crud if tango - get group by name crd. get group by name group id -groupname- Groupuser realtionship
    
     
   
    
    


# <option> drop down of dance groups on user profile page (query all groups)
#   user selects value (group) GET REQUEST 
#   request.get.args (value/group)from dropdown
#   in data model send user_id in session
#   group id after groupname CRUD creategroupuser(user_id,group_id)






    ##exisiting user 
    # if  session['user'] = username:
    # if session['user']:
    #     username =  session['current user']
    #     user = crud.get_user_by_username(username) # create this crud function
    # user = crud.get_user_by_email(email)
    # username = user.username
    # email = user.email
# return render_template('user-profile.hmtl', user=user)
### ---> HTML 
# <h1> Welcome {{ user.username }} </h1>

@app.route('/add_event')
def add_event():
    """Create Event Form"""

    return render_template('create_dance_event.html')


@app.route('/add_event', methods=['POST'])
def create_new_dance_event():
    """Get Event Creation info- Return event profile"""
# # this html page is started - need to add js/ajax/jquery 
    eventname = request.form.get('eventname')
    print('#########################################')
    print('eventname')
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    description = request.form.get('description')
    date = request.form.get('date')
    # time = request.form.get('time')
    reoccuring_event = request.form.get('reoccuringevent')
    
    session['event'] = eventname
    print(session['event'])
    event = crud.create_dance_event(eventname, city, zipcode, description, date,  reoccuring_event)

    if event: #if True: if the event exists already
        flash(f'An event with that name already exists. Try again? ')
        return render_template('event.html', event=event)
        #or better to redirect back to create event page if one already exists?
    else:
        event = crud.create_dance_event(eventname, city, zipcode, description, date, reoccuring_event)
        flash('Event created!')
        return render_template('event.html', event=event)


@app.route('/event_profile')
def return_event_profile():
    """Returns an event profile page"""

    #  eventname = session['event']

    event = crud.return_dance_event(eventname)


    return render_template('event.html', event=event)

@app.route('/all_events')
def all_events_return():
    """Returns all events"""
    

    
    # eventname = session['event']
    events = crud.return_all_dance_events()
    print("************************************************************")
    print(events)
    print('**************************************************************')

    if events:
        return render_template('all_events.html', events=events)
# evnets=events is creating a main agrument (left hand side) and giving it a value on the right side. 

@app.route('/add_group')
def add_group():
    """Create Group Form"""

    return render_template('create_group_dance.html')


@app.route('/add_group', methods=['POST'])
def create_group_dance():
    """Get group info from form and create group"""

    groupname = request.form.get('groupname')
    grouptype = request.form.get('grouptype')
    
    
    session['group'] = groupname
    print(session['group'])
    group = crud.create_group_dance(groupname, grouptype)

    if group: #if True: if the event exists already
        flash(f'A group with that name already exists. Try again? ')
        return render_template('group_dance_page.html', group=group)
        #or better to redirect back to create event page if one already exists?
    else:
       group = crud.create_group_dance(groupname, grouptype)
       flash('Group created!')
       return render_template('group_dance_page.html', group=group)


# @app.route('/group_profile')
# def group_profile():
#     """Returns Group Profile"""

#     return render_template('group_dance_page.html')

@app.route('/group_profile/<grouptype>')
def return_group_profile_page(grouptype):
    """Returns Group Profile"""

    # grouptype = request.args.get('type')
    # # # group = GroupDance.query.filter_by(group_dance_types=group_type).all()
    # group = crud.return_group_profile(grouptype)
    # # # all_users = crud.return_all_users_in_group(group)  all_users=all_users 
    # print(group)
    # all_users = crud.return_all_users_in_group()
    # grouptype = request.args.get('grouptype')
    group = crud.return_group_profile(grouptype)

    users = crud.return_all_users_in_group(group)
    
        
    return render_template('group_dance_page.html', group=group, users=users )

@app.route('/all_dance_groups')
def return_all_dance_group_types():
    """Display all groups"""

    group_type = request.args.get('type')

    groups = crud.return_all_group_types(group_type)


    if groups:
        
        return render_template('all_groups.html', groups=groups)

        #MAKE STHIS A POST REQUEST ???


# /FIX ME: Groups aren't being added to the database
# 1. new users should pick a group-type to be apart of
#       need to put a group field in the user table --> user can pick one group
#       <button>pick a group</button>      <button>pick an event</button> 
#        --> all events posted from                 --> all events render
#               that group
# 2. then events from that group-type will be displayed to them
# 3. Existing users: on their profile page: it should show: what groups they're apart of and what events those groups attend
















# # # @app.route('/users')
# # # def all_users():
# # #     """Display All Users"""
# # #     user = crud.return_all_users

# # #     return render_template('all_users.html', users=users)














#app integration test
# def test_index(self):
#     client = server.app.test_client()
#     result= client.get('/')
#     self.assertIn('b<h1>Form</h1>, result.data')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)