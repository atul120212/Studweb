from application import app,db 
from flask import render_template,flash,redirect
from application.forms import LoginForm
from application.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()

        if user and user.password==password:
            flash('You are successfully logged in','success')
            return redirect('/index')
        else:
            flash('Something went Wrong','danger')
    return render_template('login.html',form=form,title='Login')