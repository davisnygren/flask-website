# General email sending functions
from flask_mail import Message
from flask import render_template
from app import app, mail
from threading import Thread

# Send an email asynchronously
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Build an email message and send it
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()