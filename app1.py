### Building URL Dynamically
### Variable Rules And URL Building

from flask import Flask,redirect, url_for
app = Flask(__name__)

@app.route("/")
def welcome():
    return " Hey I'm Raguram"

@app.route('/success/<int:score>')
def success(score):
    return "<html><boby><h1>The Result is Pass</h1></boby></html>"

@app.route('/failed/<int:score>')
def failed(score):
    return "<html><boby><h1>The Result is Fail</h1></boby></html>"

## Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result = 'failed'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

if __name__=="__main__":
    app.run(debug=True)