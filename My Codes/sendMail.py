import smtplib

def send_email(sender_mail,receiver_mail,subject,message):
    smtp_server = "smtp.gmail.com"
    port = 587  # or the appropriate port for your email provider
    username = "2018pietcslokendra82@poornima.org"
    password = "pietlucky99"

    # Create a secure connection to the SMTP server
    server = smtplib.SMTP(smtp_server,port)
    server.starttls()
    server.login(username,password)

    # Compose the email
    email_body= f"Subject:{subject}\n\n{message}"

    # Send the email
    server.sendmail(sender_mail,receiver_mail,email_body)

    # Close the connection
    server.quit()

# Usage example:
    # sender_mail = "2018pietcslokendra82@poornima.org"
    # receiver_mail = "manish.s@mygetepay.com"
    # subject = "Check Kar"
    # message = "hey Manish it's a test mail By Lucky"
    
send_email("2018pietcslokendra82@poornima.org","aks16254ee2016@gmail.com","Check Kar","hello...it's a test mail By Lucky")

