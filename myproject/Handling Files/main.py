from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/success',methods=["POST"])
def success():
    if request.method == "POST":
        f = request.files['file1']
        f.save('static/'+f.filename)
        return "Success"

if __name__ == '__main__':
    app.run(debug=True)