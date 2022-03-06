import smtplib
from secrets import EMAIL_ADR, EMAIL_PASS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import ctime, sleep
def notify(message):
    mail_content = """Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You
    """
    mail_content = message
    #The mail addresses and password
    sender_address = EMAIL_ADR
    sender_pass = EMAIL_PASS
    #send to myself
    receiver_address = EMAIL_ADR
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = f'{ctime()} - A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    sleep(10)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    sleep(50)
    session.quit()
    #print('Mail Sent')