from flask import Flask, request
from flask import render_template
from flask import current_app as app
from .models import *

@app.route("/login", methods=["GET","POST"])
def login_user():
    error=None
    if request.method=='POST':
        user=request.form["username"]
        pwd=request.form["password"]
        s=User.query.filter_by(username=user).first()
        if s==None:
            error="User Not Found. You can register here!"
            return render_template("register.html",error=error)
        else:
            s=User.query.filter_by(username=user,password=pwd).first()
            if s:
                return render_template("dashboard.html",user=user)
            else:
                error="Invalid Password"
    else:
        return render_template("index.html")
    return render_template("index.html",error=error)

@app.route("/register", methods=["GET","POST"])
def register_user():
    error=None
    if request.method=='POST':
        user=request.form["username"]
        pwd=request.form["password"]
        s=User(username=user,password=pwd)
        try:
            db.session.add(s)
            db.session.commit()
        except Exception as e: 
            error="User already exists. Please try with a different user name"
            return render_template("register.html",error=error)
    else:
        return render_template("register.html")
    return render_template("index.html",error="Registration Successfull! Please login again")
