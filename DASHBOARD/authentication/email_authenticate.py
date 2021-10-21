import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("rizamarie46@gmail.com", "")
server.sendmail("rizamarie46@gmail.com", "russazziarnado@gmail.com", "Please click the link to confirm")

server.quit()