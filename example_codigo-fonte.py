# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:55:08 2021

@author: adam_
"""

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.nba.com/stats/players/traditional/?sort=PLAYER_NAME&dir=1"

options = Options()
options.headless = True
driver = webdriver.Chrome()

driver.get(url)
time.sleep(5)

driver.find_element_by_xpath(
    '//div[@class="banner-actions-container"]//button[@id="onetrust-accept-btn-handler"]'
    ).click()

time.sleep(1)

driver.find_element_by_xpath(
    '//div[@class="nba-stat-table"]//div[@class="nba-stat-table__overflow"]//table//thead//tr//th[@data-field="PTS"]'
    ).click()

element = driver.find_element_by_xpath('//div[@class="nba-stat-table"]//div[@class="nba-stat-table__overflow"]//table')
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')


df_full = pd.read_html(str(table))[0].head(10)

df = df_full[['Unnamed: 0','PLAYER','TEAM','PTS']]
df.columns = ['pos','player','team','total']

print(df)

driver.quit()
