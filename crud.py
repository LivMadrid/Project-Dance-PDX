"""CRUD operations."""

from model import db, User, GroupDance, DanceEvent, connect_to_db
import datetime

def create_user(username, user_fname, user_lname, email, password, user_bio, user_city, user_zipcode, user_events):
    """Create and return a new user. """
    # user_profile_photo
    user = User(username=username,
                user_fname=user_fname,
                user_lname=user_lname,
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

def create_group_dance(group_dance_name, group_dance_types):
    """Create and return a new group dance"""

    group_dance = GroupDance(group_dance_name=group_dance_name, group_dance_types=group_dance_types)

    db.session.add(group_dance)
    db.session.commit()

    return group_dance

def create_dance_event(dance_event_name, dance_event_city, dance_event_zipcode, dance_event_description, dance_event_date, dance_event_time, dance_event_reoccuring):
    """Create and return a dance event"""
    #dance_event_photo

    dance_event = DanceEvent(dance_event_name=dance_event_name,
                            dance_event_city=dance_event_city,
                            dance_event_zipcode=dance_event_zipcode, 
                            dance_event_description=dance_event_description, 
                            dance_event_date=dance_event_date, 
                            dance_event_time=dance_event_time, 
                            dance_event_reoccuring=dance_event_reoccuring)
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


# def test_tables():
#     test_user= create_user('test-username', 'test-fname', 'test-lname', 'test@test.test','test bio', '11111', 'test user events')
#     test_group_dance = create_group_dance('test group name', 'test group type')
#     test_dance_event = create_dance_event('test event', 'test city', '11111', 'test descript', '2/11/2021', '1', 'test yes', '1', '1')


    



if __name__ == '__main__':
    from server import app
    connect_to_db(app)