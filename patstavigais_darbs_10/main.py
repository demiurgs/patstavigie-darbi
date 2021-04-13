import flask
from user import User

application = flask.Flask(__name__)

user_list = []


@application.route("/")
def index():
    return flask.render_template("index.html", users=user_list)


@application.route("/add_user", methods=["GET", "POST"])
def add_visit():

    if flask.request.method == "POST":
        name = flask.request.form["name"]
        email = flask.request.form["email"]

        user = User(username=name, email=email)
        user_list.append(user)

        return flask.render_template("user.html",
                                     user=user)

    return flask.render_template("form.html")


application.run()