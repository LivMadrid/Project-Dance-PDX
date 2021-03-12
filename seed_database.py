"""Populate data automatically with Python""" 
import os
import json
from random import choice, randint
from datetime import date

import crud
from model import User, GroupDance, DanceEvent, db, connect_to_db
import server

os.system('dropdb dance_events' )
os.system('createdb dance_events')

connect_to_db(server.app)
db.create_all()



def seed_users():

    user1 = User(username='Max1', user_fname='Max', user_lname='Fernet', email='max@max.com', password='123', user_bio='Max loves all dancing especially Salsa!', user_city ='Portland', user_zipcode= '97201',  user_events ='Salsa Nights')
    user2 = User(username='Luigi2', user_fname='Luigi', user_lname='Montemurra', email='gigi@gigi.com', password='abc', user_bio='Gigi dances Salsa and Tango', user_city ='Portland', user_zipcode ='97222', user_events ='Salsa Nights, Milonga Canaro')
    user3 = User(username='Jelli', user_fname='Angelica', user_lname='Perisco', email='jellybean@jelli.com', password='1234', user_bio='Angelica loves to dance Salsa, Swing, and Blues', user_city ='Vancouver', user_zipcode= '98683', user_events ='Salsa Nights, SwingLoft, Blues Boogie')
    user4 = User(username='Bengiii', user_fname='Bengi', user_lname='Beyaz', email='bengibeats@bengi.com', password='5678', user_bio='Bengi grooves to Hip Hop, Swing, and Blues', user_city ='Portland', user_zipcode= '97266',user_events ='QuestLove Hip Hop, SwingLoft, Blues PDX')
    user5 = User(username='CutieRutie', user_fname='Rutabega', user_lname='Gardner', email='qtrutie@rutie.com', password='54321',  user_bio='Rutie is new to dancing Swing, but loves to Applejack', user_city ='Portland',user_zipcode= '97217', user_events ='SwingLoft, LindyTime')
    user6 = User(username='Shandi', user_fname='Shandor', user_lname='Lokacs', email='shandorl@shandorl.com', password='321', user_bio='Shandor just moved from Budapest. He enjoys Tango, Blues, and Salsa', user_city ='Portland', user_zipcode='97218', user_events ='Milonga Canaro, Milonga Sentimental, Salsa Nights, Blues PDX')
    user7 = User(username='Bahar82', user_fname='Bahar', user_lname='Deniz', email='bahar82@bahar.com', password='987', user_bio='Bahar gets down to Hip Hop beats and soulful Blues', user_city ='Portland', user_zipcode='97201',user_events ='QuestLove Hip Hop, Blues PDX, Blues Boogie')
    user8 = User(username='JRome', user_fname='Jerome', user_lname='Cooper', email='jcooper@cooper.com', password='1010',  user_bio='Jerome is a seasoned dancer (10 yrs) in Blues and Swing', user_city ='Oregon City', user_zipcode='97045', user_events ='SwingLoft, LindyTime, Blues Boogie, Blues PDX')
    user9 = User(username='Giu90', user_fname='Giulia', user_lname='Gigli', email='giu90@giulia.com', password='1111', user_bio='Giulia dances Tango and Salsa in Sardegna and PDX', user_city ='Portland', user_zipcode='97222', user_events ='Milonga Canaro, Milonga Sentimental, Salsa Nights')
    user10 = User(username='Titus', user_fname='Titus', user_lname='Castana', email='titusc@titus.com', password='1212', user_bio='Titus is a Milonguero solomente!', user_city ='Portland', user_zipcode='97232', user_events ='Milonga Canaro, Milonga Sentimental, Milonga Noches Azul') 

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)

    db.session.commit()

    # crud.create_user(username, user_fname, user_lname, email, password, user_bio, user_city, user_zipcode, user_events)

# username, user_fname, user_lname, email, password, user_bio, user_location, user_events


# def seed_group_dances():

#     group1 = GroupDance(group_dance_name='Portland Salsa y Bachata Dancers', group_dance_types='Salsa')
#     group2 = GroupDance(group_dance_name='Portland Hoppers', group_dance_types='Swing')
#     group3 = GroupDance(group_dance_name='PDX Hip Hop', group_dance_types='Hip Hop')
#     group4 = GroupDance(group_dance_name='Blues Dancers PDX', group_dance_types='Blues')
#     group5 = GroupDance(group_dance_name='Milongueros PDX', group_dance_types='Tango')

#     db.session.add(group1)
#     db.session.add(group2)
#     db.session.add(group3)
#     db.session.add(group4)
#     db.session.add(group5)

#     db.session.commit()

#     # crud.create_group_dance(group_dance_name, group_dance_types)

# def seed_events(): 

#     # group = group_dance_id 
    
#     # event = DanceEvent( name group_dance_id=group.id)



