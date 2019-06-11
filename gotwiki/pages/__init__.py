from flask import Blueprint, g, redirect, render_template, request, session, url_for

pages = Blueprint(
    'pages',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes