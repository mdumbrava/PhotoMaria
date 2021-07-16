""" This package gallery Page app """
from flask import Blueprint

bp = Blueprint('gallery', __name__, url_prefix='/')

from . import routes