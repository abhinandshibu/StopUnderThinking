# importing the user table to query the database for validation
from app.models import User
# hashing and salt libraries
import hashlib
# used for creating a session for the user when they login
from flask_login import login_user

def loginValidation(LoginForm):
    form = LoginForm
    usernameEmail = form.usernameEmail.data
    password = form.password.data

    user = User.query.filter_by(username=usernameEmail).first()
    if user is None:
        user = User.query.filter_by(email=usernameEmail).first()
        if user is None:
            return "username or email not found", None

    password = password.encode('utf-8')
    password_hash = hashlib.sha512(password + user.salt).hexdigest()

    if password_hash == user.password_hash:
        # i.e. error = False, so no errors
        login_user(user)
        return False, user.id
    else:
        return "password does not match", None

