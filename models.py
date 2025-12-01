{"id":"59231","variant":"standard","title":"models.py"}
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# ---------------- USER ----------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="student")

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

# ---------------- NOTIFICATIONS ----------------
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

# ---------------- ACADEMIC ----------------
class Academic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False)
    timetable = db.Column(db.String(200), nullable=False)
    assignments = db.Column(db.String(300), nullable=False)

# ---------------- HOSTEL COMPLAINT ----------------
from datetime import datetime

class HostelComplaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(100), nullable=False)
    room_no = db.Column(db.String(20), nullable=False)
    issue = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default="open")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ---------------- BOOKS ----------------
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, nullable=False)

# ---------------- CAFETERIA MENU ----------------
class CafeteriaMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    menu = db.Column(db.String(200), nullable=False)

# ---------------- TRANSPORT ----------------
class TransportSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# ---------------- EVENTS ----------------
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)