##This code is to join all the infroamtion and the previous programs
#THat now enable me to create the final project

#Attampt 1

#Libraries needed

import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

from bs4 import BeautifulSoup
from time import sleep


#Now we will create the functions that will define the 
#structure of the project


#Define some globl and important variables
urlStock = "https://www.google.com/finance/quote/USD-MXN?sa=X&ved=2ahUKEwiarpWnscCHAxVlJUQIHYMXGuEQmY0JegQIHBAw"
urlWhatsapp = "https://web.whatsapp.com/ "
		
def ObtainInformation(url):
	#Open the broser in the correct page
	response = requests.get(url, headers={'Accept': 'text/html'})
	parsed_response = BeautifulSoup(response.text, 'html.parser')

	value = parsed_response.find(class_='YMlKec fxKbKc')
	return value


def PrintInformation(value):
	#Format the value to a string
	return str(value.text) 


class SesionOpen:
	def __init__(self, urlWhatsapp, contactName):
		#Define all the variables and atributes of my object
		#Remember this is a constructor
		self.urlWhatsapp = urlWhatsapp
		self.contactName = contactName		
		
		#Init the instance correctly 
		chrome_options = Options()
		chrome_options.add_experimental_option("detach", True)

		browserDriver = Service('/usr/lib/chromium-browser/chromedriver')
		self.driver = webdriver.Chrome(service=browserDriver, options=chrome_options)
		
		
	def OpenBrowser(self):
		#Open the browser and navigate to the Whatapp web page
		driver = self.driver
		url = self.urlWhatsapp

		driver.get(url)
		
		driver.maximize_window()	## Maximize the window for better experience


	def SelectContact(self):
		#Searh in the contact list the specific one and select with a click
		driver = self.driver
		name = self.contactName
		
		contactNameXPATH = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p")
		contactNameXPATH.send_keys(name)
		

	def SendMesagge(stockValue):
		#Select the message box, prit the message and click in send
		pass



"""
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('A') #How to import passwords


#Finnaly, press LogIn Button
#/html/body/div/div[2]/div/div/div/form/button
LogInButton = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/form/button')
LogInButton.click()
"""






	#Use of the information
#Obtain the information
stockValue = ObtainInformation(urlStock)
print(PrintInformation(stockValue), "THis is the current value")


#Create instance and open browser
inicioSesion = SesionOpen(urlWhatsapp, "YoMero")
inicioSesion.OpenBrowser()
sleep(25)

#Wait to autenticata manually,
#input("Write anything here to continue with the process")

#Send the information of the instance
inicioSesion.SelectContact()





















