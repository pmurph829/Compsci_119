import smtplib as s

From = "Peter J. Murphy <petjmurphy@umass.edu>"
To = "literacy@cs.umass.edu"
Subject = "Please give me points"

Text = """
Please give me some points
for making a program
to send email.

(signed) Peter J. Murphy"""

Message = "From: " + From        + "\r\n"  + \
          "To: " + To            + "\r\n"  + \
          "Subject: " + Subject  + "\r\n"  + \
          Text

print(Message)

Server = s.SMTP('localhost')

Code = Server.sendmail(From,[To], Message)
Server.quit()
