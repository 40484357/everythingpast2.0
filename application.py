from webapp import application
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user






if __name__ == '__main__':
    application.run(debug=True)