from email.message import EmailMessage
import ssl
import smtplib

senderEmail = '' #put your sender mail
senderPassword = '' #put your generated password

emailSubject = 'Test My Code'

emailBody = """ Work Hard and DO your best walid """

recevierEmail = 'walidomar291@gmail.com'

email = EmailMessage()

email['From'] = senderEmail
email['To'] = recevierEmail
email['Subject'] = emailSubject
email.set_content(emailBody)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context= context) as smtp:
    smtp.login(senderEmail, senderPassword)
    smtp.sendmail(senderEmail, recevierEmail, email.as_string())
    
    
    