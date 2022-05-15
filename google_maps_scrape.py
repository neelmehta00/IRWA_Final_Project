#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
DRIVER_PATH = '/Users/neelmehta/Downloads/chromedriver 9'
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
listad = []
def getad(address):
    browser = webdriver.Chrome(options=options,executable_path='/Users/neelmehta/Downloads/chromedriver 9')
    browser.get(address)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hello = browser.find_elements(By.CLASS_NAME, "dbg0pd")
    for element in hello:
        finalad = ""
        element.click()
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        time.sleep(2)
        try:
            address = soup.find("span" , {"class": "LrzXr"})
            address = address.get_text()
            for ch in address:
                if ch != ",":
                    finalad = finalad + ch
            listad.append(finalad)
        except:
            print("missing")

def secpage(address):
    browser = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
    browser.get(address)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hello = browser.find_elements(By.CLASS_NAME, "dbg0pd")
    for element in hello:
        finalad = ""
        element.click()
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        time.sleep(2)
        try:
            address = soup.find("span" , {"class": "LrzXr"})
            address = address.get_text()
            for ch in address:
                if ch != ",":
                    finalad = finalad + ch
            listad.append(finalad)
        except:
            print("missing")
def thirdpage(address):
    browser = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
    browser.get(address)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hello = browser.find_elements(By.CLASS_NAME, "dbg0pd")
    for element in hello:
        finalad = ""
        element.click()
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        time.sleep(2)
        try:
            address = soup.find("span" , {"class": "LrzXr"})
            address = address.get_text()
            for ch in address:
                if ch != ",":
                    finalad = finalad + ch
            listad.append(finalad)
        except:
            print("missing")
def fourpage(address):
    browser = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
    browser.get(address)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hello = browser.find_elements(By.CLASS_NAME, "dbg0pd")
    for element in hello:
        finalad = ""
        element.click()
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        time.sleep(2)
        try:
            address = soup.find("span" , {"class": "LrzXr"})
            address = address.get_text()
            for ch in address:
                if ch != ",":
                    finalad = finalad + ch
            listad.append(finalad)
        except:
            print("missing")
def fivepage(address):
    browser = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
    browser.get(address)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    nextli = browser.find_element(By.CSS_SELECTOR, "span[style='display:block;margin-left:53px']")
    nextli.click()
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hello = browser.find_elements(By.CLASS_NAME, "dbg0pd")
    for element in hello:
        finalad = ""
        element.click()
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        time.sleep(2)
        try:
            address = soup.find("span" , {"class": "LrzXr"})
            address = address.get_text()
            for ch in address:
                if ch != ",":
                    finalad = finalad + ch
            listad.append(finalad)
        except:
            print("missing")
