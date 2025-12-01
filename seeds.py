{"id":"59232","variant":"standard","title":"seeds.py"}
from datetime import datetime
from app import app
from models import db, User, Notification, Academic, HostelComplaint, Book, CafeteriaMenu, TransportSchedule, Event

with app.app_context():

    print("Creating database tables...")
    db.drop_all()
    db.create_all()

    print("Inserting seed data...")

    # ---- USERS ----
    user1 = User(username="student1", password="pass123", full_name="Demo Student")
    user2 = User(username="admin", password="admin", full_name="Admin User", role="admin")
    db.session.add_all([user1, user2])

    # ---- NOTIFICATIONS ----
    notif1 = Notification(
        title="Welcome",
        message="Welcome to Octopus Campus!",
        created_at=datetime.now()
    )
    notif2 = Notification(
        title="Library Info",
        message="Library is open from 9 AM to 6 PM.",
        created_at=datetime.now()
    )
    db.session.add_all([notif1, notif2])

    # ---- ACADEMICS ----
    academic1 = Academic(
        course="AI & ML",
        timetable="Mon 9–11, Wed 9–11",
        assignments="Assignment 1: Build ML model"
    )
    db.session.add(academic1)

    # ---- HOSTEL COMPLAINT ----
    complaint1 = HostelComplaint(
        student="Demo Student",
        room_no="B-101",
        issue="Light not working",
        status="open"
    )
    db.session.add(complaint1)

    # ---- BOOKS ----
    book1 = Book(title="Introduction to AI", author="Russell & Norvig", available=True)
    book2 = Book(title="Deep Learning", author="Goodfellow", available=False)
    db.session.add_all([book1, book2])

    # ---- CAFETERIA MENU ----
    week_menu = [
        ("Monday", "Idli, Sambar, Vada"),
        ("Tuesday", "Dosa, Chutney, Tea"),
        ("Wednesday", "Chappati, Curry"),
        ("Thursday", "Poori, Sabji"),
        ("Friday", "Uttapam, Sambar"),
        ("Saturday", "Veg Meals"),
        ("Sunday", "Biryani")
    ]
    for day, menu in week_menu:
        db.session.add(CafeteriaMenu(day=day, menu=menu))

    # ---- TRANSPORT ----
    transport1 = TransportSchedule(route="Hostel - Campus", time="8:00 AM", status="On Time")
    db.session.add(transport1)

    # ---- EVENTS ----
    event1 = Event(
        title="Tech Fest",
        description="Annual technical festival",
        date="2025-12-10",
        location="Auditorium"
    )
    db.session.add(event1)

    db.session.commit()
    print("Seed data inserted successfully!")