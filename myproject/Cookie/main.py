from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Hello World !")
    response.set_cookie("mycookie", "myvalue")
    return response

@app.route('/show_cookie')
def show_cookie():
    cookie_value = request.cookies.get("mycookie")
    return cookie_value

if __name__ == '__main__':
    app.run(debug=True)