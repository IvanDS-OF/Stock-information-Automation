##This code is to join all the infroamtion and the previous programs
#THat now enable me to create the final project

#Attampt 1

#Libraries needed

import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from time import sleep

from bs4 import BeautifulSoup
from time import sleep


#Now we will create the functions that will define the 
#structure of the project


#Define some globl and important variables
url = "https://www.google.com/finance/quote/USD-MXN?sa=X&ved=2ahUKEwiarpWnscCHAxVlJUQIHYMXGuEQmY0JegQIHBAw"


		
def ObtainInformation(url):
	#Open the broser in the correct page
	response = requests.get(url, headers={'Accept': 'text/html'})
	parsed_response = BeautifulSoup(response.text, 'html.parser')

	value = parsed_response.find(class_='YMlKec fxKbKc')
	return value


def PrintInformation(value):
	#Format the value to a string
	return str(value.text) 

def OpenBrowser(url):
	#Now we open the browser in whatsapp 
	

def SelectContact(name):
	#Searh in the contact list the specific one and select with a click
	

def SendMesagge(stockValue)
	#Select the message box, prit the message and click in send
	







	#Use of the information

stockValue = ObtainInformation(url)
print(PrintInformation(stockValue), "THis is the current value")












