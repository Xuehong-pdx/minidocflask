from flask import Flask
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))  
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') 
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS').lower() == 'true' 
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  

mail = Mail(app)

@app.route('/')
def send():
    recipients = [os.getenv('RECIPIENTS')]
    msg = Message(
        subject='Hello from the other side!',
        sender=os.environ.get('MAIL_USERNAME') ,
        recipients=recipients
    )
    msg.body = "This is a test email sent from a Flask container."
    try:
        with app.app_context():  
            mail.send(msg)
        return "Message sent!"
    except Exception as e:
        return f"Error sending email: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
