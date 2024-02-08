# This file contains custom error pages

from flask import render_template
from app import app, db
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    # Make sure failed db sessions do not cause issues
    db.session.rollback()
    return render_template('errors/500.html'), 500