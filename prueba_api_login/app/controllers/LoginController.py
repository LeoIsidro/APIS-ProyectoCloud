from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario
import requests
import json
from cryptography.hazmat.primitives import hashes   

def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            return "Missing form parameter username or password"
        
        try:
            user = Usuario.query.filter(Usuario.username == username).first()
            if user == None or password != user.password:
                return "Invalid username or password"
            email = user.email
            password = bytes(password, 'utf-8')
            digest = hashes.Hash(hashes.SHA256())
            digest.update(password)
            hashedPassword = str(digest.finalize())
            return redirect("/juego?username="+username+"&email="+email+"&password="+hashedPassword)
        except Exception as err:
            print(err)
            return "Error while accessing user. Try again"  

    return render_template("login.html")


def loginasync():
    body = request.get_json()
    username=body["username"] 
    password=body["password"]
    try:
        user = Usuario.query.filter(Usuario.username == username).first()
        if username == None or password != user.password:
            return json.dumps({"success": False})
        else:
            print(body)
            return json.dumps({"success": True, "username": user.username})
    except:
        return json.dumps({"success": False, "username": user.username}) 



def register():
    return redirect("/register")


def option():
    if request.method == "POST":
        points  = request.points["points"]
        id = request.id["points"]

        game = Usuario.quey.filter(Usuario.id == id).first()

        if game == None: 
            return "Este usuario no tiene un puntaje aún"
        if game.points > game.points: 
            return game