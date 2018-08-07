import sys
import requests
import re
from bs4 import BeautifulSoup

def recursiveA(url, nextA):
    page = 1
    finished = False
    urls = [url]

    try:
        while finished == False:
            response = requests.get(urls[-1])

            soup = BeautifulSoup(response.text, 'html.parser')

            text = soup.title.text + '\n\n\n'
            p_list = soup.find_all('p', text=True)
            for p in p_list:
                text += p.text + '\n\n'

            file = open(soup.title.text + '.txt', 'w')
            file.write(text)
            file.close()
            page += 1

            urls.append(soup.find('a', string=nextLinkText)['href'])
    except TypeError:
        print('Exception: ' + urls[-1])
        finished = True

#    print(str(page - 1) + ' pages scraped.')
#    print('Script terminating.')

def allA(url, hrefPattern=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if isinstance(hrefPattern, str) == True:
        urls = soup.find_all('a', {'href': re.compile(hrefPattern)})
    else:
        urls = soup.find_all('a')

    for url in urls:
        response = requests.get(url['href'])
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.title.text + '\n\n\n'
        p_list = soup.find_all('p', text=True)
        for p in p_list:
            text += p.text + '\n\n'
   
    file = open(soup.title.text + '.txt', 'w')
    file.write(text)
    file.close()
    finished = True
