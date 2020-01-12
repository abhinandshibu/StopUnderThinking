from datetime import datetime
from app import db
from app import login_manager
from flask_login import UserMixin


# inherits the basic properties for managing logon from UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(), unique=True)
    password_hash = db.Column(db.String())
    salt = db.Column(db.String())
    journals = db.relationship('Journal', backref='User', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username, self.password_hash, self.salt)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_mod = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sections = db.relationship('Section', backref='Journal_Name', lazy=True)

    def __repr__(self):
        return '<Journal {}>'.format(self.user_id, self.name, self.id)


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_mod = db.Column(db.DateTime, default=datetime.utcnow)
    journal_id = db.Column(db.Integer, db.ForeignKey('journal.id'))
    entry = db.relationship('Entry', backref='Section_Name', lazy=True)


    def __repr__(self):
        return '<Journal {}>'.format(self.journal_id, self.name, self.id)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    content = db.Column(db.Text)
    last_mod = db.Column(db.DateTime, default=datetime.utcnow)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))

    def __repr__(self):
        return '<Journal {}>'.format(self.section_id, self.name, self.id)




