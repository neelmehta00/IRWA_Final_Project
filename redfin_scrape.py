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

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def get_redfin_csv(address):
    browser = webdriver.Chrome(options=options, executable_path='/Users/neelmehta/Downloads/chromedriver 9')
    browser.get(address)
    time.sleep(6)
    csv = browser.find_element(By.XPATH, '//*[@id="download-and-save"]')
    time.sleep(6)
    csv.click()
    time.sleep(6)
city_code = "1073"  # PLEASE ENTER CITY CODE HERE
city = "Baltimore" # PLEASE ENTER CITY HERE
state_abbrev = "MD" # PLEASE ENTER STATE ABBREV. HERE
bed_list = ["0", "1", "2", "3", "4", "5"]
year_built_list = [["1900", "1960"], ["1960", "1980"], ["1980", "2000"], ["2000", "2010"], ["2010", "2022"]]
for bed in bed_list:
    for years in year_built_list:
        link = "https://www.redfin.com/city/"+city_code+"/"+state_abbrev+"/" + city+ "/filter/property-type=house+condo+townhouse+multifamily,min-beds=" \
               + bed + ",max-beds=" + bed + ",min-year-built=" + years[0] + ",max-year-built=" + years[1] + ",include=sold-2yr"
        try:
            get_redfin_csv(link)
        except:
            print("Could not fine matching data!")
