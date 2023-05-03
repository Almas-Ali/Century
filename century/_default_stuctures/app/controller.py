from flask import render_template
from century import settings

app = settings.app

@app.route("/")
def home():
    return render_template("index.html")