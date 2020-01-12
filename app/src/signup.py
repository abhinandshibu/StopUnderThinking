# re is a regex library
import re
from app import db
from app.models import User, Journal, Section, Entry
# hashing library
import hashlib
# a random generator library used for salt
import uuid

def signupValidation(SignupForm):
    form = SignupForm
    username = form.username.data
    firstname = form.firstName.data
    surname = form.surname.data
    email = form.email.data
    password1 = form.password1.data
    password2 = form.password2.data

    # Username Validation
    # username can only contain . _ and alphanumeric
    regexusername = re.compile('^(?=.{5,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')
    # follow an email format ie. have an @, only allows alphanumerical and certain other characters
    regexemail = re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    # password minimum 8 character, at least 1 number 1 letter
    regexpassword = re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

    if not regexusername.match(username):
        return "username must be between 5-20 characters, contain letters, numbers or ._", None

    elif (User.query.filter_by(username=username).scalar()) is not None:
        return "username is taken", None

    # First name Validation
    elif (len(firstname) < 2 or len(firstname) > 14):
        # !!!!!!!!!!!!!!!!!!!! fix lower case thingy, lower case usernames still match
        # func.lower(User.username) == func.lower("GaNyE")
        return "firstname must be 2 - 20 characters", None

    elif not firstname.isalpha():
        return "firstname can only contain letters", None

    # Surname Validation
    elif (len(surname) < 2 or len(surname) > 14):
        return "surname must be 2 - 20 characters", None

    elif not surname.isalpha():
        return "surname can only contain letters", None

    # Email Validation
    elif not regexemail.match(email):
        return "invalid email", None

    elif (User.query.filter_by(email=email).scalar()) is not None:
        return "email is taken", None

    # Password validation
    elif password1 != password2:
        return "passwords do not match", None

    elif not regexpassword.match(password1):
        return "passwords must be a minimum of 8 characters, with at least 1 number and letter", None

    else:
        password = password1.encode('utf-8')
        salt = uuid.uuid4().hex.encode('utf-8')
        password_hash = hashlib.sha512(password + salt).hexdigest()

        user = User(username=username, firstname=firstname, surname=surname, email=email, salt=salt, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        journal = Journal(name="my journal", user_id=user.id)
        db.session.add(journal)
        db.session.commit()
        section = Section(name="my section", journal_id=journal.id)
        db.session.add(section)
        db.session.commit()
        entry = Entry(name="my entry", section_id=section.id, content="this is some content")
        db.session.add(entry)
        db.session.commit()


        # i.e. error = False, so no errors
        return False, user.id


