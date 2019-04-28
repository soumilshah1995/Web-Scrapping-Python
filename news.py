import requests
import bs4
from bs4 import BeautifulSoup


def news():

    url_news = 'https://www.bridgeport.edu/news'

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }

    r = requests.get(url=url_news,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all(class_= "views-row")

    with open("sample.txt", "w")  as f:
        l_title=[]

        for x in data:
            try:
                title = x.find(class_='views-field views-field-title').get_text()

                date = x.find(class_="views-field views-field-created").get_text()
                a = x.find(class_= "views-field views-field-view-node")


                for q in a.findAll('a', href=True):
                    link = "https://www.bridgeport.edu" + q["href"]

                var = date + title + link+ "\n"
                l_title.append(var)

            except:
                pass

        s = " ".join(str(x) for x in l_title)

    return s



if __name__ == "__main__":
    print(news())


