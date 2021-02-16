"""Populate data automatically with Python""" 
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()



def seed_users():
    user1 = User('Max1', 'Max', 'Fernet', 'max@max.com', '123', 'Max loves all dancing especially Salsa!', 'Portland', '97201' 'Salsa Nights')
    user2 = User('Luigi2', 'Luigi', 'Montemurra', 'gigi@gigi.com', 'abc', 'Gigi dances Salsa and Tango', 'Portland', '97222','Salsa Nights, Milonga Canaro')
    user3 = User('Jelli', 'Angelica', 'Perisco', 'jellybean@jelli.com', '1234', 'Angelica loves to dance Salsa, Swing, and Blues', 'Vancouver', '98683', 'Salsa Nights, SwingLoft, Blues Boogie')
    user4 = User('Bengiii', 'Bengi', 'Beyaz', 'bengibeats@bengi.com', '5678', 'Bengi grooves to Hip Hop, Swing, and Blues', 'Portland', '97266','QuestLove Hip Hop, SwingLoft, Blues PDX')
    user5 = User('CutieRutie', 'Rutabega', 'Gardner', 'qtrutie@rutie.com', '54321',  'Rutie is new to dancing Swing, but loves to Applejack', 'Portland','97217', 'SwingLoft, LindyTime')
    user6 = User('Shandi', 'Shandor', 'Lokacs', 'shandorl@shandorl.com', '321', 'Shandor just moved from Budapest. He enjoys Tango, Blues, and Salsa', 'Portland', '97218', 'Milonga Canaro, Milonga Sentimental, Salsa Nights, Blues PDX')
    user7 = User('Bahar82', 'Bahar', 'Deniz', 'bahar82@bahar.com', '987', 'Bahar gets down to Hip Hop beats and soulful Blues', 'Portland', '97201','QuestLove Hip Hop, Blues PDX, Blues Boogie')
    user8 = User('JRome', 'Jerome', 'Cooper', 'jcooper@cooper.com', '1010',  'Jerome is a seasoned dancer (10 yrs) in Blues and Swing', 'Oregon City', '97045', 'SwingLoft, LindyTime, Blues Boogie, Blues PDX')
    user9 = User('Giu90', 'Giulia', 'Gigli', 'giu90@giulia.com', '1111', 'Giulia dances Tango and Salsa in Sardegna and PDX', 'Portland', '97222', 'Milonga Canaro, Milonga Sentimental, Salsa Nights')
    user10 = User('Titus', 'Titus', 'Castana', 'titusc@titus.com', '1212', 'Titus is a Milonguero solomente!', 'Portland', '97232','Milonga Canaro, Milonga Sentimental, Milonga Noches Azul') 

    db.add(user1)
    db.add(user2)
    db.add(user3)
    db.add(user4)
    db.add(user5)
    db.add(user6)
    db.add(user7)
    db.add(user8)
    db.add(user9)
    db.add(user10)

    db.commit()

    crud.create_user(username, user_fname, user_lname, email, password, user_bio, user_city, user_zipcode, user_events)

# username, user_fname, user_lname, email, password, user_bio, user_location, user_events


def seed_group_dances():

    group1 = ('Portland Salsa y Bachata Dancers', 'Salsa, Bachata')
    group2 = ('Portland Hoppers', 'East-Coast Swing, Lindy Hop')
    group3 = ('PDX Hip Hop', 'Hip Hop')
    group4 = ('Blues Dancers PDX', 'Blues')
    group5 = ('Milongueros PDX', 'Tango, Milonga, Tango Nuevo')

    db.add(group1)
    db.add(group2)
    db.add(group3)
    db.add(group4)
    db.add(group5)

    db.commit()

    crud.create_group_dance(group_dance_name, group_dance_types)

def seed_events(): 
    # event1 = (dance_event_name, dance_event_city, dance_event_zipcode,  dance_event_description, dance_event_date, dance_event_time, dance_event_reoccuring, dance_event_photo
    # Salsa Nights SwingLoft Blues Boogie Blues PDX LindyTime Milonga Canaro Milonga Sentimental Milonga Noches Azul QuestLove Hip Hop
    event1 = DanceEvent('Salsa Nights', 'Portland', '97201', 'Salsa y Bachata! Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8-11:30! Come enjoy with us', '2/28/2021', '7', 'Yes' )
    event2 =  DanceEvent('SwingLoft', 'Portland', '97217', 'East Coast Swing! Beginner class starts at 6pm. Intermediate at 7:00. Social Dancing from 8-11:30! Come dance till you drop!', '3/8/2021', '6', 'Yes' )
    event3 =  DanceEvent('LindyTime', 'Portland', '97201', 'LindyHop weekly classes! Beginner class 2pm-3pm. Intermediate at 3:15-5pm. Practice, Practice, Practice!', '3/7/2021', '2', 'Yes' )
    event4 = DanceEvent('Blues Boogie', 'Portland', '97045', 'Blues Social! Every first Saturday of the Month. Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8pm-1am!', '3/6/2021', '7', 'Yes' )
    event5 = DanceEvent('Blues PDX', 'Portland', '97201', 'Blues Lessons/Practica! Every Tuesday night. Beginner class starts at 5pm. Intermediate at 6:00. Practice Dancing from 7-8:30', '3/9/2021', '5', 'Yes' )
    event6 = DanceEvent('Milonga Noches Azul', 'Portland', '97232', 'Monthly Milonga Every Fourth Satuday. Quick Review class at 8. Milonga 8:30pm-2am - refreshments provided. Dress to impress', '3/27/2021', '8', 'Yes' )
    event7 = DanceEvent('Milonga Canaro', 'Portland', '97222', 'Biweekly Friday Night Milonga. Beginner class starts at 7pm. Intermediate at 7:30. Social Dancing from 8pm-1am!', '3/5/2021', '7', 'Yes' )
    event8 = DanceEvent('Milonga Sentimental', 'Portland', '97218', ' 2nd Saturday Milonga. No classes. Tango Nuevo and Milonguero Tandas! Bring a snack to share! Social Dancing from 8pm-2am!', '3/13/2021', '8', 'Yes' )
    event9 = DanceEvent('QuestLove Hip Hop', 'Portland', '97266', 'Weekly classes every Tuesday and Thursday 7pm Sharp! Bring a water bottle and comfortable clothes ', ' ', '7', 'Yes' )
    event10 = DanceEvent('Hip Hop Duels', 'Portland', '97266', 'Come show off your moves in a duel competition! 8pm March 20th! RSVP ', '3/13/2021', '8', 'No' )

    db.add(event1)
    db.add(event2)
    db.add(event3)
    db.add(event4)
    db.add(event5)
    db.add(event6)
    db.add(event7)
    db.add(event8)
    db.add(event9)
    db.add(event10)

    db.commit()

    crud.create_dance_event(dance_event_name, dance_event_city, dance_event_zipcode, dance_event_description, dance_event_date, dance_event_time, dance_event_reoccuring)



