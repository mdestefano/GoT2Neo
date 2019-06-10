from flask import Blueprint, g, redirect, render_template, request, session, url_for

houses = Blueprint(
    'houses',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes