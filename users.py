import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql = "SELECT password, id, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    if not check_password_hash(user[0],password):
        return False
    if check_password_hash(user[0],password):
        session["user_id"] = user[1]
        session["username"] = username
        session["role"] = user[2]
        session["csrf_token"] = os.urandom(16).hex()                
        return True

def logout():
    del session["user_id"]
    del session["username"]
    del session["role"]

def register(name, password, role):
    hash_value = generate_password_hash(password)
    try: 
        sql = "INSERT INTO users (username,password,role,created_at) VALUES (:username,:password,:role, NOW())"
        db.session.execute(sql, {"username":name,"password":hash_value,"role":role})
        db.session.commit()
    except:
        return False
    return login(name,password)

def user_id():
    return session.get("user_id")

def require_role(role):
    user_role = session["role"]
    if user_role != role:
        return False
    return True

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
