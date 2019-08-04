# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 23:02:51 2019

@author: satya
"""

import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.amazon.in/Passport-Portable-External-Drive-Black/dp/B01LQQH86A/ref=sr_1_1_sspa?keywords=portable+hard+disk&qid=1564682006&s=gateway&sr=8-1-spons&psc=1"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,"html.parser")
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=price[2:7]
    c_price=converted_price.replace(",","")
    print(c_price)
    c_p=int(c_price)
    if (int(c_p)<9000):
        send_email()
    
def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('satyaajeet.gmail.com','otxybjftfznmueky')
    print("ok")
    subject="Price Fell Down!"
    Body = "Check link https://www.amazon.in/Passport-Portable-External-Drive-Black/dp/B01LQQH86A/ref=sr_1_1_sspa?keywords=portable+hard+disk&qid=1564682006&s=gateway&sr=8-1-spons&psc=1"
    msg=f'Subject: {subject}\n\n{Body}'
    
    server.sendmail('satyaajeet@gmail.com',msg)
    print("Email has been sent")
    
    server.quit()
    
check_price()
    
