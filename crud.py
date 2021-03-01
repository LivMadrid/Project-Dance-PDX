"""CRUD operations."""

from model import db, User, GroupDance, DanceEvent, connect_to_db
import datetime

def create_user(username, user_fname, lname, email, password, user_bio, user_city, user_zipcode, user_events):
    """Create and return a new user. """
    # user_profile_photo
    user = User(username=username,
                user_fname=user_fname,
                user_lname=lname,
                email=email,
                password=password,
                user_bio=user_bio,
                user_city=user_city,
                user_zipcode=user_zipcode,
                user_events=user_events)
                # user_profile_photo=user_profile_photo)

    db.session.add(user)
    db.session.commit()

    return user 

def create_group_dance(groupname, grouptype):
    """Create and return a new group dance"""

    group_dance = GroupDance(group_dance_name=groupname, group_dance_types=grouptype)

    db.session.add(group_dance)
    db.session.commit()

    return group_dance

def create_dance_event(eventname, city, zipcode, description, date, reoccuring_event):
    """Create and return a dance event"""
    #dance_event_photo

    dance_event = DanceEvent(dance_event_name=eventname,
                            dance_event_city=city,
                            dance_event_zipcode=zipcode, 
                            dance_event_description=description, 
                            dance_event_date=date, 
                            # dance_event_time=time, 
                            dance_event_reoccuring=reoccuring_event)
                            # dance_event_photo=dance_event_photo)

    db.session.add(dance_event)
    db.session.commit()

    return dance_event

def return_all_users():
    """Returns all users"""

    all_users = User.query.all()
    return all_users


def return_all_dance_events():
    """Returns all events"""

    all_events = DanceEvent.query.all()
    return all_events
#change to limit ? so that only the nameand info shows not tableid number

# def return_group_profile(groupname):
#     """Returns group profile page """

#     group_profile = GroupDance.query.filter_by(group_dance_name=groupname).first()

#     return group_profile

def return_all_group_types(group_type):
    """Returns all groups"""
    all_group_types = GroupDance.query
    if group_type:
        all_group_types = all_group_types.filter_by(group_dance_types=group_type)
    return all_group_types

def return_user_profile(username):
    """Display user profile"""
    user = User.query.filter_by(username=username).first()

    return user

def get_user_groups(): 

    user_groups = DanceGroup.query.filter_by(user_id=userid)

    return user_groups

def return_dance_event(eventname):

    event = DanceEvent.query.filter_by(dance_event_name=eventname).first()

    return event

# def get_user_by_username(username): #user exists 
#     """Return a user by email."""
    
#     user = return_user_profile(username)
#     print(user)
#     # db_username = user.username
#     print("#######CRUD FUNCCTIOIIIOONNNN#############################")
#     #print("here in the crud function we have db_password which is: ", db_username)
#     if user:
#         return True # this person already exists - don't create another one
#     else:
#         return False

# redundant 

def check_user_login_email(email):
    """Checks to see if a user account exists using email"""
    
    db_email = User.query.get(User.email == email)
    return db_email

# def check_user_login_password(password):
#     """Verifies user account password"""

#     # db_password = User.query.get(User.password == password)
#     user  = User.query.get.all() # FIX ME --- how to get current user's /current session passwrod
#     db_password = user.password
#     print("#######CRUD FUNCCTIOIIIOONNNN#############################")
#     # print("here in the crud function we have db_password which is: ", db_password)
#     return db_password

# def test_tables():
# """TEST CODE FOR DATA BASE"""
#     test_user= create_user('test-username', 'test-fname', 'test-lname', 'test@test.test','test bio', '11111', 'test user events')
#     test_group_dance = create_group_dance('test group name', 'test group type')
#     test_dance_event = create_dance_event('test event', 'test city', '11111', 'test descript', '2/11/2021', '1', 'test yes', '1', '1')


    



if __name__ == '__main__':
    from server import app
    connect_to_db(app)