'''
1) Go to google.com/maps
2) type in city + POINT OF INTEREST (ie. parks in Baltimore)
3) Copy url
4) Paste below.
5) Run scraper
'''
park_link = "https://www.google.com/search?q=parks+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1420&bih=744&sz=0&tbm=lcl&sxsrf=ALiCzsY3DXVkDHgLhmx8IrH_ReYS6wePcA%3A1652312888350&ei=OEt8YoGJFemxptQPgdCHoAQ&oq=parks+in+baltimore&gs_l=psy-ab.3...0.0.0.3132.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.VzI72WAJZsU#rlfi=hd:;si:;mv:[[39.348756099999996,-76.56834429999999],[39.2666258,-76.6568415]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:1"
grocery_link = "https://www.google.com/search?q=grocery+stores+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1720&bih=1304&sz=0&tbm=lcl&sxsrf=ALiCzsbCQrdtPuQKUEBed5abKz75pskS-Q%3A1652327797692&ei=dYV8Yo34KfXqtQbK3ZeYDA&oq=gr+in+baltimore&gs_l=psy-ab.3.0.0i7i30k1l10.8428.8523.0.10426.2.2.0.0.0.0.117.117.0j1.1.0....0...1c.1.64.psy-ab..1.1.117....0.6XtMiFREmIg#rlfi=hd:;si:;mv:[[39.3785226,-76.5385469],[39.277184299999995,-76.6561444]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10"
fast_food_link = "https://www.google.com/search?q=fast+food+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1720&bih=1304&sz=0&tbm=lcl&sxsrf=ALiCzsbe-Ao9R0yWjk0qeBPyRgiuuVweWA%3A1652327809124&ei=gYV8YoSfB5PbtAavpobwCg&oq=fast+food+in+baltimore&gs_l=psy-ab.3..0i512k1j0i7i30k1l6j0i8i30k1l2j38.111324.112744.0.113020.9.9.0.0.0.0.113.827.3j5.8.0....0...1c.1.64.psy-ab..1.8.826...0i13k1j0i8i7i30k1j0i390k1.0.uOM8RvJi3JI#rlfi=hd:;si:;mv:[[39.362761899999995,-76.5467736],[39.273092999999996,-76.7141723]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u5!2m2!5m1!1sgcid_3american_1restaurant!1m4!1u5!2m2!5m1!1sgcid_3hamburger_1restaurant!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!1m4!1u22!2m2!21m1!1e1!2m1!1e2!2m1!1e5!2m1!1e1!2m1!1e3!3sIAEqAlVT,lf:1,lf_ui:9"
gas_link = "https://www.google.com/search?q=gas+stations+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1720&bih=1304&sz=0&tbm=lcl&sxsrf=ALiCzsYq-URPNqCWEZQgrCR6MPbiTa0tQg%3A1652328028876&ei=XIZ8YvGYNZDbtAal5pjABg&oq=gas+stations+in+baltimore&gs_l=psy-ab.3..0i512k1l2j0i7i30k1l2j0i30k1j0i5i30k1l5.6200.6200.0.6662.1.1.0.0.0.0.111.111.0j1.1.0....0...1c.1.64.psy-ab..0.1.111....0.RStMMk6Lrjs#rlfi=hd:;si:;mv:[[39.362718199999996,-76.5851346],[39.2801877,-76.671736]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:3"
hotel_link = "https://www.google.com/search?q=hotels+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1720&bih=1304&sz=0&tbm=lcl&sxsrf=ALiCzsaIg2gxu2mlxpoC8wQSGuXn88cEiQ%3A1652328097532&ei=oYZ8YsT6H9vRtAaP7pIw&oq=hotels+in+baltimore&gs_l=psy-ab.3...0.0.0.101900.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.7mHfVVrRBfA#rlfi=hd:;si:;mv:[[39.359573100000006,-76.61143349999999],[39.2782969,-76.6485515]];tbs:lrf:!1m4!1u13!2m2!13m1!1b1!1m4!1u7!2m2!7m1!4e1!1m4!1u2!2m2!2m1!1e1!1m4!1u10!2m2!11m1!1e6!1m4!1u10!2m2!11m1!1e4!1m4!1u10!2m2!11m1!1e9!1m4!1u10!2m2!11m1!1e8!1m4!1u10!2m2!11m1!1e10!1m4!1u10!2m2!11m1!1e2!1m4!1u10!2m2!11m1!1e1!1m4!1u10!2m2!11m1!1e3!1m4!1u10!2m2!11m1!1e7!1m4!1u4!2m2!4m1!2e1!2m1!1e2!2m7!1e17!4m2!17m1!1e3!4m2!17m1!1e8!3sIAE,lf:1,lf_ui:6"
hospital_link = "https://www.google.com/search?q=hospitals+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1720&bih=1304&sz=0&tbm=lcl&sxsrf=ALiCzsZBKWUxeZHw9Hbxqs75uUlDr9-VmA%3A1652328200950&ei=CId8YpHIOf-E9PwPxrmByAo&oq=hospitals+in+baltimore&gs_l=psy-ab.3..0i512k1l8j0i7i30k1l2.35663.41228.0.41476.8.8.0.0.0.0.138.834.4j4.8.0....0...1c.1.64.psy-ab..2.6.650...0i13k1.0.S4JIlbMalfs#rlfi=hd:;si:;mv:[[39.4003655,-76.5323107],[39.2433726,-76.680156]];tbs:lrf:!1m4!1u45!2m2!46m1!1e1!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
whole_traders_link = "https://www.google.com/search?q=whole+foods+or+trader+joes+in+baltimore&rlz=1C5CHFA_enUS863US863&biw=1720&bih=1304&sz=0&tbm=lcl&sxsrf=ALiCzsb46yrdjcAzWCTiPRrZtSdXMpSOEw%3A1652328310657&ei=dod8YrHdJ8m0tQausJeoAw&oq=whole+foods+or+trader+joes+in+baltimore&gs_l=psy-ab.3...27669.29912.0.30182.15.15.0.0.0.0.123.1415.12j3.15.0....0...1c.1.64.psy-ab..0.5.520...38j0i67k1j0i512k1j0i7i30k1j0i5i30k1j0i546k1j33i10k1.0.sMmW8vI1JpQ#rlfi=hd:;si:;mv:[[39.4475668,-76.50025029999999],[38.774732,-77.2467803]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4"

# Uncomment for which page you want in the Google Maps results
link = park_link
getad(link)
#secpage(link)
#thirdpage(link)
#fourpage(link)
#fivepage(link)
print(listad)

filename = "Non_Traditional_Factors_CSV/Baltimore_Whole_Traders_testeerer.csv"
f = open(filename, "w")
headers = "Address\n"
f.write(headers)
for x in range(len(listad)):
    finalad = ""
    f.write(listad[x])
    f.write("\n")
f.close()

