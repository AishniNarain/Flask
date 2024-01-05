from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    saved_name = request.cookies.get("saved_name")
    return render_template('index.html',saved_name = saved_name)

@app.route('/save_name',methods=['POST'])
def save_name():
    name = request.form['name']
    
    response = make_response(f"Hello {name}")
    response.set_cookie("saved_name",name)
    return response
    
@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("Sorry we don't remember your name !")
    response.set_cookie("saved_name","",expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)