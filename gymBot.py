from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
usernameStr = os.getenv('usernameStr')
passwordStr = os.getenv('passwordStr')
timeSlot = 13
now = datetime.now()
refreshTime = now.replace(hour=19, minute=0, second=0, microsecond=0)

# Open Crunch Website
browser = webdriver.Chrome()
browser.get(('https://members.crunchfitness.ca/members/sign_in'))

# Fill in Username and Password and Click Login
username = browser.find_element_by_id('login-email')
username.send_keys(usernameStr)

password = browser.find_element_by_id('login-password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_name('commit')
signInButton.click()

# Wait For Transition Then Click on My Classes

MyClasses = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div/ul/li[3]/a')))
MyClasses.click()

# Wait For Clock to Hit The Hour and Then Refresh
while now < refreshTime:
    time.sleep(0.5)
    now = datetime.now()

time.sleep(0.1)
browser.refresh()
time.sleep(0.5)

# Click On Current Day
CurrentDay = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div/section[2]/div[2]/div[1]/ul/li[2]')))
CurrentDay.click()

# Click Reserve Button
reserve = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div/section[2]/div[2]/div[2]/div[' + str(timeSlot) + ']/div[3]/div/a/span')))
reserve.click()