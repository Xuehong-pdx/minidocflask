import smtplib

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Or 465 for SSL
        server.ehlo()
        server.starttls()
        server.ehlo()  # Crucial: Call ehlo again after starttls
        server.login("your_test_email@gmail.com", "your_app_password")  # Use app password!
        print("Login successful!")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check app password and credentials.")
except smtplib.SMTPException as e:  # Catch other SMTP errors
    print(f"SMTP error: {e}")
except Exception as e:  # Catch general exceptions
    print(f"An error occurred: {e}")