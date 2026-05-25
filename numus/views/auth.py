from flask import Blueprint, render_template,flash,request,redirect
from numus.extension import db
from numus.models import  User
import random

auth_bp = Blueprint("auth", __name__)

def get_random_id():
    random_id = random.randint(1,1000)
    users = User.query.all()
    used_id = [x.id for x in users]
    if random_id in used_id:
        return get_random_id()
    return random_id


@auth_bp.route("/login", methods=["POST", "GET"], strict_slashes=False)
def login():
    if request.method == "POST":
        userName = request.form.get("username")
        pass1 = request.form.get("password1")
        pass2 = request.form.get("password2")
        if pass1 != pass2:
            flash('Please make sure both password are same')
        elif len(pass1) < 7:
            flash("The password must be atleast 8 characters long")
        else:
            user = User(
                id = get_random_id(),
                username = userName,
                password = pass1
            )
            db.session.add(user)
            db.session.commit()
            for user in User.query.all():
                print(f'{user.id}/{user.username}/{user.password}')
            return redirect('/dashboard')
    return render_template("login.html")
