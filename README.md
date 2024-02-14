**Python + Flask Website** following [Miguel Grinberg's tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

**Index page:**

![Homepage screenshot](screenshots/screenshot-homepage.jpg?raw-true "Homepage Screenshot")

**Profile page:**

![Profile page screenshot](screenshots/screenshot-profile.jpg?raw-true "Profile page Screenshot")

**Search page:**

![Search page screenshot](screenshots/screenshot-search.jpg?raw-true "Search page Screenshot")

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
- Elasticsearch (via Docker)

**Notes:**
- Use "flask run" to start the server on http://localhost:5000.
  - Elasticsearch Docker container must be started to search or commit to the db.
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
  - Error Handling (errors)
  - Authentication (auth)
  - Main Functionality (main)
- For security, the ".env" file is not included in the repository and must be
  created manually.
- Virtual environment can be set up with "pip install -r requirements.txt"
- Venv setup file can be updated with "pip freeze > requirements.txt"