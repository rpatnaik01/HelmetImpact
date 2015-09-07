import smtplib
import string

def notify(toaddrs,player,force):

   # Specifying the from and to addresses

   fromaddr = 'impact.notification@gmail.com'


   # Writing the message (this message will appear in the email)

   SUBJECT = "HIGH MAGNITUDE IMPACT!"

   TEXT = """Your player, %s, has just suffered a high magnitude impact!
   The Intel Edison's Impact System has recorded %f g's of Force on impact.
   Please monitor %s for any concussive symptoms.""" % (player,force,player)
   
   msg =string.join((
   "From: %s" % fromaddr,
   "To: %s" % ", ".join(toaddrs),
   "Subject: %s" % SUBJECT,
   "",
   TEXT
   ), "\r\n")

   # Gmail Login

   username = 'impact.notification'
   password = 'NinRakEmail'

   # Sending the mail  

   server = smtplib.SMTP('smtp.gmail.com:587')
   server.starttls()
   server.login(username,password)
   server.sendmail(fromaddr, toaddrs, msg)
   server.quit()
