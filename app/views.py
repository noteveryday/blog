from flask import render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email
from app import app
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What\'s your email', validators=[Email()])
    submit = SubmitField('Submit')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.route('/', methods = ['GET', 'POST'])
def index():
    # user = {'nickname': 'Miguel'}
    name = None
    email = None
    form = NameForm()
    if form.validate_on_submit():
        # name = form.name.data
        # email = form.email.data
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    posts = [
        {'author': {'nickname': "john"},
         'body': 'Beautiful day in Portland!'},
        {'author': {'nickname': 'Susan'},
         'body': 'The Avengers movie was so cool!'}
    ]
    current_time = datetime.utcnow()

    return render_template('index.html',
                           title = 'Home',
                           form = form,
                           name = session.get('name'),
                           email = session.get('email'),
                           posts = posts,
                           current_time=current_time) 
