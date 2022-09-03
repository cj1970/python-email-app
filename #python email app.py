#python email app

#go over to our gmail account and setup 2 factor authentification
#generate password
#create function to send mail

from email.message import EmailMessage
from app2 import password


email_sender = "jc770679@gmail.com"
email_password = password

email_reciever = ''

subject = "Hey there"
body = """ There's a lot going on here!"""

em = EmailMessage()

em['From'] = email_sender

em['To'] = email_reciever

em['Subject'] = subject




