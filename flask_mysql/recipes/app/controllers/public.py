import re
from flask.helpers import flash
from app import app
from flask import Flask, render_template, redirect, session, request
from flask_bcrypt import Bcrypt
from app.models.user import User

bcrypt = Bcrypt(app)

#-------- main landing page - reg/log
@app.route('/')
def index():
    return render_template('index.html')

#-------- hidden route that validates form data - redirect to dashboard
@app.route('/register', methods=['POST'])
def register():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    if not id:
        flash('something went wrong')
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')