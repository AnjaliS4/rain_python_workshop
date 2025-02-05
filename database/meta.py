# Extract meta information from a webpage 
import requests
from bs4 import BeautifulSoup

url = "http://kathmandupost.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

meta = soup.find_all("meta")

#for meta in soup.find_all("meta"):
    #print(meta.get("name"), meta.get("content"))

# to find the meta content
meta_content = soup.find("meta", {"name": "description"})
# print the content 
if meta_content:
    print(meta_content.get("content"))
else:
    print("No meta content found.")