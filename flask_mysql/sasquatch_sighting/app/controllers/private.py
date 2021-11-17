from types import MethodDescriptorType
from app import app
from flask import Flask, render_template, redirect, session, request
from flask_bcrypt import Bcrypt
from app.models.user import User
from app.models.sighting import Sighting

#------ route that renders the dashboard. 
@app.route('/dashboard')
def view_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    all_sights=User.get_all_users_sighting()
    print(all_sights)
    return render_template('dashboard.html', user=User.get_one(data), all_sights=all_sights)

# ------ route that render the page to report a sighiting for the user. 
@app.route('/dashboard/new/sighting')
def report():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    return render_template('sighting.html', user=User.get_one(data))

#------ hidden route that takes in the sight form, saves and redirects to dashboard.
@app.route('/dashboard/new/sighting/create', methods=['POST'])
def create():
    is_valid = Sighting.validate(request.form)
    if not is_valid:
        return redirect('/dashboard/new/sighting')
    data = {
        'location': request.form['location'],
        'date_of_sighting': request.form['date_of_sighting'],
        'what_happened' : request.form['what_happened'],
        'number_of_sasquatches': request.form ['number_of_sasquatches'],
        'users_id':request.form ['users_id']
    }
    Sighting.save(data)
    return redirect('/dashboard') # saves a sighting, showing in the database.

#------- app route that renders sightings page. 
@app.route('/dashboard/sighting')
def show_sights():
    data = {
        'id' : session['user_id']
    }
    return render_template ('dashboard.html', all_sights=User.get_sightings_with_user(data), user=User.get_one(data) )

#------ app route that deletes a sighting.
@app.route('/sighting/delete/<int:id>')
def delete_sighting(id):
    data = {
        'id': id
    }
    Sighting.delete(data)
    return redirect('/dashboard')

#----- app routes that renders the edit.
@app.route('/sighting/edit/<int:id>')
def edit(id):
    data ={
    'id':id
    }
    return render_template('edit.html', user=User.get_one(data), sight=Sighting.get_one(data))

#----- app route that redirects back to the dashboard. 
@app.route('/sighting/edit/update/<int:id>', methods=['POST'])
def update(id):
    is_valid = Sighting.validate(request.form)
    if not is_valid:
        return redirect('/sighting/edit/<int:id>')
    data = {
        'location': request.form['location'],
        'date_of_sighting': request.form['date_of_sighting'],
        'what_happened' : request.form['what_happened'],
        'number_of_sasquatches': request.form ['number_of_sasquatches'],
        'id':id
    }
    Sighting.update(data)
    return redirect('/dashboard') # is this redirect route correct ?

#----- app route that takes to view details. 
@app.route('/sighting/show/<int:id>')
def show_details(id):
    data = {
        'id':id
    }
    return render_template('details.html', user=User.get_one(data), sight=Sighting.get_one(data))