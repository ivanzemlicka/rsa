from flask import Flask  # type: ignore
from config import Config
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
