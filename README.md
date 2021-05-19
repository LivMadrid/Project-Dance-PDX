
# Project-DANCE PDX


DANCE PDX is a social network application designed for dancers to connect with their greater dancing community in Portland, Oregon. 
Users sign-up for an account and are then able to create a profile, create new events, join groups, and display
their events dynamically on Google Maps. 
 
 ## Created with:
 Backend: Python3, Flask, SQLAlchemy, JSON
 Frontend: HTML5, CSS3, Bootstrap, Jinja, Javascript
 Database: PostgreSQL
 API: Google Maps Geocode API, Google Maps Javascript API

## Installation:

Clone repository:
$ git clone https://github.com/LivMadrid/Project-Dance-PDX.git

Create and activate virtual environment 
Windows 
$vitrualenv env --always copy 
$source env/bin/activate 
Mac
$virtualenv env
$source env/bin/activate

Install Requirements:
(env) pip3 install -r requirments.txt

Create Database
(env)$ createdb dance_events

Seed data base:
(env) $ python3 seed_database.py

Initiate Server:
(env)$ python3 server.py 

Now enter in http://localhost:5000/ to your browser and start dancing!

## Video Demo:
https://youtu.be/3kmkk9leq2U

## Version 2.0

User Capabilities:
 -Chat/Messaging
 -Going/Interested buttons
 -Partner look-up/user search
 -More Dance Groups Available 
 
Calendar:
-Implement calendar API to display all events/reoccuring events

Technologies:
-Implement more AJAX and possibly add React to freshen up the front-end 
- Add Google Maps Directions API so users could just use website to find location and driections to events 


## About the developer:

Olivia hails from multi-faceted background. Since Olivia was a child she was interested in people, art, dancing, and languages. 
After studying, living, and working abroad in Italy, Turkey, and Hungary she became fluent in Italian and versed in Turkish and Hungarian. 
She became interested in software engineering after learning about the Python language and all the creative ways to implement it. 
Searching for a career in which she could be creative, solve problems, help people, and utilize her language skills she found her path in software engineering. 
Olivia is interested in the intersection of Tech and women’s health, creativity, and languages and how she can be part of a team to make things more efficient
and better for the world.

Contact the developer at:
liv.madrid14@gmail.com or on linkedin: https://www.linkedin.com/in/olivia-boynton/
