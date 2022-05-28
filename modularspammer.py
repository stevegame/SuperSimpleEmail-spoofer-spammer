import smtplib
mail_users = input("Mail para: ")
sent_from = input("enviado de: ")
mail_server = input("server: ")
count = 0
to = [mail_users]
subject = "Ape Vibes to you"
body = "Sus Among US body"
message = (f"""From: From Impostor From AMong Us <{sent_from}>
To: To Person <{mail_users}>
Subject: Sus Mail

U be like
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
""")

while True:
      smtpObj = smtplib.SMTP(mail_server)
      smtpObj.sendmail(sent_from, to, message)         
      print("Successfully sent email")
if smtplib.SMTPException:
   print("Error: unable to send email")
