from flask import render_template

from app import myapp_obj
from app.forms import LoginForm


# different URL the app will implement
@myapp_obj.route("/")
# called view function
def hello():
    user = {'name' : 'Miguel (made with Dictionary)'}
    posts = [
        {
            'author' : 'Linh',
            'body' : 'Beautiful day in San Jose!'
        },
        {
            'author': 'Emma',
            'body' : 'I got my vaccine today!'
        }
    ]

    return render_template('hello.html', user_template=user, posts=posts)

@myapp_obj.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

