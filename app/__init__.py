from flask import Flask
from Products.views import *

app=Flask(__name__)

app.register_blueprint(products)

if __name__ == "__main__":
    app.run(debug=True) 

