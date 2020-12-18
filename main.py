from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import main

#lg - Ckaai
#pw - eGcibzB1uJf9vcZn


client = MongoClient("mongodb+srv://Ckaai:eGcibzB1uJf9vcZn@myproject.bdsbv.mongodb.net/myProject?retryWrites=true&w=majority")
db = client.myProject

users_db = db.users

#user1 = {"name":"Leo", "surname":"Chu", "status":"admin"}
#users_db.insert_one(user1)
#exit()

app = Flask(__name__)

@app.route('/')
def mainpage1():
    return render_template('mainpage.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/croom')
def croom():
    return render_template('croom.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/catologue')
def catologue():
    return render_template('catologue.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route("/users")
def users():
    users_data = users_db.find()
    if users_data:
        return dumps(users_data)
    else:
        return {"error":"No users in DB"}

@app.route("/user/<id>")
def user(id):
    user = users_db.find_one({"_id":ObjectId(id)})
    if user:
        return dumps(user)

@app.route('/admin_room')
def admin_room():
    return render_template('admin_room.html')

@app.route("/user/create", methods = ["POST"])
def createUser():
    if request.method == "POST" and request.content_type == "application/json":
        dati = request.json
        users_db.insert_one({"vards":dati["vards"], "uzvards":dati["uzvards"], "status":dati["status"]})
        return {"message":"User crated!"}
    else:
        return {"error":"Method or content type not supprted!"}

app.run(host='0.0.0.0', port=80, debug=True)
