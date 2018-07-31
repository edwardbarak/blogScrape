import sys
import requests
from bs4 import BeautifulSoup

post = 1
finished = False
urls = [input("Start Page URL: ")]
nextLinkText = input("Next link's text (Must be EXACT): ")

try:
    while finished == False:
        response = requests.get(urls[-1])

        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.title.text + '\n\n\n'
        p_list = soup.find_all('p', text=True)
        for p in p_list:
            text += p.text + '\n\n'

        file = open('Post_' + str(post) + '.txt', 'w')
        file.write(text)
        file.close()
        post += 1

        urls.append(soup.find('a', string=nextLinkText)['href'])
except TypeError:
    print('Exception: ' + urls[-1])
    finished = True

print(str(post - 1) + ' posts scraped.')
print('Script terminating.')
