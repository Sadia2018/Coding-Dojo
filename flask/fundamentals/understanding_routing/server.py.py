from logging import exception
from flask import Flask
from flask.helpers import make_response
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World !"
@app.route('/dojo')
def dojo():
    return "This is my Dojo !"
@app.route('/say/<name>')
def say_name(name):
    return "Hi " + str(name)
@app.route('/repeat/<num>/<var>')
def num_var(num,var):
    return var * int(num)
@app.errorhandler(404)
def not_found(e):
    return "Sorry! No Response. Try again"
if __name__ == "__main__":
    app.run(debug=True)
