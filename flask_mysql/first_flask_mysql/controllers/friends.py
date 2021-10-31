from first_flask_mysql import app
from flask import render_template, redirect,request
from models.friend import Friend

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
@app.route("/create_friend", methods=["POST"])
    # call the save classmethod to save new data
def create_friend():
    data = { 
        "fname":request.form["fname"],
        "lname":request.form["lname"],
        "occ":request.form["occ"]
    }
    Friend.save(data)
    return redirect('/')