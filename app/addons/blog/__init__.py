from flask import Blueprint

bp = Blueprint("blog", __name__)

from app.addons.blog import routes