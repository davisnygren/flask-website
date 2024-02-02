Python Flask Website following https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Uses:
    - Python 3
	  - aiosmtpd
    - Flask
	  - Flask-SQLAlchemy
	  - Flask-Migrate
	  - Flask-Login
    - Jinja
    - WTForms
	- SQLAlchemy
	- Alembic
	
- Use "flask run" to start the server on http://localhost:5000.
- Use "venv\scripts\activate" to activate virtual Python environment.
- Set "FLASK_DEBUG" variable to 1 before running to enable debugging mode.
- To enable local email server for errors:
	- pip install aiosmtpd
	- aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025