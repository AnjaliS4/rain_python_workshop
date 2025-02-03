import requests
from bs4 import BeautifulSoup


# use another URL this is is having connection issues 

#URL of a news website (Example: BBC news)
url = "https://ekantipur.com/"

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
news = soup.find_all('a')
print("All news:")
for i in news:
    print(i.get('href'))