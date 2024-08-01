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


	#Open the broser in the correct page	
def obtainInformation(url):
	response = requests.get(url, headers={'Accept': 'text/html'})
	parsed_response = BeautifulSoup(response.text, 'html.parser')

	value = parsed_response.find(class_='YMlKec fxKbKc')
	return value


def printInformation(value):
	return str(value.text) 


	#Use of the information

stockValue = obtainInformation(url)
print(printInformation(stockValue), "THis is the current value")








