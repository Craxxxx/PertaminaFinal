from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# register blueprint on init.py
auth = Blueprint('auth', __name__)
# register blueprint on init.py

# LOGIN ROUTES
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        # print(user)
        # print(user.username)
        # print(user.password)
        # print(username)
        # print(password)
        # exit()
        if user:
            if user.password == password:
                flash('Logged in successfully!', category='success')
                # pass the user that we logged in as 
                login_user(user, remember=True) #this user will be stored in the flask session until you restart the flask server
                # pass the user that we logged in as
                if current_user.permission == "Admin" :
                    return redirect(url_for('views.home4x4'))
                elif current_user.permission == "User" :
                    return redirect(url_for('views.Userhome4x4'))
            else:
                # print(user.username)
                # print(password)
                # print(user.password)
                # print(check_password_hash(user.password, password))
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", wincamss = [])
# LOGIN ROUTES

#logout routes
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
#logout routes

#REGISTER ROUTES
@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        # if user already exist flash error
        if user:
            flash('Username already exists.', category='error')
        else:
            #initiate an object for new data
            new_user = User(username=username, password=password)
            #initiate an object for new data

            #add data to database
            db.session.add(new_user)
            db.session.commit()
            #add data to database

            #create session
            login_user(new_user, remember=True)
            #create session
            
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))
    return render_template('register.html')
#REGISTER ROUTES




