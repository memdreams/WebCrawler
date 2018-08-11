# Capture the OINP website updating and send the massage to my email address
# 2018.06.29
# refer to https://chrisalbon.com/python/web_scraping/monitor_a_website/


# -*-coding:utf8-*- #


import requests  # to download the page
from bs4 import BeautifulSoup  # to parse what we download

import time  # to add a delay between the times the scape runs

import smtplib  # to allow us to email


# This script downloads the homepage of sth, and if it finds the text, email me.
# If it does not find some text, it waits 60 seconds and downloads the website again.
while True:
    # set the url:
    url = "http://www.ontarioimmigration.ca/en/pnp/OI_PNPNEW.html" #"http://Google.com/"#Mac+OS+X/10.13.5 (17F77) CalendarAgent/399.2.2
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15'}
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word "Google" occurs on the page is less than 1,
    # if the number of times the word "Aug" occurs on the page is less than 1,
    findStr = "Augrr`"
    if str(soup).find(findStr) == -1:
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with just a subject line,
        msg = 'Subject: This is Jie\'s script talking, CHECK Date Modified!'
        # set the 'from' address,
        fromaddr = 'memdreams@gmail.com'
        # set the 'to' addresses,
        toaddrs = ['memdreams@me.com', 'jmeng008@uottawa.ca', 'A_THIRD_EMAIL_ADDRESS']

        # setup the email server,
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        # add my account login name and password,
        # server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        # server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        # server.quit()

        break










