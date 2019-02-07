
import smtplib

def sendMail():
    gmail_user = 'tiago.cnorberto@pbh.gov.br'  
    gmail_password = "PBH*2510"

    sent_from = gmail_user  
    to = ['tiago.cnorberto@pbh.gov.br']
    subject = "OMG Super Important Message"
    body = "Hey, whats up?\n\n- You"

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:  
        server = smtplib.SMTP_SSL('10.0.25.19', 587)
        
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ("Email sent")
    except Exception as e:
        print(str(e))  
        print ("Something went wrong")



sendMail()