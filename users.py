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
    del session["csrf_token"]

def register(name, password, role):
    hash_value = generate_password_hash(password)
    try: 
        sql = "INSERT INTO users (username,password,role,created_at) VALUES (:username,:password,:role, NOW())"
        db.session.execute(sql, {"username":name,"password":hash_value,"role":role})
        db.session.commit()
    except:
        return False
    return login(name,password)

def check_username(username):
    if len(username) < 1 or len(username) > 20:
        return False
    return True

def check_password(password1):
    if password1 == "":
        return False
    return True

def check_passwords(password1, password2):
    if password1 != password2:
        return False
    return True

def check_role(role):
    if role not in ("1", "2"):
        return False
    return True

def user_id():
    return session.get("user_id")

def registration_time():
    user = user_id()
    sql = "SELECT created_at FROM users WHERE users.id=:user"
    result = db.session.execute(sql, {"user":user})
    return result.fetchone()[0]

def require_role(role):
    user_role = session["role"]
    if user_role != role:
        return False
    return True

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
