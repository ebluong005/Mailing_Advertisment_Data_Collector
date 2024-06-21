import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def log_message(message):
    logging.basicConfig(filename='zillow_scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(message)

def send_email(subject, body):
    sender_email = 'youremail@example.com'
    receiver_email = 'recipient@example.com'
    password = 'yourpassword'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        log_message('Email sent successfully')
    except Exception as e:
        log_message(f'Failed to send email: {e}')
