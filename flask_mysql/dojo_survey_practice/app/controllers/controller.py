from app import app
from flask import Flask, render_template, redirect, request

from app.models.dojo import Dojo

#----------- main landing page. 
@app.route('/')
def index():
    return render_template('survey_page.html')

#----------- route that validates teh form data
@app.route('/process', methods=['POST'])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.save(request.form)
    return redirect('/dojos')