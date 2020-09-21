import requests
from bs4 import BeautifulSoup
import time
while True:
    URL = 'http://localhost:80'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    follower = soup.body.text
    print(follower)
    time.sleep(5)