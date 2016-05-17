from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from app import app
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
@app.route('/', methods = ['GET', 'POST'])
def index():
    # user = {'nickname': 'Miguel'}
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
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
                           name = name,
                           posts = posts,
                           current_time=current_time) 
