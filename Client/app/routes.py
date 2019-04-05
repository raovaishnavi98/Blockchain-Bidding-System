from flask import render_template
from app import app
from app.forms import LoginForm

# ...
@app.route('/add')
def add():
    return render_template('base.html',request.form['name'])
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
