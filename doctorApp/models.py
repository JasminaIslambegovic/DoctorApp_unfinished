from doctorApp import db
from doctorApp import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(dr_id):
    return Doctor.query.get(int(dr_id))

class Doctor(db.Model, UserMixin): 
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    email_address = db.Column(db.String(length = 50), nullable = False, unique = True)
    password = db.Column(db.String(length = 60), nullable = False)
    photo = db.Column(db.BLOB)
    appointments = db.relationship('Appointment', backref = 'booked_doctor', lazy = True)

class Patient(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 60), nullable = False)
    photo = db.Column(db.BLOB)
    appointment = db.relationship('Appointment', backref = 'booked_patient', lazy = True)


class Appointment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    medical_problem = db.Column(db.String(length = 1024), nullable = False)
    doctor = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    patient = db.Column(db.Integer(), db.ForeignKey('patient.id'))
    day = db.Column(db.Integer(), nullable = False)
    month = db.Column(db.Integer(), nullable = False)
    year = db.Column(db.Integer(), nullable = False)
    hour = db.Column(db.Integer(), nullable = False)
    minutes = db.Column(db.Integer(), nullable = False)