from flask import Flask, request, render_template, json, jsonify

app = Flask(__name__)

@app.route('/')
def mainpage1():
    return render_template('mainpage1.html')

@app.route('/mainpage2.html')
def mainpage2():
    return render_template('mainpage2.html')

@app.route('/sign_in.html')
def sign_in():
    return render_template('sign_in.html')

@app.route('/croom.html')
def croom():
    return render_template('croom.html')

@app.route('/help.html')
def help():
    return render_template('help.html')

@app.route('/catologue.html')
def catologue():
    return render_template('catologue.html')

app.run(host='0.0.0.0', port=80, debug=True)