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

# #loads data from dance.json file
# with open('data/dance.json') as f:
#     dance_data = json.loads(f.read())


def seed_users:
    user1 = User('Max1', 'Max', 'Fernet', 'max@max.com', '123', 'Max loves all dancing especially Salsa!', 'Portland, OR', 'Salsa Nights')
    user2 = User('Luigi2', 'Luigi', 'Montemurra', 'gigi@gigi.com', 'Gigi dances Salsa and Tango', 'Mollala, OR', 'Salsa Nights, Milonga Canaro')
    user3 = User('Jelli', 'Angelica', 'Perisco', 'jellybean@jelli.com', 'Angelica loves to dance Salsa, Swing, and Blues', 'Vancouver, OR', 'Salsa Nights, SwingLoft, Blues Boogie')
    user4 = User('Bengiii', 'Bengi', 'Beyaz', 'bengibeats@bengi.com', 'Bengi grooves to Hip Hop, Swing, and Blues', 'Portland, OR', 'QuestLove Hip Hop, SwingLoft, Blues PDX')
    user5 = User('CutieRutie', 'Rutabega', 'Gardner', 'qtrutie@rutie.com', 'Rutie is new to dancing Swing, but loves to Applejack', 'Oregon City, Oregon', 'SwingLoft, LindyTime')
    user6 = User('Shandi', 'Shandor', 'Lokacs', 'shandorl@shandorl.com', 'Shandor just moved from Budapest. He enjoys Tango, Blues, and Salsa', 'Portland, OR', 'Milonga Canaro, Milonga Sentimental, Salsa Nights, Blues PDX')
    user7 = User('Bahar82', 'Bahar', 'Deniz', 'bahar82@bahar.com', 'Bahar gets down to Hip Hop beats and soulful Blues', 'Mollala, OR', 'QuestLove Hip Hop, Blues PDX, Blues Boogie')
    user8 = User('JRome', 'Jerome', 'Cooper', 'jcooper@cooper.com', 'Jerome is a seasoned dancer (10 yrs) in Blues and Swing', 'Oregon City, OR', 'SwingLoft, LindyTime, Blues Boogie, Blues PDX')
    user9 = User('Giu90', 'Giulia', 'Gigli', 'giu90@giulia.com', 'Giulia dances Tango and Salsa in Sardegna and PDX', 'Portland, OR', 'Milonga Canaro, Milonga Sentimental, Salsa Nights')
    user10 = User('Titus', 'Titus', 'Castana', 'titusc@titus.com', 'Titus is a Milonguero solomente!', 'Portland, OR', 'Milonga Canaro, Milonga Sentimental, Milonga Noches Azul') 

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

# username, user_fname, user_lname, email, password, user_bio, user_location, user_events

def seed_events: 
    # event1 = (dance_event_name, dance_event_location, dance_event_description, dance_event_date, dance_event_time, dance_event_reoccuring, dance_event_photo

    event1
    event2
    event3
    event4
    event5
    event6
    event7
    event8
    event9
    event10  


# crud.create_username('liv')   ??????

for n in range(15):

    email = f'user{n}@test.com' #unique email using nums
    password = 'randompass' #hardcoded as default  #NOT unique 
#create 10 random users and ratings 
    user = crud.create_user(email, password)

    for x in range(10): 
        random_movie = choice(movies_in_db)
        # random_rating = randint(5) wrong but tried to get score 
        score = randint(1,5)

    crud.create_rating(user, random_movie, score)