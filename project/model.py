import re
import joblib

def striphtml(data):
    p = re.compile(r'<.*?>|&.+;')
    return p.sub('', data)

from flask import Flask,Blueprint, render_template,redirect,request,jsonify,flash
from flask_login import login_required,current_user

model = Blueprint('model', __name__)

@model.route('/text')
@login_required
def text():
    return render_template('textinp.html')


@model.route("/predict",methods=['POST'])

def predict():
        
    model_mlp = open('Allevaite_model.pkl','rb')
    clf = joblib.load(model_mlp)

    if request.method == 'POST':
        message = request.form['editordata']
        cleantext = striphtml(message)
        title = request.form.get('title')
         
        # save the data in th database
        from . import db
        from .models import User,Post

        # post = Post(title=title, author=current_user.name , content = cleantext, owner_id=current_user.id)        
        # db.session.add(post)
        # db.session.commit()
        data = [cleantext]
        my_pred = str(clf.predict(data)[0])
        output_str = " Predicted Output Is ::: {} ".format(my_pred)
    return render_template('textinp.html',pred = output_str)