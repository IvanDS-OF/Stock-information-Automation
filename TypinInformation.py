#Now we will type information using the Library Selenium
#We can type information within a form or we can text an specific message and send it

#Import all the libraries needed: 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#Know th URL, in this case it will be Whasap
url = 'https://acme-test.uipath.com/login'

#Iniciate the instance and open Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Maximize Browser window
driver.maximize_window()

#Load the URL to our browser
driver.get(url)


#we will type information in a portal to login us
#To type information we need the XPath of the text box in the next sentence
Email = driver.find_element(By.XPATH, '//*[@id="email"]') #Locate the text box
Email.send_keys("ivan_hds11@hotmail.com")   #Text type

#Do the same with the pass
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('Inicio..12345')


#Finnaly, press LogIn Button
#/html/body/div/div[2]/div/div/div/form/button
LogInButton = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/form/button')
LogInButton.click()


#It is recommedable to wait some time to see the process
sleep(10)


#Finally close the application
driver.quit()
