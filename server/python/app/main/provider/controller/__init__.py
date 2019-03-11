from flask import Blueprint

api = Blueprint('api', __name__)

from . import article_controller, other_controller, tag_controller, comment_controller
