from sys import platform

from backend.app import app
from backend.app.models import db

if __name__ == "__main__":
    db.create_all()
    app.run()
