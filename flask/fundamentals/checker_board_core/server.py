from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/<int:num>')
def smaller_checkerboard(num):
    return render_template('smaller_checkerboard.html', num = num )
@app.route('/<int:length>/<int:width>')
def custom_checker(length, width):
    return render_template('custom_checker.html',length = length, width = width )
if __name__ == '__main__':
    app.run(debug=True)