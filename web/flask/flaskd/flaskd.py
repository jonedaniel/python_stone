from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from web.flask.flaskd.databse import db_session
from web.flask.flaskd.models import *

app = Flask(__name__)
app.config.from_object(__name__)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/users")
def users():
    users = db_session.query(User).all()
    return render_template("users.html", users=users)


if __name__ == '__main__':
    app.run()
