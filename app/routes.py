from flask import render_template

from app import myapp_obj


# different URL the app will implement
@myapp_obj.route("/")
# called view function
def hello():
    user = {'name' : 'Miguel (made with Dictionary)'}
    return render_template('hello.html', user_template=user)
