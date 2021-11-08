from app import app
from flask import Flask, render_template, redirect, session, request
from flask_bcrypt import Bcrypt
from app.models.user import User

bcrypt = Bcrypt(app)

#-------- main landing page - reg/log
@app.route('/')
def index():
    return render_template('index.html')