import os
from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
CORS(app)

from backend.app import views
from backend.app.controller import user_handler
