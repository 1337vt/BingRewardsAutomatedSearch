from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from string import ascii_letters, digits
from random import choice
from selenium.webdriver.edge.options import Options
import time
from msedge.selenium_tools import Edge, EdgeOptions  
import os

options = EdgeOptions()
directory = os.getenv('LOCALAPPDATA')

driver = Edge(executable_path = directory + r"\Tools\SeleniumDriver\msedgedriver.exe",options = options)  
driver.get("http://www.bing.com")
time.sleep(5)
i=40
while i > 0:
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(''.join([choice(ascii_letters + digits) for i in range(32)]))
    elem.send_keys(Keys.RETURN)
    i-=1
    time.sleep(0.5)   
driver.close()
 
# Phase 2.  The 
options.use_chromium = True  
mobile_emulation = {"userAgent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"}
options.add_experimental_option("mobileEmulation", mobile_emulation)  
driver = Edge(executable_path = directory + r"\Tools\SeleniumDriver\msedgedriver.exe",options = options)  
driver.get("http://www.bing.com")

time.sleep(4)
hamburger = driver.find_element(By.ID, "mHamburger")
hamburger.send_keys(Keys.RETURN)
time.sleep(1)
sign_in = driver.find_element(By.ID, "hb_s")
sign_in.click()
time.sleep(1)
i=40
while i > 0:
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(''.join([choice(ascii_letters + digits) for i in range(32)]))
    elem.send_keys(Keys.RETURN)
    i-=1
    time.sleep(0.5)

driver.close()
