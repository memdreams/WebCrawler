# Capture the OINP website updating and send the massage to my email address
# 2018.07.18


# -*-coding:utf-8-*-

import requests
from lxml import html
import smtplib
from email.mime.text import MIMEText
import time

cookie = {}

raw_cookies = ''

# for line in raw_cookies.split(';'):
#     key, value = line.split("=", 1)
#     cookie[key] = value

url = "http://www.ontarioimmigration.ca/en/pnp/OI_PNPNEW.html"

while True:
    page = requests.get(url, cookies=cookie)

    tree = html.fromstring(page.text)

    # XPath resolution
    intro_raw = tree.xpath('//p/strong/span[@style=" text-decoration: underline;"]/text()')

    # print(intro_raw[0])

    cmp_str = 'July 27, 2018'
    if cmp_str != intro_raw[0]:
        # if changed, notify me!
        # setup send mailbox
        mail_host = 'smtp.gmail.com'
        mail_user = 'memdreams'
        mail_pass = 'mengying'
        sender = 'memdreams@gmail.com'
        receivers = ['memdreams@me.com', 'leeyimm@me.com']

        # setup email information
        body = cmp_str + '\n' + url
        message = MIMEText(body, 'plain', 'utf-8')
        message['Subject'] = 'PNP Info Changed!'
        message['Body'] = cmp_str
        message['From'] = sender
        message['To'] = receivers[0]

        # log in and send email
        try:
            # smtpObj = smtplib.SMTP(mail_host, 587) # not secure enough, 587 is the port for gmail
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.ehlo()
            # smtpObj.starttls()
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            smtpObj.quit()
            print('success')

        except smtplib.SMTPException as e:
            print('error:', e)

    else:
        time.sleep(900)







