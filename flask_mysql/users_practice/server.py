# import flask and user class into the server.py
from types import MethodDescriptorType
from flask import Flask, render_template,request, redirect
from werkzeug.utils import redirect
from user import User

app = Flask(__name__)
# app routes
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)

@app.route('/users/new')
def render_data():
    return render_template('create.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)