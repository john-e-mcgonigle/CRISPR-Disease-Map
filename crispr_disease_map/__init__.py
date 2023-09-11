from typing import Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from crispr_disease_map import routes, models


def create_app_instance(config_class: Type[Config] = Config) -> Flask:
    """
    A function to creat a Flask app instance to avoid the issues that come with global declaration of a web app and
    support a factory design pattern approach.

    :param config_class: A config class tasked with loading the Flask specific variables

    :return: A Flask web app.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    return app

