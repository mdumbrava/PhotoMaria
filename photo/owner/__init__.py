""" This package owner Page app """
from flask import Blueprint

bp = Blueprint('owner', __name__, url_prefix='/')

from . import routes