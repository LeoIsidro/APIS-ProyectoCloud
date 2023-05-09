from app import app
import re
from flask import render_template, request, redirect
from app import db
import json
from app.models import Score, Usuario


def profile():
    user = request.args
    username = user.get("username")
    password = user.get("password")
    email = user.get("email")
    return render_template("profile.html", username=username, password=password, email=email)

def update():
    if request.method == "POST":
        usernameUpdate = request.form["username-update"]
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]

        if not username and not email and not password:
            return "Requires at least one parameter to update"
        user = Usuario.query.filter(Usuario.username==usernameUpdate).first()
        if user == None:
            return "Usuario Invalido"
        
        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email
        
        try:
            db.session.commit()
        except Exception as err:
            print("Error while updating", err)
            return "Internal error while updating, please try again"
        return redirect("/login")
    return render_template("update.html")

def juegoasync():
    body = request.get_json()
    username=body["username"]
    points=body["points"]
    try:
        user = Score.query.filter(Score.user_username == username).first()
    except Exception as err:
        print(err)
        return "Error while accessing user. Try again"
    if user == None:
        user = Score(user_username=username,points=points)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print(err)
            return json.dumps({"success": False, "username": user.user_username, "points": user.points})
        return json.dumps({"success": True, "username": user.user_username, "points": user.points})
    else:
        if user.points<points:
            user.points=points    
        try:
            db.session.commit()
        except Exception as err:
            print(err)
            return json.dumps({"success": False, "username": user.user_username, "points": user.points})
        return json.dumps({"success": True, "username": user.user_username, "points": user.points})