#     # event1 = (dance_event_name, dance_event_city, dance_event_zipcode,  dance_event_description, dance_event_date, dance_event_time, dance_event_reoccuring=, dance_event_photo
#     # Salsa Nights SwingLoft Blues Boogie Blues PDX LindyTime Milonga Canaro Milonga Sentimental Milonga Noches Azul QuestLove Hip Hop
#     event1 = DanceEvent(dance_event_name='Salsa Nights', dance_event_city='Portland', dance_event_zipcode='97201', dance_event_description='Salsa y Bachata! Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8-11:30! Come enjoy with us', dance_event_date='2/28/2021', dance_event_time='7', dance_event_reoccuring='Yes' )
#     event2 =  DanceEvent(dance_event_name='SwingLoft', dance_event_city='Portland', dance_event_zipcode='97217', dance_event_description='East Coast Swing! Beginner class starts at 6pm. Intermediate at 7:00. Social Dancing from 8-11:30! Come dance till you drop!', dance_event_date='3/8/2021', dance_event_time='6', dance_event_reoccuring='Yes' )
#     event3 =  DanceEvent(dance_event_name='LindyTime', dance_event_city='Portland', dance_event_zipcode='97201', dance_event_description='LindyHop weekly classes! Beginner class 2pm-3pm. Intermediate at 3:15-5pm. Practice, Practice, Practice!', dance_event_date='3/7/2021', dance_event_time='2', dance_event_reoccuring='Yes' )
#     event4 = DanceEvent(dance_event_name='Blues Boogie', dance_event_city='Portland', dance_event_zipcode='97045', dance_event_description='Blues Social! Every first Saturday of the Month. Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8pm-1am!', dance_event_date='3/6/2021', dance_event_time='7', dance_event_reoccuring='Yes' )
#     event5 = DanceEvent(dance_event_name='Blues PDX', dance_event_city='Portland', dance_event_zipcode='97201', dance_event_description='Blues Lessons/Practica! Every Tuesday night. Beginner class starts at 5pm. Intermediate at 6:00. Practice Dancing from 7-8:30', dance_event_date='3/9/2021', dance_event_time='5', dance_event_reoccuring='Yes' )
#     event6 = DanceEvent(dance_event_name='Milonga Noches Azul', dance_event_city='Portland', dance_event_zipcode='97232', dance_event_description='Monthly Milonga Every Fourth Satuday. Quick Review class at 8. Milonga 8:30pm-2am - refreshments provided. Dress to impress', dance_event_date='3/27/2021', dance_event_time='8', dance_event_reoccuring='Yes' )
#     event7 = DanceEvent(dance_event_name='Milonga Canaro', dance_event_city='Portland', dance_event_zipcode='97222', dance_event_description='Biweekly Friday Night Milonga. Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8pm-1am!', dance_event_date='3/5/2021', dance_event_time='7', dance_event_reoccuring='Yes' )
#     event8 = DanceEvent(dance_event_name='Milonga Sentimental', dance_event_city='Portland', dance_event_zipcode='97218', dance_event_description=' 2nd Saturday Milonga. No classes. Tango Nuevo and Milonguero Tandas! Bring a snack to share! Social Dancing from 8pm-2am!', dance_event_date='3/13/2021', dance_event_time='8', dance_event_reoccuring='Yes' )
#     event9 = DanceEvent(dance_event_name='QuestLove Hip Hop', dance_event_city='Portland', dance_event_zipcode='97266', dance_event_description='Weekly classes every Tuesday and Thursday 7pm Sharp! Bring a water bottle and comfortable clothes ', dance_event_date=None , dance_event_time='7', dance_event_reoccuring='Yes' )
#     event10 = DanceEvent(dance_event_name='Hip Hop Duels', dance_event_city='Portland', dance_event_zipcode='97266', dance_event_description='Come show off your moves in a duel competition! 8pm March 20th! RSVP ', dance_event_date='3/13/2021', dance_event_time='8', dance_event_reoccuring='No' )

#     db.session.add(event1)
#     db.session.add(event2)
#     db.session.add(event3)
#     db.session.add(event4)
#     db.session.add(event5)
#     db.session.add(event6)
#     db.session.add(event7)
#     db.session.add(event8)
#     db.session.add(event9)
#     db.session.add(event10)

#     db.session.commit()

# #     # crud.create_dance_event(dance_event_name, dance_event_city, dance_event_zipcode, dance_event_description, dance_event_date, dance_event_time, dance_event_reoccuring)



def create_record(record):
    db.session.add(record)
    db.session.commit()



