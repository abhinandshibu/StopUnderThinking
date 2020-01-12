from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# Key to stop CSRF attacks
app.config['SECRET_KEY'] = 'you-will-never-guess-hdcxxxgcbvdhpmqlcrrlsuioppmujgay'
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

from app.src import routes

