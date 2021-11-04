from flask import Flask 
from flask_classful import FlaskView 

app = Flask(__name__) 

class TestView(FlaskView): 
    def index(self): 
    # http://localhost:5000/
        return "<h1>This is my indexpage</h1>" 

TestView.register(app,route_base = '/')

if __name__ == '__main__':
    app.run(debug=True) 