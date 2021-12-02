from app import app
from flask import Flask, render_template, redirect, session, request
from flask_bcrypt import Bcrypt
from app.models.user import User
from app.models.car import Car

#------ route that renders the dashboard. 
@app.route('/dashboard')
def view_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    all_cars=User.get_all_users_car()
    print(all_cars)
    return render_template('dashboard.html', user=User.get_one(data), all_cars=all_cars)

# ------ route that render the page to report a sighiting for the user. 
@app.route('/dashboard/new/')
def report():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    return render_template('new_car.html', user=User.get_one(data))

#------ hidden route that takes in the sight form, saves and redirects to dashboard.
@app.route('/dashboard/new/create', methods=['POST'])
def create():
    is_valid = Car.validate(request.form)
    if not is_valid:
        return redirect('/dashboard/new/')
    data = {
        'price': request.form['price'],
        'model': request.form['model'],
        'make' : request.form['make'],
        'year': request.form ['year'],
        'description': request.form['description'],
        'users_id':request.form ['users_id']
    }
    Car.save(data)
    return redirect('/dashboard')

#----- app routes that renders the edit.
@app.route('/dashboard/edit/<int:id>')
def edit(id):
    data ={
    'id':id
    }
    return render_template('edit_car.html', user=User.get_one(data), one_car=Car.get_one(data))

#----- app route that redirects back to the dashboard. 
@app.route('/dashboard/edit/update/<int:id>', methods=['POST'])
def update(id):
    is_valid = Car.validate(request.form)
    if not is_valid:
        return redirect('/dashboard/edit/<int:id>')
    data = {
        'price': request.form['price'],
        'model': request.form['model'],
        'make' : request.form['make'],
        'year': request.form ['year'],
        'description': request.form['description'],
        'id':id
    }
    Car.update(data)
    return redirect('/dashboard')

#------ app route that deletes a car.
@app.route('/dashboard/delete/<int:id>')
def delete_car(id):
    data = {
        'id': id
    }
    Car.delete(data)
    return redirect('/dashboard')

#----- app route that takes to view details. 
@app.route('/dashboard/show/<int:id>')
def show_details(id):
    data = {
        'id':id
    }
    return render_template('show_details.html', user=User.get_one(data), one_car=Car.get_one(data))

