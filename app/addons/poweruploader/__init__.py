from flask import Blueprint

bp = Blueprint("poweruploader", __name__)

from app.addons.poweruploader import routes