import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('mycourseitcp@gmail.com','Here passward send by google')
try:
    subject="important message"
    body="Hello my bst friend gogo"
    message= 'subject:{}\n\n{}'.format(subject,body)
    server.sendmail('mycourseitcp@gmail.com','haronhager19@gmail.com',message)
    print('success')
except Exception as e:
    print('failed',e)