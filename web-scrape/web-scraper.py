import re
import requests
from bs4 import BeautifulSoup

url = 'https://twin-cities.umn.edu/contact'
url_source = requests.get(url)
#url_source.text
soup = BeautifulSoup(url_source.text, 'html.parser')

#regex patterns for emails and phone numbers
phones = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',url_source.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)',url_source.text)
print(phones,emails)

#extract all links
links=[]
for link in soup.find_all('a', href=True):
    links.append(link['href'])
print(links)
