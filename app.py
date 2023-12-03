
import os
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
    abort,
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from bson.json_util import dumps, loads
import cloudinary
import cloudinary.uploader

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]

# Cloudinary config
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
)


# Utility functions -----------------------------------------------------------

# Convert date string to datetime object
# Set date 01-01-1900 if not provided
def ds_to_dt(date_string):

    if date_string != "":
        return datetime.strptime((date_string), "%d-%m-%Y %H:%M")
    else:
        return datetime.strptime("01-01-1900", "%d-%m-%Y")


# Convert date string to date object
# Set date 01-01-1900 if not provided
def ds_to_date(date_string):

    if date_string != "":
        return datetime.strptime((date_string), "%d-%m-%Y")
    else:
        return datetime.strptime("01-01-1900", "%d-%m-%Y")


# Main application -----------------------------------------------------------

# Inject content for base template
@app.context_processor
def inject_content():

    # Get key info from database
    key_info = mongo.db.key_info.find_one()

    # Get superuser status from database
    if "user" in session:
        is_superuser = mongo.db.admins.find_one(
            {"username": session["user"]})["is_superuser"]
    else:
        is_superuser = "off"

    # Set Cloudinary base url
    cloudinary_url = \
        "https://res.cloudinary.com/dpy1aevmo/image/upload/f_auto,q_auto/"

    return dict(
        key_info=key_info, is_superuser=is_superuser,
        cloudinary_url=cloudinary_url
    )


@app.route("/")
@app.route("/home")
def home():
    GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
    return render_template("home.html",
                           GOOGLE_MAPS_API_KEY=GOOGLE_MAPS_API_KEY)


@app.route("/lineup")
def lineup():

    # Get individual dates for schedule
    start_dt = mongo.db.key_info.find_one()["event_start"]
    end_dt = mongo.db.key_info.find_one()["event_end"]
    delta = timedelta(days=1)
    dates = []

    while start_dt <= end_dt:
        dates.append(start_dt)
        start_dt += delta

    # Add individual showtimes to list
    showtimes = []
    artists = list(mongo.db.artists.find())
    for artist in artists:

        shows = ["show1", "show2", "show3"]

        for show in shows:

            if artist[f"{show}_duration"] == "":
                showtime_duration = 0
            else:
                showtime_duration = int(artist[f"{show}_duration"])

            if artist[f"{show}_start"] > datetime(1900, 1, 1):

                # Get showtime info from database
                showtime_stage = artist[f"{show}_stage"]
                showtime_artist = artist["artist_name"]
                showtime_day = artist[f"{show}_start"].strftime("%A")
                showtime_start = artist[f"{show}_start"]
                showtime_end = showtime_start + timedelta(
                    minutes=showtime_duration)

                # Add showtime information to list
                showtimes.append(
                    {
                        "showtime_stage": showtime_stage,
                        "showtime_artist": showtime_artist,
                        "showtime_day": showtime_day,
                        "showtime_start": showtime_start,
                        "showtime_end": showtime_end,
                    }
                )

    # Sort showtimes by start date/time
    showtimes.sort(key=lambda item: item["showtime_start"])

    # Sort artists by artist name
    artists = list(mongo.db.artists.find().sort("artist_name"))

    # Get stage names from database
    stages = mongo.db.key_info.find_one()["stages"]

    # Get display_schedule value from database
    display_schedule = mongo.db.key_info.find_one()["display_schedule"]

    return render_template(
        "lineup.html",
        artists=artists,
        dates=dates,
        showtimes=showtimes,
        stages=stages,
        display_schedule=display_schedule,
    )


