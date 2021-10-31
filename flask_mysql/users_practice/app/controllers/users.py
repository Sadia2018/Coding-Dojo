from app import app
from flask import render_template, request, redirect
from app.models.user import User

# app routes
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)

#index route
@app.route('/users/new')
def render_data():
    return render_template('create.html')

#route to insert new data
@app.route('/users/new', methods=['POST'])
def create_user():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect('/users')

#route to show each user info
@app.route('/users/<int:id>')
def show_user_info(id):
    data = {
        'id' : id
    }
    return render_template('show_user_info.html', user_info = User.show_info(data))

#route to render the template to update each user info.
@app.route('/users/<int:id>/edit')
def template_update_info(id):
    data = {
        'id': id
    }
    return render_template('update_info.html', user_info = User.show_info(data))

#route that takes in the form data and runs the function to update the database
@app.route('/users/<int:id>/edit', methods=['POST'])
def updated_info(id):
    data = {
        'id':id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.update_info(data)
    return redirect('/users')

#route that deletes from the database.
@app.route("/users/<int:id>/delete")
def delete(id):
    data = {
        'id':id
    }
    User.delete_info(data)
    return redirect('/users')