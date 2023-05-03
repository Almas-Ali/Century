from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from pathlib import Path
import os

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the environment variables
load_dotenv(BASE_DIR / ".env")


# create the app
app = Flask(
    import_name="controller",
    template_folder=os.path.join(BASE_DIR, "views/"),
    static_folder=os.path.join(BASE_DIR, "static/"),
    static_url_path="/static",
)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")

# Database settings
# create the extension
models = SQLAlchemy()

# initialize the app with the extension
models.init_app(app)


# Server settings
DEBUG = os.getenv("DEBUG")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
