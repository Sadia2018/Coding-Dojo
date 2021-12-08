from app import app
from flask import Flask, render_template, redirect, session, request
from flask_bcrypt import Bcrypt
from app.models.user import User
from app.models.listing import Listing

@app.route('/dashboard')
def view_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    all_listings=User.get_all_users_listing()
    print(all_listings)
    return render_template('dashboard.html', user=User.get_one(data), all_listings=all_listings)
