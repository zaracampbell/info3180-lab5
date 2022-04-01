from flask import Flask
from .config import Config

app = Flask(__name__, static_folder='../dist/assets')
app.config.from_object(Config)

from app import views