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

#loads data from dance.json file
with open('data/dance.json') as f:
    dance_data = json.loads(f.read())



# crud.create_username('liv')   ??????