from app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from app.models.user import User

bcrypt = Bcrypt(app)