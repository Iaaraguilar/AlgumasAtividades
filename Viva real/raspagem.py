from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import TimeoutException
chrome_driver= r'C:\Program Files\chromedriver-win64\chromedriver.exe' 
service=Service(chrome_driver)
options=webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")