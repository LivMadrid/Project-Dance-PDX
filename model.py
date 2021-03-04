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
    user_city = db.Column(db.String, nullable=False)
    user_zipcode = db.Column(db.Integer, nullable=False, unique=False)
    user_events = db.Column(db.String)
    # user_profile_photo = db.Column()
    # group_dance_id = db.Column(db.Integer, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    # group_dance_name = db.Column(db.String, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    
    # dance_group = db.relationship('DanceGroup'), backref (this goes dancegroup class right ? backref 'dance_groups')
    


    def __repr__(self):
        """Show user info"""
        return f'<User user_id={self.user_id} username={self.username} user_fname={self.user_fname} user_lname={self.user_lname}\
        email={self.email} user_bio={self.user_bio} user_city={self.user_city} user_zipcode={self.user_zipcode} user_events={self.user_events}>'

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

    #users = db.relationship('User', backref='group_dances')

    
    def __repr__(self):
        return f'<GroupDance group_dance_id={self.group_dance_id} group_dance_name={self.group_dance_name}\
        group_dance_types={self.group_dance_types}>'

class GroupUser(db.Model):

    __tablename__ = "groupusers"

    id = db.Column(db.Integer,
                        autoincrement=True, 
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    group_id = db.Column(db.Integer, db.ForeignKey('group_dances.group_dance_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('dance_events.dance_event_id'))

    users = db.relationship('User', backref='groupusers')
    groups = db.relationship('GroupDance', backref='groupusers')
    events = db.relationship('DanceEvent', backref='groupusers')

    # SalsaLiv = GroupUser(user_id=session['user'].user_id)
    
    def __repr__(self):
        return f'<Groupuser user_id={self.user_id} group_id={self.group_id} event_id={self.event_id}>' 
    
class DanceEvent(db.Model):
    """ A dance event"""
    
    __tablename__= 'dance_events'

    dance_event_id = db.Column(db.Integer,
                        autoincrement=True, 
                        primary_key=True)
    dance_event_name = db.Column(db.String)
    dance_event_city = db.Column(db.String)
    dance_event_zipcode = db.Column(db.Integer)
    dance_event_description = db.Column(db.String)
    dance_event_date = db.Column(db.DateTime)
    # dance_event_time = db.Column(db.Integer)
    dance_event_reoccuring = db.Column(db.String)
    # dance_event_photo = 
    group_dance_id = db.Column(db.Integer, db.ForeignKey('group_dances.group_dance_id'))
    # group_dance_name = db.Column(db.String, db.ForeignKey('group_dances.group_dance_id'), nullable=False)
    # username = db.Column(db.String, db.ForeignKey('users.username')
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id') )
    # (WHY IS USER_ID HIGHLIGHTED BLUE ???? )

     
    group = db.relationship('GroupDance', backref='dance_events')
    # from events --> DanceEvent.group = [<Group salsa>, <Group tango>] #all groups assc with event_id
    # from DanceEvent.group[0].user (user relationship from line 56) = [<User Liv>, <User Lucia>]
    # DanceEvent.group[0].user[0].user_fname = 'Liv'

    # Group.user => list of users in that group

    # salsa1 = Liv & Lucia
  
 
    def __repr__(self):
        return f'<DanceEvent dance_event_id={self.dance_event_id} dance_event_name={self.dance_event_name}\
        dance_event_city={self.dance_event_city} dance_event_zipcode={self.dance_event_zipcode} dance_event_description={self.dance_event_description}\
        dance_event_date={self.dance_event_date} \
        dance_event_reoccuring={self.dance_event_reoccuring} >'

# dance_event_time={self.dance_event_time}
# dance_event_photo={self.dance_event_photo





def connect_to_db(flask_app, db_uri='postgresql:///dance_events', echo=False):
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




# (username='test-username',user_fname='test-fname', user_lname='test-lname', email='test@test.test', password='test', user_bio = 'test user bio', user_zipcode = '97701', user_events = 'test-user-events')