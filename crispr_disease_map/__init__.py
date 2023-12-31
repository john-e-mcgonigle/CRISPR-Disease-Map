from typing import Type

from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)


from crispr_disease_map import routes, models