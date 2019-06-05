from flask import Blueprint

houses = Blueprint(
    'houses',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes