from datetime import datetime
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
