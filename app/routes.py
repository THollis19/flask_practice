from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Tim'}
    posts = [
        {
            'author': {'username': 'Kate'},
            'body': 'Moar tattoos!'
        },
        {
            'author': {'username': 'Darcy'},
            'body': 'I love to chew things!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)