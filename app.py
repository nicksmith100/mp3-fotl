import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


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

        ## Get current date

        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
                
        # Register admin user
        register = {
            "name": request.form.get("name"),
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
            "is_superuser": request.form.get("superuser-check"),
            "date_added": date
        }
        mongo.db.admins.insert_one(register)

        # Confirm registration with flash message
        flash("New admin {} successfully added".format(
            request.form.get("name")))

    #Get superuser status from database
    is_superuser = mongo.db.admins.find_one(
    {"username": session["user"]})["is_superuser"]

    # Get list of existing admins to display
    admins = mongo.db.admins.find()

    return render_template("register.html", admins=admins, is_superuser=is_superuser)


@app.route("/delete_admin/<admin_id>")
def delete_admin(admin_id):
    deleted_admin = mongo.db.admins.find_one({"_id": ObjectId(admin_id)})["username"]
    mongo.db.admins.delete_one({"_id": ObjectId(admin_id)})
    flash("Admin {} successfully deleted".format(deleted_admin))
    return redirect(url_for("register"))


@app.route("/switch_superuser/<admin_id>")
def switch_superuser(admin_id):

    admin = mongo.db.admins.find_one({"_id": ObjectId(admin_id)})
    
    is_superuser = "off" if admin.get('is_superuser') == "on" else "on"
    
    submit = {
            "$set": {
                "is_superuser": is_superuser
            }
        }

    switched_admin = mongo.db.admins.find_one({"_id": ObjectId(admin_id)})["username"]
    mongo.db.admins.update_one({"_id": ObjectId(admin_id)}, submit)
    flash("Superuser status of {} updated".format(switched_admin))
    return redirect(url_for("register"))


@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Login functionality from Code Institute Task Manager walkthrough:
    # https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/02-UserAuthenticationAndAuthorization/04-login_functionality/app.py
    
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.admins.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("artists"))
            else:
                # Invalid password
                flash("Incorrect username or password")
                return redirect(url_for("admin"))

        else:
            # Username doesn't exist
            flash("Incorrect username or password")
            return redirect(url_for("admin"))
    
    return render_template("admin.html")


@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("admin"))


@app.route("/event", methods=["GET", "POST"])
def event():

    if request.method == "POST":
        event_id = mongo.db.event.find_one()["_id"]
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")

        # Convert date strings to datetime objects
        if request.form.get("event_start") != "":
            event_start = datetime.strptime(request.form.get("event_start"), "%d-%m-%Y")
        else:
            event_start = datetime.strptime("01-01-1900", "%d-%m-%Y")

        if request.form.get("event_end") != "":
            event_end = datetime.strptime(request.form.get("event_end"), "%d-%m-%Y")
        else:
            event_end = datetime.strptime("01-01-1900", "%d-%m-%Y")

        # Convert comma separated string to list with no spaces
        stages_list = request.form.get("stages").replace(", ", ",").split(",")

        event_info = {
            "$set": {
            "event_name": request.form.get("event_name"),
            "event_about": request.form.get("event_about"),
            "event_img": request.form.get("event_img"),
            "event_location": request.form.get("event_location"),
            "event_start": event_start,
            "event_end": event_end,
            "stages": stages_list,
            "last_edit_by": session["user"],
            "last_edit_on": date
            }
        }
        mongo.db.event.update_one({"_id": event_id}, event_info)
        flash("Event info successfully updated")
        return redirect(url_for("event"))
    
    # Get superuser status from database
    is_superuser = mongo.db.admins.find_one(
    {"username": session["user"]})["is_superuser"]
    
    event = mongo.db.event.find_one()
    return render_template("event.html", is_superuser = is_superuser,
    event=event)


@app.route("/artists")
def artists():
    artists = list(mongo.db.artists.find())

    # Get superuser status from database
    is_superuser = mongo.db.admins.find_one(
    {"username": session["user"]})["is_superuser"]

    return render_template("artists.html",
    artists=artists,
    is_superuser=is_superuser)


