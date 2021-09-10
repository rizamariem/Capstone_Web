import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("rizamarie46@gmail.com", "TPSNSiuw2lfiWHTIDcutiechanak44cutiechanak44")
server.sendmail("rizamarie46@gmail.com", "russazziarnado@gmail.com", "Please click the link to confirm")

server.quit()