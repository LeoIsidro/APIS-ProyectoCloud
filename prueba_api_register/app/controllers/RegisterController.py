import json
from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario

def Register():
    
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            user1 = Usuario.query.filter(Usuario.username == username).first()
            user2 = Usuario.query.filter(Usuario.email == email).first()
        except Exception as err:
            print(err)
            return "Error while accessing user. Try again"

        if user1 != None:
            return "Username already exists"
        if user2 != None:
            return "Email already exists"

        user = Usuario(username=username,age = age,email = email,password = password)
        #newPoints = Puntos(username=username,position = PuestoDefault(),corrects = 0,fails=0,points = 0)
        
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print(err)
            return "Internal server error. Try again later"
        return redirect("/login")
    return render_template("register.html")


def registerasync():
    print("register")
    body=request.get_json()

    username = body["username"]
    email = body["email"]

    try:
        user1 = Usuario.query.filter(Usuario.username == username).first()
        user2 = Usuario.query.filter(Usuario.email == email).first()
    except Exception as err:
        print(err)
        return "Error while accessing user. Try again"

    if user1 != None:
        return "Username already exists"
    if user2 != None:
        return "Email already exists"

    
    user=Usuario(username=body["username"],age=body["age"],email=body["email"],password=body["password"])
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return json.dumps({"success": False, "username": user.username, "email": user.email})
    
    print(body)
    return json.dumps({"success": True, "username": user.username, "email": user.email})