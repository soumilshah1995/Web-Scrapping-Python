import requests
from bs4 import BeautifulSoup

url = 'https://www.bridgeport.edu'

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

i = 0
for img in soup.findAll('img'):
    i = i + 1

    image_temp = img.get('src')
    if image_temp[:1] == '/':
        image_path = "https://www.bridgeport.edu" + image_temp
    else:
        image_path = image_temp

    file_name_temp = img.get('alt')

    if len(file_name_temp) == 0:
        filename = str(i)
    else:
        filename = file_name_temp

    if '.jpg' in image_path:
        with open("{}.jpg".format(filename), 'wb') as f:
            f.write(requests.get(url=url).content)

    elif '.png' in image_path:
        with open("{}.jpg".format(filename), 'wb') as f:
            f.write(requests.get(url=url).content)




