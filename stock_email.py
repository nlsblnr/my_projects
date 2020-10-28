'''
This script sends the recent value of a stock, in my case it's the one of Crédit Suisse,
to my E-Mail address
'''


import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

URL = 'https://marktdaten.fuw.ch/detail/stocks/index?ID_NOTATION=100295'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

cs_box = soup.find('div', attrs={'class':'product_rate'})
cs = cs_box.text

prozentchange_box = soup.find('div', attrs={'class':'product_changePercent'})
prozentchange = prozentchange_box.text

#Zugriff durch weniger sichere Apps: https://myaccount.google.com/lesssecureapps?pli=1

print('Searching Information...')
email = 'from_email'
password = 'password'
send_to_email = 'to_email'
subject = 'Momentane Aktienkurse'
message = 'Preis einer Crédit Suisse Aktie:\n\n' + cs + 'CHF' + '\n\nVeränderung in Prozent:\n\n' + prozentchange + '\n\nhttps://marktdaten.fuw.ch/detail/stocks/index?ID_NOTATION=100295'
time.sleep(5)
print('Sending E-Mail...')
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
print('Successfully sent E-Mail!')
server.quit()