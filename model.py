"""Models and database functions for Track Side Stats project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class User(db.Model):
    """A User of the Track Side Stats that enters the data."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50), nullable=True)
    lname = db.Column(db.String(50), nullable=True)
    uname = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    permission_lvl = db.Column(db.String(50), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'),
                        nullable=True)

    team = db.relationship('Team', backref='users')
    league = db.relationship('League', 
                            secondary='leagueusers',
                            backref='users')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User id=%s name=%s email=%s>" % (self.user_id, 
                                                 self.name, self.email)


class LeagueUser(db.Model):
    """A joiner table between User and League."""

    __tablename__ = "leagueusers"
    
    leause_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('leagues.league_id'), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<LeagueUser id=%s permission_lvl=%s>" % (self.leause_id, users.permission_lvl)


class Team(db.Model):
    """The Team class."""

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    t_type = db.Column(db.String(100), nullable=False)
    founded = db.Column(db.Date, nullable=True)
    disbanded = db.Column(db.Date, nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey('leagues.league_id'), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Team id=%s name=%s t_type=%s>" % (self.team_id, 
            self.name, self.t_type)


class Player(db.Model):
    """The Player class."""

    __tablename__ = "players"

    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    legal_fname = db.Column(db.String(50), nullable=True)
    legal_lname = db.Column(db.String(50), nullable=True)
    number = db.Column(db.String(4), nullable=False)
    started = db.Column(db.Date, nullable=True)
    retired = db.Column(db.Date, nullable=True)

    jams = db.relationship('JamPosition', backref='players')
    teams = db.relationship('Team',
                            secondary='teamplayers',
                            backref='players')
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Player id=%s name=%s number=%s>" % (self.player_id, 
            self.name, self.number)


class TeamPlayer(db.Model):
    """A joiner table between Player and Team."""

    __tablename__ = "teamplayers"
    
    teapla_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<TeamPlayer id=%s team_id=%s player_id=%s>" % (self.teapla_id, 
            self.team_id, self.player_id)


class League(db.Model):
    """The League class."""

    __tablename__ = "leagues"

    league_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    affiliation = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Date, nullable=True)
    disbanded = db.Column(db.Date, nullable=True)

    teams = db.relationship('Team', backref='leagues')

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<League id=%s name=%s>" % (self.league_id, self.name)


class Roster(db.Model):
    """The Roster class."""

    __tablename__ = "rosters"

    roster_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    ordinal = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)

    teams = db.relationship('Team', backref='rosters')
    games = db.relationship('Game', backref='rosters')
    players = db.relationship('Player',
                              secondary='rosterplayers',
                              backref='rosters')
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Roster id=%s color=%s>" % (self.roster_id, self.color)


class RosterPlayer(db.Model):
    """A joiner table between Roster and Player."""

    __tablename__ = "rosterplayers"
    
    rospla_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roster_id = db.Column(db.Integer, db.ForeignKey('rosters.roster_id'), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<RosterPlayer id=%s player_name=%s roster_id=%s >" % (self.rospla_id, 
            players.name, rosters.roster_id)


class Game(db.Model):
    """The Game class."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    location = db.Column(db.String(100), nullable=False)
    event_name = db.Column(db.String(100), nullable=True)
    g_type = db.Column(db.String(100), nullable=False)
    floor = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Game id=%s date=%s, location=%s>" % (self.game_id, 
            self.date, self.location)


class Jam(db.Model):
    """The Jam class."""

    __tablename__ = "jams"

    jam_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    period = db.Column(db.Integer, nullable=False)
    j_start = db.Column(db.DateTime, default=datetime.utcnow(), nullable=True)
    j_end = db.Column(db.DateTime, nullable=True)
    end_type = db.Column(db.String(20), nullable=True)
    number = db.Column(db.Integer, nullable=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    timeout_type = db.Column(db.String(25), nullable=True)
    t_start = db.Column(db.DateTime, nullable=True)
    t_end = db.Column(db.DateTime, nullable=True)

    game = db.relationship('Game', backref='jams')
    players = db.relationship('JamPosition', backref='jams')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Jam id=%s period=%s, jam number=%s>" % (self.jam_id, 
            self.period, self.number)    


class JamPosition(db.Model):
    """An Association Object table between Player and Jam.
    http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many
    """

    __tablename__ = "jampositions"
    
    jampos_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    jam_id = db.Column(db.Integer, db.ForeignKey('jams.jam_id'), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<JamPosition id=%s position=%s jam_info=%s>" % (
            self.jampos_id, self.position, self.jam_id)


class Action(db.Model):
    """An Association Object table between jams and players."""

    __tablename__ = "actions"

    action_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    jam_id = db.Column(db.Integer, db.ForeignKey('jams.jam_id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    play = db.Column(db.String(20), nullable=False)
    points = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    jams = db.relationship('Jam', backref='actions')
    players = db.relationship('Player', backref='actions')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Action id=%s player_name=%s, play=%s>" % (self.action_id, 
            players.name, self.play)    


# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/trackstats'
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