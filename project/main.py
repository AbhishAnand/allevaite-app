from flask import Blueprint,render_template
from . import db
from flask_login import login_required
from project.models import User,Post

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    posts=Post.query.all()
    return render_template('dashboard.html',posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')