def seed_groups_with_events():

    salsa_group = GroupDance(group_dance_name='Portland Salsa y Bachata Dancers', group_dance_types='Salsa')
    create_record(salsa_group)

    salsa_event = DanceEvent(group_dance_id = salsa_group.group_dance_id, dance_event_name='Salsa Nights',  dance_event_location='7000 NE Airport Way, Portland, OR 97218', dance_event_description='Salsa y Bachata! Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8-11:30! Come enjoy with us', dance_event_date='2/28/2021', dance_event_reoccuring='Yes')
    create_record(salsa_event)

    swing_group = GroupDance(group_dance_name= 'Swing PDX ', group_dance_types= 'Swing')
    create_record(swing_group)

    swing_event = DanceEvent(group_dance_id = swing_group.group_dance_id, dance_event_name='SwingLoft', dance_event_location = '325 NW 13th Ave, Portland, OR 97209',  dance_event_description='East Coast Swing! Beginner class starts at 6pm. Intermediate at 7:00. Social Dancing from 8-11:30! Come dance till you drop!', dance_event_date='3/8/2021', dance_event_reoccuring='Yes' )
    create_record(swing_event)

    swing_event = DanceEvent(group_dance_id = swing_group.group_dance_id, dance_event_name='LindyTime',  dance_event_location ='539 NW 13th Ave, Portland, OR 97209', dance_event_description='LindyHop weekly classes! Beginner class 2pm-3pm. Intermediate at 3:15-5pm. Practice, Practice, Practice!', dance_event_date='3/7/2021',  dance_event_reoccuring='Yes' )
    create_record(swing_event)

    blues_group = GroupDance(group_dance_name= 'Blues Dancers of PDX ', group_dance_types= 'Blues')
    create_record(blues_group)

    blues_event = DanceEvent(group_dance_id = blues_group.group_dance_id, dance_event_name='Blues Boogie', dance_event_location ='1725 NE Alberta St, Portland, OR 97211', dance_event_description='Blues Social! Every first Saturday of the Month. Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8pm-1am!', dance_event_date='3/6/2021',  dance_event_reoccuring='Yes' )
    create_record(blues_event)

    blues_event = DanceEvent(group_dance_id = blues_group.group_dance_id, dance_event_name= 'Blues PDX', dance_event_location = '611 SW Kingston Ave, Portland, OR 97205', dance_event_description='Blues Lessons/Practica! Every Tuesday night. Beginner class starts at 5pm. Intermediate at 6:00. Practice Dancing from 7-8:30', dance_event_date='3/9/2021', dance_event_reoccuring='Yes' )
    create_record(blues_event)

    tango_group = GroupDance(group_dance_name= 'Milongueros PDX', group_dance_types= 'Tango')
    create_record(tango_group)

    tango_event = DanceEvent(group_dance_id = tango_group.group_dance_id, dance_event_name='Milonga Noches Azul', dance_event_location ='1300 SE Stark St #203, Portland, OR 97214', dance_event_description='Monthly Milonga Every Fourth Satuday. Quick Review class at 8. Milonga 8:30pm-2am - refreshments provided. Dress to impress', dance_event_date='3/27/2021', dance_event_reoccuring='Yes' )
    create_record(tango_event)

    tango_event = DanceEvent(group_dance_id = tango_group.group_dance_id, dance_event_name='Milonga Canaro', dance_event_location = '21 NE 12th Ave, Portland, OR 97232', dance_event_description='Biweekly Friday Night Milonga. Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8pm-1am!', dance_event_date='3/5/2021', dance_event_reoccuring='Yes' )
    create_record(tango_event)

    tango_event = DanceEvent(group_dance_id = tango_group.group_dance_id, dance_event_name='Milonga Sentimental', dance_event_location ='6305 SE Foster Rd, Portland, OR 97206', dance_event_description=' 2nd Saturday Milonga. No classes. Tango Nuevo and Milonguero Tandas! Bring a snack to share! Social Dancing from 8pm-2am!', dance_event_date='3/13/2021', dance_event_reoccuring='Yes' )
    create_record(tango_event)

    hiphop_group = GroupDance(group_dance_name= 'PDX Hip Hop ', group_dance_types= 'Hip Hop')
    create_record(hiphop_group)
     
    hiphop_event = DanceEvent(group_dance_id = hiphop_group.group_dance_id, dance_event_name= 'QuestLove Hip Hop', dance_event_location = 'S Gibbs St, Portland, OR 97239', dance_event_description='Weekly classes every Tuesday and Thursday 7pm Sharp! Bring a water bottle and comfortable clothes ', dance_event_date=None , dance_event_reoccuring='Yes' )
    create_record(hiphop_event)

    hiphop_event = DanceEvent(group_dance_id = hiphop_group.group_dance_id, dance_event_name='Hip Hop Duels', dance_event_location = '1510 SE 9th Ave, Portland, OR 97214', dance_event_description='Come show off your moves in a duel competition! 8pm March 20th! RSVP ', dance_event_date='3/13/2021', dance_event_reoccuring='No' )
    create_record(hiphop_event)






seed_users()
# seed_group_dances()
# seed_events()

seed_groups_with_events()