from app import myapp_obj

# different URL the app will implement
@myapp_obj.route("/")
# called view function
def hello():
    user = {'name' : 'Miguel (made with Dictionary)'}
    # return HTML string
    #
    # Remember when using quotes inside of quotes you need to change.
    # For example, as shown below if the outside quotes are ' then any quotes
    # inside that string need to be " quotes.
    #
    # Also, I can print variables inside the string using {} because I put an
    # f in front of the start of the string.
    return f'''
    <html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
        <h1>Hello, {user["name"]} !</h1>
    </body>
    </html>'''

