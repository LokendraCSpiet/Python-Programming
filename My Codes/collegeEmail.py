import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
print('opening mail')
server.starttls()
server.login('2018pietcslokendra82@poornima.org','pietlucky99')
print('logged in successfully')
msg="Hello !!!"
print('preparing mail')
server.sendmail('2018pietcslokendra82@poornima.org','abhishar9057@gmail.com',msg)
print('sending mail')
server.quit()
print('logged out')