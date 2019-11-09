import schedule
import time
import smtplib, ssl

def job():
  

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "usamawizard@gamil.com"
	receiver_email ="usamawizard@gamil.com"
	password = "0usamaisacomputerwizard"
	message = """\
	Subject: Hi there

	This message is sent from Python."""

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

schedule.every(0.5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)