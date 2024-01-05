from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my Youtube Channel'

# Dynamic Url Building

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the score is '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the score is '+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    # return result
    return redirect(url_for(result,score = marks))
    
if __name__ == '__main__':
    app.run(debug = True)
     