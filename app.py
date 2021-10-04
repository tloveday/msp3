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
        reviews = list(mongo.db.reviews.find(
            {'reviewed_by': session["user"]}))
        tv_reviews = list(mongo.db.tvreviews.find(
            {'reviewed_by': session["user"]}))
        print(tv_reviews)

        return render_template("profile.html", username=username,
        tv_reviews=tv_reviews, reviews=reviews)

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


# Movie Information Page
@app.route("/movieinfo/<movie_id>")
def movieinfo(movie_id):
    # Gets movie info from db
    movie = mongo.db.movies.find_one({'_id': ObjectId(movie_id)})
    review = list(mongo.db.reviews.find())
    related_review = list(mongo.db.reviews.find({'movie_id': movie_id}))

    return render_template(
        'movie_info.html', movie=movie, review=review,
        related_review=related_review)


# TV Information Page
@app.route("/tvinfo/<tvshows_id>")
def tvinfo(tvshows_id):
    # Gets TV info from db
    tvshows = mongo.db.tvshows.find_one({'_id': ObjectId(tvshows_id)})
    tvreview = list(mongo.db.tvreviews.find())
    related_review = list(mongo.db.tvreviews.find({'tvshows_id': tvshows_id}))

    return render_template(
        'television_info.html', tvshows=tvshows, tvreview=tvreview,
        related_review=related_review)


# Movie Review Forms
@app.route("/review/<movie_id>", methods=["GET", "POST"])
def review(movie_id):
    if request.method == "POST":
        review = {
            "movie": movie_id,
            "headline": request.form.get("headline"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "reviewed_by": session["user"],
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Added")
        return redirect(url_for('get_movies'))

    return render_template("review.html", movie_id=movie_id)


# TV Show Review Form
@app.route("/tvreview/<tvshows_id>", methods=["GET", "POST"])
def tvreview(tvshows_id):
    if request.method == "POST":
        tvreview = {
            "show": tvshows_id,
            "headline": request.form.get("headline"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "reviewed_by": session["user"],
        }
        mongo.db.tvreviews.insert_one(tvreview)
        flash("Review Added")
        return redirect(url_for('get_television'))

    return render_template("tvreview.html", tvshows_id=tvshows_id)


# Edit Movie Reviews
@app.route("/edit_moviereview/<reviews_id>", methods=["GET", "POST"])
def edit_moviereview(reviews_id):
    if request.method == "POST":
        submit = {
            "headline": request.form.get("headline"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "reviewed_by": session["user"],
        }
        mongo.db.reviews.update({"_id": ObjectId(reviews_id)}, submit)
        flash("Review Successfully Edited")
        return redirect(url_for('get_movies'))

    review = mongo.db.reviews.find_one({"_id": ObjectId(reviews_id)})
    return render_template("edit_movie_review.html", reviews=review)


# Edit TV Review
@app.route("/edit_tvreview/<tvreviews_id>", methods=["GET", "POST"])
def edit_tvreview(tvreviews_id):
    if request.method == "POST":
        submitreview = {
            "headline": request.form.get("headline"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "reviewed_by": session["user"],
        }
        mongo.db.tvreviews.update({"_id": ObjectId(
            tvreviews_id)}, submitreview)
        flash("Review Successfully Edited")
        return redirect(url_for('get_television'))

    tvreview = mongo.db.tvreviews.find_one({"_id": ObjectId(tvreviews_id)})
    return render_template("edit_tv_review.html", tvreviews=tvreview)


# Delete Movie review
@app.route("/delete_moviereview/<reviews_id>")
def delete_moviereview(reviews_id):
    mongo.db.reviews.remove({"_id": ObjectId(reviews_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for('get_movies'))


# Delete TV Review
@app.route("/delete_tvreview/<tvreviews_id>")
def delete_tvreview(tvreviews_id):
    mongo.db.tvreviews.remove({"_id": ObjectId(tvreviews_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for('get_television'))


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
