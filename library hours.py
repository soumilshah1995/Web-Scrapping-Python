import requests
import bs4
from bs4 import BeautifulSoup

def get_title_news():

    counter = 0
    url_news = 'https://library.bridgeport.edu/about/hours/'

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }

    # Make a Request to URL
    r = requests.get(url=url_news, headers=headers)

    # Create a Soup Object
    soup = BeautifulSoup(r.text, 'html.parser')

    counter = 0
    time = []

    for x in soup.findAll(class_= "column-2"):
        try:
            counter += 1
            if counter == 1:
                time.append("Mon-Thursday " + x.get_text())
            if counter == 2:
                time.append("Friday " + x.get_text())
            if counter == 3:
                time.append("Saturday  " + x.get_text())
            if counter == 5:
                time.append("Sunday  " + x.get_text())
            if counter == 6:
                break
        except:
            pass

    s = " ".join(str(x) for x in time)
    return s


if __name__ == "__main__":
    print(get_title_news())


