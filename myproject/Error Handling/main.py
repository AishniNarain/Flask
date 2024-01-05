from flask import Flask, redirect, url_for, render_template, request,abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success')
def success():
    return "Logged in Successfully"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['uname'] == 'Aishni' and request.form['pass'] == 'Aishni123':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True)