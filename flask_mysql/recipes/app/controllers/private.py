from flask.helpers import flash
from app import app
from flask import Flask, render_template, redirect, session, request
from app.models.user import User
from app.models.recipe import Recipe

#------ route that displays the dashboard 
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = { 
        'id' : session['user_id']
    }
    return render_template('dashboard.html', user=User.get_one(data), recipe_info=Recipe.get_user())

#----- route that renders the create page. 
@app.route('/recipes/new')
def new_recipe():
    return render_template('new_recipe.html')

#----- hidden route that will validate recipe form and add new recipe to the user.
@app.route("/recipes/create_new", methods=['POST'])
def add_new_recipe():
    is_valid = Recipe.validate(request.form)
    if not is_valid:
        return redirect('/recipes/new')
    data = {
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'under_30_minutes':request.form['under_30_minutes'],
        'created_at':request.form['created_at'],
        'users_id' : session['user_id']
    }
    id = Recipe.save(data)
    if not id:
        flash('something went wrong')
        return redirect('/recipes/new')
    return redirect('/dashboard')