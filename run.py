# include Flask class from file flask
from flask import Flask

# create an instance of Flask class
# __name__ is a predefined setup variable
myapp_obj = Flask(__name__)

# different URL the app will implement
@myapp_obj.route("/")
# called view function
def hello():
    return "Hello World!"

myapp_obj.run()



