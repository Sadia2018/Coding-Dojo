from flask import Flask, render_template, redirect,session
app = Flask(__name__)
@app.route('/')
def survey():
    return render_template('survey_page.html')
@app.route('/process')
def info():
    return redirect
if (__name__) == '__main__':
    app.run(debug=True)