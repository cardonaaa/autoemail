import smtplib

username = ''
password = ''
fromaddr = ''

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username,password)

file = open('model-list.txt')
for line in file:
	line = ' '.join(line.split())
	temp = line.split(' ')
	name = temp[0]
	toaddr = temp[1]
	date = temp[2]
	msg = "\r\n".join([
  		"From: ".join(fromaddr),
  		"To: ".join(toaddr),
  		"Subject: OTL Modeling Times",
  		"",
  		"Hi %s, \n\n\tWe have scheduled you to model on %s. Please let me know if this date works for you! \n\nThanks!\nKathleen" % (name, date)
  		])
	server.sendmail(fromaddr, toaddr, msg)

file.close()
server.quit()