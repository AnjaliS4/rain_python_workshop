# Question 1 Scrape Article Titles from a News Website
# Question 2 Extract Table Data from a Webpage 

import requests
from bs4 import BeautifulSoup
url = "https://ekantipur.com/" 
response = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')
Title = soup.find_all('h1', class_='eng-text eng-text-heading') 







for i in news:
    print(i.text)

