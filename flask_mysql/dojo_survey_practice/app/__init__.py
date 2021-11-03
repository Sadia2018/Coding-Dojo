from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'super_secret_key'