# Import all the libraries needed
from selenium import webdriver
#In this case we will be using CHrome because we are using a Raspberry
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from time import sleep


browserDriver = Service('/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=browserDriver)

driver.get('https://acme-test.uipath.com/login')


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




#From here we can Start the project using objects


