import requests
from bs4 import BeautifulSoup

post = 1
url = input("Start Page URL: ")
nextLinkText = input("Next link's text (Must be EXACT): ")

while post <= 3:
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.title.text + '\n\n\n'
        p_list = soup.find_all('p', text=True)
        for p in p_list:
            text += p.text + '\n\n'

        file = open('Post_' + str(post) + '.txt', 'w')
        file.write(text)
        file.close()
        post += 1

        url = soup.find('a', string=nextLinkText)['href']
