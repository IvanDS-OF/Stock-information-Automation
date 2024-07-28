import requests
from bs4 import BeautifulSoup
from time import sleep

def WebScraping():
    url = "https://www.google.com/finance/quote/USD-MXN?sa=X&ved=2ahUKEwiarpWnscCHAxVlJUQIHYMXGuEQmY0JegQIHBAw"

    response = requests.get(url, headers={'Accept': 'text/html'})
    parsed_response = BeautifulSoup(response.text, 'html.parser')

    value = parsed_response.find(class_='YMlKec fxKbKc')
    print (value.text)
    return str(value.text) # To work with a function, we need to treat this different





#<div class="YMlKec fxKbKc">18.3578</div>

for i in range(10):
    url = "https://www.google.com/finance/quote/USD-MXN?sa=X&ved=2ahUKEwiarpWnscCHAxVlJUQIHYMXGuEQmY0JegQIHBAw"

    response = requests.get(url, headers={'Accept': 'text/html'})
    parsed_response = BeautifulSoup(response.text, 'html.parser')

    value = parsed_response.find(class_='YMlKec fxKbKc')
    print (value.text)
    sleep(60)
