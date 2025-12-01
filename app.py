from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Notification, Academic, HostelComplaint, Book, CafeteriaMenu, TransportSchedule, Event
import config
import os

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        full_name = request.form.get('full_name','')
        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
            return redirect(url_for('register'))
        user = User(username=username, password=password, full_name=full_name)
        db.session.add(user)
        db.session.commit()
        flash("Registered. Please log in.", "success")
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/dashboard")
@login_required
def dashboard():
    latest_notifications = Notification.query.order_by(Notification.created_at.desc()).limit(5).all()
    return render_template("dashboard.html", notifications=latest_notifications)

# Academics
@app.route("/academics")
@login_required
def academics():
    courses = Academic.query.all()
    return render_template("academics.html", courses=courses)

# Hostel
@app.route("/hostel", methods=["GET","POST"])
@login_required
def hostel():
    if request.method == "POST":
        room_no = request.form.get('room_no','')
        issue = request.form.get('issue','')
        complaint = HostelComplaint(student=current_user.full_name or current_user.username, room_no=room_no, issue=issue)
        db.session.add(complaint)
        db.session.commit()
        flash("Complaint submitted", "success")
        return redirect(url_for('hostel'))
    complaints = HostelComplaint.query.filter_by(student=current_user.full_name or current_user.username).all()
    return render_template("hostel.html", complaints=complaints)

# Library
@app.route("/library")
@login_required
def library():
    books = Book.query.all()
    return render_template("library.html", books=books)

# Cafeteria
@app.route("/cafeteria")
@login_required
def cafeteria():
    menus = CafeteriaMenu.query.all()
    return render_template("cafeteria.html", menus=menus)

# Transport
@app.route("/transport")
@login_required
def transport():
    schedules = TransportSchedule.query.all()
    return render_template("transport.html", schedules=schedules)

# Events
@app.route("/events")
@login_required
def events():
    events = Event.query.order_by(Event.date).all()
    return render_template("events.html", events=events)

# Notifications
@app.route("/notifications")
@login_required
def notifications():
    notifs = Notification.query.order_by(Notification.created_at.desc()).all()
    return render_template("notifications.html", notifications=notifs)

# Simple route to create a notification (admin-like, for prototype)
@app.route("/create-notification", methods=["POST"])
@login_required
def create_notification():
    title = request.form.get('title')
    message = request.form.get('message')
    if title and message:
        n = Notification(title=title, message=message)
        db.session.add(n)
        db.session.commit()
        flash("Notification created", "success")
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    # ensure instance folder
    os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)
    app.run(debug=True)