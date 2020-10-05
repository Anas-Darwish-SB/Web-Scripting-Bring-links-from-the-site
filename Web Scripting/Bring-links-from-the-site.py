#Made by Anas Darwish

from bs4 import BeautifulSoup
import requests

url = input("Type in the URL for a site: ")

req = requests.get(url)
bs = BeautifulSoup(req.text,"html.parser")
for link in bs.findAll('a'):
    print(link.get("href"))
