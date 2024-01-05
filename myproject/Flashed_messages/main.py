from flask import Flask, redirect, url_for, flash, render_template

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
    flash("This is a flashed message !")
    return redirect(url_for('example'))

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == '__main__':
    app.run(debug=True)