@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    if request.method == "POST":
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")

        # Convert date strings to datetime objects
        if request.form.get("show1_start") != "":
            show1_start = datetime.strptime(request.form.get("show1_start"), "%d-%m-%Y %H:%M")
        else:
            show1_start = datetime.strptime("01-01-1900", "%d-%m-%Y")

        if request.form.get("show2_start") != "":
            show2_start = datetime.strptime(request.form.get("show2_start"), "%d-%m-%Y %H:%M")
        else:
            show2_start = datetime.strptime("01-01-1900", "%d-%m-%Y")

        if request.form.get("show3_start") != "":
            show3_start = datetime.strptime(request.form.get("show3_start"), "%d-%m-%Y %H:%M")
        else:
            show3_start = datetime.strptime("01-01-1900", "%d-%m-%Y")          

        artist = {
            "artist_name": request.form.get("artist_name"),
            "artist_bio": request.form.get("artist_bio"),
            "artist_url": request.form.get("artist_url"),
            "artist_img": request.form.get("artist_img"),
            "show1_stage": request.form.get("show1_stage"),
            "show1_start": show1_start,
            "show1_duration": request.form.get("show1_duration"),
            "show2_stage": request.form.get("show2_stage"),
            "show2_start": show2_start,
            "show2_duration": request.form.get("show2_duration"),
            "show3_stage": request.form.get("show3_stage"),
            "show3_start": show3_start,
            "show3_duration": request.form.get("show3_duration"),
            "last_edit_by": session["user"],
            "last_edit_on": date
        }
        mongo.db.artists.insert_one(artist)
        flash("Artist {} successfully added".format(request.form.get("artist_name")))
        return redirect(url_for("artists"))

    return render_template("add_artist.html")


@app.route("/edit_artist/<artist_id>", methods=["GET", "POST"])
def edit_artist(artist_id):

    if request.method == "POST":
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")

        # Convert date strings to datetime objects
        if request.form.get("show1_start") != "":
            show1_start = datetime.strptime(request.form.get("show1_start"), "%d-%m-%Y %H:%M")
        else:
            show1_start = datetime.strptime("01-01-1900", "%d-%m-%Y")

        if request.form.get("show2_start") != "":
            show2_start = datetime.strptime(request.form.get("show2_start"), "%d-%m-%Y %H:%M")
        else:
            show2_start = datetime.strptime("01-01-1900", "%d-%m-%Y")

        if request.form.get("show3_start") != "":
            show3_start = datetime.strptime(request.form.get("show3_start"), "%d-%m-%Y %H:%M")
        else:
            show3_start = datetime.strptime("01-01-1900", "%d-%m-%Y")          

        edited_artist = {
            "$set": {
            "artist_name": request.form.get("artist_name"),
            "artist_bio": request.form.get("artist_bio"),
            "artist_url": request.form.get("artist_url"),
            "artist_img": request.form.get("artist_img"),
            "show1_stage": request.form.get("show1_stage"),
            "show1_start": show1_start,
            "show1_duration": request.form.get("show1_duration"),
            "show2_stage": request.form.get("show2_stage"),
            "show2_start": show2_start,
            "show2_duration": request.form.get("show2_duration"),
            "show3_stage": request.form.get("show3_stage"),
            "show3_start": show3_start,
            "show3_duration": request.form.get("show3_duration"),
            "last_edit_by": session["user"],
            "last_edit_on": date
            }
        }
        mongo.db.artists.update_one({"_id": ObjectId(artist_id)}, edited_artist)
        flash("Artist {} successfully updated".format(request.form.get("artist_name")))
        return redirect(url_for("artists"))

    artist = mongo.db.artists.find_one({"_id": ObjectId(artist_id)})
    stages = ["river", "mill", "bar", "cottage"]
    return render_template("edit_artist.html", artist=artist, stages=stages)


@app.route("/delete_artist/<artist_id>")
def delete_artist(artist_id):
    deleted_artist = mongo.db.artists.find_one({"_id": ObjectId(artist_id)})["artist_name"]
    mongo.db.artists.delete_one({"_id": ObjectId(artist_id)})
    flash("Artist {} successfully deleted".format(deleted_artist))
    return redirect(url_for("artists"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
