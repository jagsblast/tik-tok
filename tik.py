import requests
from bs4 import BeautifulSoup
import time
while True:
    URL = 'http://localhost:80'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    follower = soup.body.text
    new = int(follower)
    print ("current followers", new)
    if new > current:
        print (new, "you gained a new follower")
        current = new
    elif new < current:
        print(current, "get in the bin m8")
        current = new
    else:
        print(current, "gg my drilla")
        current = new
    time.sleep(2)