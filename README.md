**Python + Flask Website** following [Miguel Grinberg's tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

![Homepage screenshot](screenshot-homepage.png?raw-true "Homepage Screenshot")

**Uses:**
- Python 3
  - aiosmtpd
  - pyjwt
- JavaScript
  - Moment.js
- Flask
  - Flask-SQLAlchemy
  - Flask-Migrate
  - Flask-Login
  - Flask-Mail
  - Flask-Moment
- Jinja
- WTForms
- SQLAlchemy
- Alembic
- Bootstrap

**Notes:**
- Use "flask run" to start the server on http://localhost:5000.
- Use 'python tests.py' to run the unit tests.
- Use "venv\scripts\activate" to activate virtual Python environment.
- Set "FLASK_DEBUG" variable to 1 before running to enable debugging mode.
- To enable local email server for errors:
	- pip install aiosmtpd
	- (in second terminal)
		- aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
	- (in original terminal) 
		- set MAIL_SERVER=localhost
		- set MAIL_PORT=8025
- Application includes separate blueprints for these submodules:
  - errors
  - auth