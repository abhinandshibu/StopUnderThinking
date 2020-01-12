from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usernameEmail = StringField('UsernameEmail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    firstName = StringField('firstname', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password1 = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('Enter Again', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class NewJournal(FlaskForm):
    new_journal = StringField('new_journal', validators=[DataRequired()])
    submit = SubmitField('create new_journal')


class NewSection(FlaskForm):
    section_input = StringField('new_journal', validators=[DataRequired()])
    submit = SubmitField('create new_journal')


class NewEntry(FlaskForm):
    entry_input = StringField('new_journal', validators=[DataRequired()])
    submit = SubmitField('create new_journal')


class EntryInput(FlaskForm):
    entry_name = StringField('entry_name')
    entry_content = TextAreaField('entry_content')
    submit = SubmitField('update entry')


