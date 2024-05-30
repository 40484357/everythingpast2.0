from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import os
from dotenv import load_dotenv
from . import db
from .models import User
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Mail, Message
from . import mail

auth = Blueprint('auth', __name__)
s = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        Email = request.form.get("email")
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')
        if(password != passwordConfirm):
            flash('passwords do not match')

        checkUser = User.query.filter_by(email=Email).first()
       
        if checkUser:
            flash('a user with this email already exists')
            
        else:
            name = first_name + ' ' + last_name
            password = generate_password_hash(password, method='pbkdf2', salt_length=16)
            new_user = User(email = Email, password = password, name = name)
            db.session.add(new_user)
            db.session.commit()
            token = s.dumps(Email, salt='email-confirm')

            msg = Message('Confirm email', sender ='byronfry89@gmail.com', recipients=[Email])
            link = url_for('auth.confirm_email', token=token, external=True)
            msg.body='Your link is ()'.format(link)
            mail.send(msg)
            login_user(new_user, remember=True)
            return redirect(url_for('views.profile'))

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.profile'))
            else:
                flash('incorrect password', category='error')
        else:
            flash('incorrect email or account does not exist', category='error')
    return render_template("login.html")



@auth.route('/confirm_email/<token>')
def confirm_email(token):
    try: 
        email = s.load(token, salt='email-confirm', max_age=10000)
    except SignatureExpired: 
        return '<h1> The token is expired</h1>'
    return '<h1> The token works</h1>'