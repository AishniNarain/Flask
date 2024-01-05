from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'title':'Blog Post 1',
        'author' : 'Aishni Narain',
        'content' : 'First Blog Post',
        'dated_on' : 'December 27, 2023'
    },
    {
        'title':'Blog Post 2',
        'author' : 'Aishni Narain',
        'content' : 'Second Blog Post',
        'dated_on' : 'December 28, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = posts)

@app.route('/about')
def about():
    return render_template('about.html',title = 'About')

if __name__ == '__main__':
    app.run(debug=True)