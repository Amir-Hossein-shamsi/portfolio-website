import streamlit as st
import re
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Configuration from environment variables
load_dotenv()
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
EMAIL_USER = os.getenv('EMAIL_USER')  # Your email address
APP_PASSWORD = os.getenv('APP_PASSWORD')   # Your email password/app password
TO_EMAIL = os.getenv('TO_EMAIL')

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def send_email(name, sender_email, message):
    """Send email using SMTP with proper formatting"""
    try:
        msg = MIMEText(f"Name: {name}\nEmail: {sender_email}\nMessage: {message}")
        msg['Subject'] = f"New message from {name}"
        msg['From'] = EMAIL_USER
        msg['To'] = TO_EMAIL

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:  # Use SSL port
            server.login(EMAIL_USER, APP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Auth Error: {str(e)}")
        return False

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            validation_passed = True
    
            if not name:
                st.error("Please provide your name.", icon="🧑")
                validation_passed = False
            if not email:
                st.error("Please provide your email address.", icon="📨")
                validation_passed = False
            elif not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="📧")
                validation_passed = False
            if not message:
                st.error("Please provide a message.", icon="💬")
                validation_passed = False
                
            if not validation_passed:
                st.stop()  # Stop execution if validation fails
                
            try:
                if send_email(name, email, message):
                    st.success("Your message has been sent successfully! 🎉", icon="🚀")
                else:
                    st.error("Failed to send message. Please try again later.", icon="😨")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")

