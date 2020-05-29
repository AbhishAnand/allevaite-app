from flask import Blueprint,render_template ,redirect ,url_for ,request ,flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user,logout_user
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm = request.form.get('confirm_pwd')

    # check if password and confirm password are equal 
    if password != confirm:
        flash('Passwords do not match !!! ')
        return redirect(url_for('auth.signup'))

    # if this returns a user, then the email already exists in database    
    user = User.query.filter_by(email=email).first() 
    if user:
        flash('Email address already exists !!! ')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password    
    new_user = User(email=email, name=username, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

# login method 
@auth.route('/login', methods=['POST'])
def login_post():
    user = request.form.get('user')
    password = request.form.get('pwd')

    user = User.query.filter_by(name=user).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    next_page = request.args.get('next')
    return redirect(next_page) if next_page else redirect(url_for('main.profile')) 