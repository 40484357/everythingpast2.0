from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector
from flask_login import login_user, login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def landing():
    return render_template('index.html')

@views.route('/profile')
@login_required
def profile():
    name = current_user.name
    return render_template('profile.html', name = name)

