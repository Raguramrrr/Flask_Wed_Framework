from flask import Flask
## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "I'm rajaraguraman"

@app.route('/fine')
def fine():
    return " How are you, i'm fine"

if __name__ == '__main__':
    app.run(debug=True) 