from app import app
from flask import Flask, redirect, render_template, request, session
from flask_bcrypt import Bcrypt
from app.models.user import User


