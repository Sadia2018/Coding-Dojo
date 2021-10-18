from flask import Flask, request, redirect, session, render_template
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def visits():
    counter = session['counter']
    if 'counter' in session:
        session['counter'] = session.get('counter') + 1
        return render_template('index.html', counter=counter)
    else:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.pop('counter', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)