@app.route("/superuser", methods=["GET", "POST"])
def superuser():

    # Check user is admin
    if "user" in session:

        # Check user is superuser
        user_is_superuser = mongo.db.admins.find_one(
            {"username": session["user"]})["is_superuser"]

        if user_is_superuser == "on":

            if request.method == "POST":
                # Check if username already exists
                existing_user = mongo.db.admins.find_one(
                    {"username": request.form.get("username").lower()}
                )

                if existing_user:
                    flash("Username already exists")
                    return redirect(url_for("superuser"))

                # Get current date
                now = datetime.now()
                date = now.strftime("%d-%m-%Y")

                # Register admin user
                register = {
                    "name": request.form.get("name"),
                    "username": request.form.get("username"),
                    "password": generate_password_hash(
                        request.form.get("password")),
                    "is_superuser": request.form.get("superuser-check"),
                    "date_added": date,
                }
                mongo.db.admins.insert_one(register)

                # Confirm registration with flash message
                flash(
                    "New admin {} successfully added".format(
                        request.form.get("name"))
                )

            # Get list of existing admins to display
            admins = mongo.db.admins.find()

        else:
            abort(403)

        return render_template("superuser.html", admins=admins)

    else:

        abort(403)


@app.route("/delete_admin/<admin_id>")
def delete_admin(admin_id):

    # Check user is admin
    if "user" in session:

        # Check user is superuser
        user_is_superuser = mongo.db.admins.find_one(
            {"username": session["user"]})["is_superuser"]

        if user_is_superuser == "on":

            deleted_admin = mongo.db.admins.find_one(
                {"_id": ObjectId(admin_id)})[
                "username"
            ]
            mongo.db.admins.delete_one({"_id": ObjectId(admin_id)})
            flash("Admin {} successfully deleted".format(deleted_admin))
            return redirect(url_for("superuser"))

        else:

            abort(403)

    else:

        abort(403)


@app.route("/switch_superuser/<admin_id>")
def switch_superuser(admin_id):

    # Check user is admin
    if "user" in session:

        # Check user is superuser
        user_is_superuser = mongo.db.admins.find_one(
            {"username": session["user"]})["is_superuser"]

        if user_is_superuser == "on":

            admin = mongo.db.admins.find_one({"_id": ObjectId(admin_id)})

            # Toggle superuser status of selected admin
            is_superuser = "off" if admin.get("is_superuser") == "on" else "on"

            submit = {"$set": {"is_superuser": is_superuser}}

            switched_admin = mongo.db.admins.find_one(
                {"_id": ObjectId(admin_id)})[
                "username"
            ]
            mongo.db.admins.update_one({"_id": ObjectId(admin_id)}, submit)
            flash("Superuser status of {} updated".format(switched_admin))
            return redirect(url_for("superuser"))

        else:

            abort(403)

    else:

        abort(403)


@app.route("/admin", methods=["GET", "POST"])
def admin():

    # Login functionality from Code Institute Task Manager walkthrough:
    # https://github.com/Code-Institute-Solutions/TaskManagerAuth/

    if request.method == "POST":

        # Check if username exists in db
        existing_user = mongo.db.admins.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))

                # Direct user to key_info template if festival dates in past,
                # otherwise artists template
                now = datetime.now()
                event_start = mongo.db.key_info.find_one()["event_start"]
                if event_start < now:
                    return redirect(url_for("key_info"))
                else:
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

    # Check user is admin
    if "user" in session:

        # Remove user from session cookie
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("admin"))

    else:
        abort(403)


