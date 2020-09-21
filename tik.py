import requests
from bs4 import BeautifulSoup
import time
new = 0
current = 0
while True:
    URL = 'http://localhost:80'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    follower = soup.body.text
    new = int(follower)
    if new > current:
        print (new, "you gained a new follower")
        current = new
    else:
        print(current, "get in the bin m8")
    time.sleep(5)