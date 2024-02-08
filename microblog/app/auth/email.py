# Authentication-specific email functions
from flask import render_template
from app import app
from app.email import send_email

# Send an email prompting a user to reset their password
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.txt',
                                         user=user, token=token))