from doctorApp import app
from flask import render_template, redirect, url_for, flash, request
from doctorApp.models import Doctor
from doctorApp.forms import LoginForm
from doctorApp import db
from flask_login import login_user, logout_user, login_required, current_user
from urllib.error import HTTPError


@login_required
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    #patiens =  Patient.query.all().first()
    try:
        if form.validate_on_submit():
            attempted_doctor=Doctor.query.filter_by(email_address=form.email_address.data).first()
            if attempted_doctor and (attempted_doctor.password==form.password.data):
                login_user(attempted_doctor)
                return redirect(url_for('home_page'))
            else:
                flash('Pogresan email ili password', category='danger')
    except HTTPError:
        flash('Nema network konekcije', category='danger')
    except Exception:
        flash('Interni server error', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('login_page'))
