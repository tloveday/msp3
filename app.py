import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Home Page
@app.route("/")
@app.route("/landing")
def landing():
    movies = mongo.db.movies.find()
    tvshows = mongo.db.tvshows.find()
    return render_template("index.html", movies=movies, tvshows=tvshows)


# Registration Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' through cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful - Welcome to Level 7!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Sign In Page
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # Check Database for Username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check passwords match
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash(
                        "Welcome back Agent {}".format(
                            request.form.get("username")))
                    return redirect(url_for(
                         "profile", username=session["user"]))
            else:
                # Incorrect password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # No Username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


# User Profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("sign_in"))


# Sign out
@app.route("/sign_out")
def sign_out():
    # Remove the user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


# Movies Page
@app.route("/get_movies")
def get_movies():
    movies = mongo.db.movies.find()
    return render_template("movies.html", movies=movies)


# TV Shows Page
@app.route("/get_television")
def get_television():
    tvshows = mongo.db.tvshows.find()
    return render_template("tvshows.html", tvshows=tvshows)


# Review Form
@app.route("/review")
def review():
    return render_template("review.html")


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
