# This file contains custom error pages

from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    # Make sure failed db sessions do not cause issues
    db.session.rollback()
    return render_template('500.html'), 500