@app.route("/key_info", methods=["GET", "POST"])
def key_info():

    # Check user is admin
    if "user" in session:

        if request.method == "POST":
            key_info_id = mongo.db.key_info.find_one()["_id"]
            now = datetime.now()
            date = now.strftime("%d-%m-%Y")

            # Convert date strings to datetime objects
            event_start = ds_to_date(request.form.get("event_start"))
            event_end = ds_to_date(request.form.get("event_end"))

            # Convert comma separated string to list with no spaces
            stages_list = request.form.get(
                "stages").replace(", ", ",").split(",")

            # Get current main_img ID and assign it to upload_result variable
            upload_result = mongo.db.key_info.find_one()["main_img"]

            # Upload image to Cloudinary and return public_id
            main_img = request.files["main_img"]
            if main_img.filename.split(".")[-1].lower() in ALLOWED_EXTENSIONS:
                upload_result = cloudinary.uploader.upload(
                    main_img)["public_id"]

            key_info = {
                "$set": {
                    "event_start": event_start,
                    "event_end": event_end,
                    "stages": stages_list,
                    "display_schedule": request.form.get("display_schedule"),
                    "main_img": upload_result,
                    "banner_heading": request.form.get("banner_heading"),
                    "banner_text": request.form.get("banner_text"),
                    "fundraising_url": request.form.get("fundraising_url"),
                    "last_edit_by": session["user"],
                    "last_edit_on": date,
                }
            }
            mongo.db.key_info.update_one({"_id": key_info_id}, key_info)
            flash("Key info successfully updated")
            return redirect(url_for("key_info"))

        # Check if shows have been added
        show_stages = []
        artists = list(mongo.db.artists.find())
        shows = ["show1", "show2", "show3"]

        for artist in artists:
            for show in shows:
                if artist[f"{show}_start"] > datetime(1900, 1, 1):
                    if artist[f"{show}_stage"] != "":
                        show_stage = artist[f"{show}_stage"]
                        show_stages.append(show_stage)

        if len(show_stages) > 0:
            shows_exist = True
        else:
            shows_exist = False

        key_info = mongo.db.key_info.find_one()
        return render_template("key_info.html", shows_exist=shows_exist)

    else:
        abort(403)


@app.route("/delete_event")
def delete_event():

    # Check user is admin
    if "user" in session:

        key_info_id = mongo.db.key_info.find_one()["_id"]
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")

        # Set values to blank or defaults
        key_info = {
            "$set": {
                "event_start": datetime.strptime("01-01-1900", "%d-%m-%Y"),
                "event_end": datetime.strptime("01-01-1900", "%d-%m-%Y"),
                "stages": "",
                "display_schedule": "",
                "main_img": "",
                "banner_heading": "",
                "banner_text": "",
                "fundraising_url": "",
                "last_edit_by": session["user"],
                "last_edit_on": date,
            }
        }

        mongo.db.key_info.update_one({"_id": key_info_id}, key_info)
        flash("Event successfully deleted")
        return redirect(url_for("key_info"))

    else:
        abort(403)


@app.route("/artists")
def artists():

    # Check user is admin
    if "user" in session:

        artists = list(mongo.db.artists.find().sort("artist_name"))

        return render_template("artists.html", artists=artists)

    else:
        abort(403)


@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():

    # Check user is admin
    if "user" in session:

        if request.method == "POST":
            now = datetime.now()
            date = now.strftime("%d-%m-%Y")

            # Convert date strings to datetime objects
            show1_start = ds_to_dt(request.form.get("show1_start"))
            show2_start = ds_to_dt(request.form.get("show2_start"))
            show3_start = ds_to_dt(request.form.get("show3_start"))

            # Upload image to Cloudinary and return public_id
            artist_img = request.files["artist_img"]
            if artist_img.filename.split(".")[-1].lower(
                    ) in ALLOWED_EXTENSIONS:
                upload_result = cloudinary.uploader.upload(
                    artist_img)["public_id"]
            else:
                upload_result = ""

            artist = {
                "artist_name": request.form.get("artist_name"),
                "artist_bio": request.form.get("artist_bio"),
                "artist_url": request.form.get("artist_url"),
                "artist_img": upload_result,
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
                "last_edit_on": date,
            }
            mongo.db.artists.insert_one(artist)
            flash(
                "Artist {} successfully added".format(request.form.get(
                    "artist_name"))
            )
            return redirect(url_for("artists"))

        stages = mongo.db.key_info.find_one()["stages"]
        return render_template("add_artist.html", stages=stages)

    else:

        abort(403)


