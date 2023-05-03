from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_marshmallow import Marshmallow

from century import settings

models = settings.models 

class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(80), unique=True)
    email = models.Column(models.String, unique=True)
    password = models.Column(models.String, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'
