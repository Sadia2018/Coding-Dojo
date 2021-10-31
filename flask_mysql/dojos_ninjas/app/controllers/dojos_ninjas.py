from app import app
from flask import redirect, request,render_template
from app.models.dojo import Dojo
from app.models.ninja import Ninja

#app route to display dojos
@app.route('/dojos')
def display_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', all_dojos = dojos)

# hidden route that will run our method to add new dojos.
@app.route('/dojos', methods=['POST'])
def create_dojo():
    data = {
        'dname': request.form['dname']
    }
    Dojo.new_dojo(data)
    return redirect('/dojos')

#route that captures all dojos
@app.route('/dojos/ninjas')
def render():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('ninjas.html', all_dojos = dojos)

#route to display the ninja form where a new ninja can be added. 
@app.route('/dojos/ninjas', methods=["POST"])
def create_ninja():
    data = {
        'dojos_id': request.form['dojos_id'],
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age']
    }
    one_ninja = Ninja.new_ninja(data)
    return redirect('/dojos/'+ one_ninja.dojos_id)


# @app.route('/dojos/<int:id>')
# def render_dojo(id):
#     data = {
#         'id': id
#     }
#     return render_template()