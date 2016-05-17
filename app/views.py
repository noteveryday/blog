from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from app import app

bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {'author': {'nickname': "john"},
         'body': 'Beautiful day in Portland!'},
        {'author': {'nickname': 'Susan'},
         'body': 'The Avengers movie was so cool!'}
    ]
    current_time = datetime.utcnow()

    return render_template('index.html',
                           title = 'Home',
                           user = user,
                           posts = posts,
                           current_time=current_time) 
