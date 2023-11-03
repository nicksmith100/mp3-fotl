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


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/lineup")
def lineup():
    artists = mongo.db.artists.find()
    return render_template("lineup.html", artists=artists)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.admins.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Register admin user
        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "is_superuser": request.form.get("superuser-check")
        }
        mongo.db.admins.insert_one(register)

        # Confirm registration with flash message
        flash("New admin {} successfully added!".format(
            request.form.get("username")))

    # Get list of existing admins to display
    admins = mongo.db.admins.find()

    return render_template("register.html", admins=admins)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
