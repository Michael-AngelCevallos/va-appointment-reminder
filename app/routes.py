from flask import Blueprint, render_template, request, redirect, url_for
from .models import Appointment
from . import db
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/")
def index():
    appointments = Appointment.query.order_by(Appointment.appointment_date).all()
    return render_template("index.html", appointments=appointments)

@main.route("/add", methods=["POST"])
def add_appointment():
    title = request.form["title"]
    location = request.form["location"]
    date_str = request.form["appointment_date"]

    appointment_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M")

    appointment = Appointment(
        title=title,
        location=location,
        appointment_date=appointment_date
    )

    db.session.add(appointment)
    db.session.commit()

    return redirect(url_for("main.index"))
