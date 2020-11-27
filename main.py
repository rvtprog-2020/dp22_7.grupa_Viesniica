from flask import Flask, request, render_template, json, jsonify
import main

app = Flask(__name__)

CHAT_FILE = "main.txt"

def write(jsonData):
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(jsonData) + '\n')

def read():
    chatLines = []
    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        for row in f:
            chatLines.append(json.loads(row))
    
    return jsonify({"chatMsg":chatLines})

@app.route('/')
def mainpage1():
    return render_template('mainpage1.html')

@app.route('/mainpage2.html')
def mainpage2():
    return render_template('mainpage2.html')

@app.route('/sign_in.html')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up.html')
def sign_up():
    return render_template('sign_up.html')

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
