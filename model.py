"""Models for dance communites in any location"""

from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """ A user """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    user_fname = db.Column(db.String, nullable=False)
    user_lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=False)
    user_bio = db.Column(db.Text, nullable=False)
    user_location = db.Column(db.String, nullable=False)
    user_events = db.Column(db.String, nullable=False)
    # user_profile_photo = db.Column()
    # group_dance_id = db.Column(db.Integer, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    # group_dance_name = db.Column(db.String, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    
    # dance_group = db.relationship('DanceGroup'), backref (this goes dancegroup class right ? backref 'dance_groups')
    


    def __repr__(self):
        """Show user info"""
        return f'<User user_id={self.user_id} username={self.username} user_fname={self.user_fname} user_lname={self.user_lname}\
        email={self.email} user_bio={self.user_bio} user_location={self.user_location} user_events={self.user_events}>'

# user_profile_photo={self.user_profile_photo}>'



class GroupDance(db.Model):
    """A dance group"""

    __tablename__ = 'group_dances'

    group_dance_id = db.Column(db.Integer,
                        autoincrement=True, 
                        primary_key=True)
    group_dance_name = db.Column(db.String)
    group_dance_types = db.Column(db.String)
    # username = db.Column(db.String, db.ForeignKey('users.username')
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    #user_id references to table group_dances as it is the foreign key

    user = db.relationship('User', backref='group_dances')

    
    def __repr__(self):
        return f'<GroupDance group_dance_id={self.group_dance_id} group_dance_name={self.group_dance_name}\
        group_dance_types={self.group_dance_types}>'

    
class DanceEvent(db.Model):
    """ A dance event"""
    
    __tablename__= 'dance_events'

    dance_event_id = db.Column(db.Integer,
                        autoincrement=True, 
                        primary_key=True)
    dance_event_name = db.Column(db.String)
    dance_event_location = db.Column(db.String)
    dance_event_description = db.Column(db.String)
    dance_event_date = db.Column(db.DateTime)
    dance_event_time = db.Column(db.Integer)
    dance_event_reoccuring = db.Column(db.String)
    # dance_event_photo = 
    group_dance_id = db.Column(db.Integer, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    # group_dance_name = db.Column(db.String, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    # username = db.Column(db.String, db.ForeignKey('users.username')
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id') )
    # (WHY IS USER_ID HIGHLIGHTED BLUE ???? )

     
    user = db.relationship('User', backref='dance_events')

 
    def __repr__(self):
        return f'<DanceEvent dance_event_id={self.dance_event_id} dance_event_name={self.dance_event_name}\
        dance_event_location={self.dance_event_location} dance_event_description={self.dance_event_description}\
        dance_event_date={self.dance_event_date} dance_event_time={self.dance_event_time}\
        dance_event_reoccuring={self.dance_event_reoccuring} dance_event_photo={self.dance_event_photo}>'








def connect_to_db(flask_app, db_uri='postgresql:///dance_events', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
