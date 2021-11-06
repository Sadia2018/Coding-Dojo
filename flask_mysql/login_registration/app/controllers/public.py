from app import app
from flask import Flask, redirect, render_template, request, session, flash
from flask_bcrypt import Bcrypt
from app.models.user import User

bcrypt = Bcrypt(app)

#-------- main landing page - reg/log
@app.route('/')
def index():
    return render_template('index.html')

#------hidden route that validates form data
@app.route("/register", methods=['POST'])
def register():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    if not id:
        flash('something went wrong')
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')

#------- route that registers a user in and renders dashboard.
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user=User.get_one(data))

#------- route that logs a user in and renders dashboard. 
@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.get_email(data)
    if not user:
        flash('Email address not in use. Please register first ')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Incorrect password. Please check again')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

#------ route that logout and clears session. 
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')