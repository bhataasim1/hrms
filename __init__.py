from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hrms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models here to avoid circular imports
from models import Employee, Attendance

# Create all tables
with app.app_context():
    db.create_all()

# Import routes after the app and db are initialized
from routes import *