@app.route("/edit_artist/<artist_id>", methods=["GET", "POST"])
def edit_artist(artist_id):

    # Check user is admin
    if "user" in session:

        artist = mongo.db.artists.find_one({"_id": ObjectId(artist_id)})

        if request.method == "POST":
            now = datetime.now()
            date = now.strftime("%d-%m-%Y")

            # Convert date strings to datetime objects
            show1_start = ds_to_dt(request.form.get("show1_start"))
            show2_start = ds_to_dt(request.form.get("show2_start"))
            show3_start = ds_to_dt(request.form.get("show3_start"))

            # Get current artist_img ID and assign it to upload_result variable
            upload_result = artist["artist_img"]

            # Upload image to Cloudinary and return public_id
            artist_img = request.files["artist_img"]
            if artist_img.filename.split(".")[-1].lower(
                    ) in ALLOWED_EXTENSIONS:
                upload_result = cloudinary.uploader.upload(
                    artist_img)["public_id"]

            edited_artist = {
                "$set": {
                    "artist_name": request.form.get("artist_name"),
                    "artist_bio": request.form.get("artist_bio"),
                    "artist_url": request.form.get("artist_url"),
                    "artist_img": upload_result,
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
                    "last_edit_on": date,
                }
            }
            mongo.db.artists.update_one({"_id": ObjectId(
                artist_id)}, edited_artist)
            flash(
                "Artist {} successfully updated".format(request.form.get(
                    "artist_name"))
            )
            return redirect(url_for("artists"))

        stages = mongo.db.key_info.find_one()["stages"]
        return render_template(
                "edit_artist.html", artist=artist, stages=stages)

    else:

        abort(403)


@app.route("/delete_artist/<artist_id>")
def delete_artist(artist_id):

    # Check user is admin
    if "user" in session:

        deleted_artist = mongo.db.artists.find_one(
            {"_id": ObjectId(artist_id)})[
            "artist_name"
        ]
        mongo.db.artists.delete_one({"_id": ObjectId(artist_id)})
        flash("Artist {} successfully deleted".format(deleted_artist))
        return redirect(url_for("artists"))

    else:

        abort(403)


@app.route("/delete_all")
def delete_all():

    # Check user is admin
    if "user" in session:

        mongo.db.artists.delete_many({})
        flash("All artists successfully deleted")
        return redirect(url_for("artists"))

    else:

        abort(403)


# Data backup and restore ----------------------------------------------------

# Backup functionality adapted from:
# https://github.com/abonello/food_nutrition/


@app.route("/backup")
def backup():

    # Check user is admin
    if "user" in session:

        # Check user is superuser
        user_is_superuser = mongo.db.admins.find_one(
            {"username": session["user"]})["is_superuser"]

        if user_is_superuser == "on":

            # Get data from database
            artists = dumps(mongo.db.artists.find())
            key_info = dumps(mongo.db.key_info.find())

            # Write data to json files
            with open("data_backup/artists_bkup.json", "w") as file:
                file.write(artists)
            with open("data_backup/key_info_bkup.json", "w") as file:
                file.write(key_info)
            flash("Database successfully backed up")
            return redirect(url_for("superuser"))

        else:
            abort(403)

    else:
        abort(403)


@app.route("/restore")
def restore():

    # Check user is admin
    if "user" in session:

        # Check user is superuser
        user_is_superuser = mongo.db.admins.find_one(
            {"username": session["user"]})["is_superuser"]

        if user_is_superuser == "on":

            artists = []
            key_info = []

            # Read data from backup json files
            with open("data_backup/artists_bkup.json", "r") as file:
                artists = loads(file.read())
            with open("data_backup/key_info_bkup.json", "r") as file:
                key_info = loads(file.read())

            # Write data to database
            artists_db = mongo.db.artists
            artists_db.drop()
            for ndx, each_artist in enumerate(artists):
                del artists[ndx]["_id"]
                artists_db.insert_one(artists[ndx])

            key_info_db = mongo.db.key_info
            key_info_db.drop()
            for ndx, each_info in enumerate(key_info):
                del key_info[ndx]["_id"]
                key_info_db.insert_one(key_info[ndx])

            flash("Database successfully restored from backup")
            return redirect(url_for("superuser"))

        else:
            abort(403)

    else:
        abort(403)


# Error handlers -------------------------------------------------------------

# Error handler code from:
# https://flask.palletsprojects.com/en/2.3.x/errorhandling/


@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html", e=e), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=False)
