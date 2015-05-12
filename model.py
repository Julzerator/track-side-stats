"""Models and database functions for Track Side Stats project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class User(db.Model):
    """A User of the Track Side Stats that enters the data."""

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, nullable=True)
    password = dbColumn(db.String(20), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User id=%s name=%s email=%s>" % (self.user_id, self.name, self.email)


class Team(db.Model):
    """The Team class."""

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Date, nullable=False)
    league_id = db.Column(db.Integer, nullable=True)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Team id=%s name=%s>" % (self.team_id, self.name)


class Player(db.Model):
    """The Player class."""

    __tablename__ = "players"

    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    legal_name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    started = db.Column(db.Date, nullable=False)
    retired = db.Column(db.Date, nullable=True)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Player id=%s name=%s>" % (self.player_id, self.name)


class Position(db.Model):
    """The Position class."""

    __tablename__ = "positions"

    position_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position_type = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Position id=%s name=%s type=%s>" % (self.position_id, self.name, 
            self.position_type)


class Roster(db.Model):
    """The Roster class."""

    __tablename__ = "rosters"

    roster_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_id = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Roster id=%s name=%s>" % (self.roster_id, self.team_id)

#### TODO

# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///derby.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
