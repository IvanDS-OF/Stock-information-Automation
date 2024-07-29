# Import all the libraries needed
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from time import sleep

# Know the URL
url = 'https://acme-test.uipath.com/login'

# Specify the path to the geckodriver
gecko_service = FirefoxService(executable_path="/usr/local/bin/geckodriver")

# Initiate the instance and open Firefox
driver = webdriver.Firefox(service=gecko_service)
# Maximize Browser window
driver.maximize_window()

# Load the URL to our browser
driver.get(url)

# Wait some time to see the process
sleep(10)
