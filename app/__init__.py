from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app config file
from config import Config

# create the application instance
app = Flask(__name__)
app.config.from_object(Config)

# create the application database instance
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

@app.route('/')
def bienvenida():
    return "Bienvenido a la vitrina web del CBC"

from app.controllers import categoria, producto
from app.models import categorias, productos