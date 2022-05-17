import requests
from bs4 import BeautifulSoup
import pprint
import json

pages=int(input('Введите кол-во страниц для сбора данных: '))
i = 0
data={}
data['release'] = []
data['title']=[]
data['short_description']=[]
data['href']=[]
for page in range(1,pages+1):
    url = 'https://pythondigest.ru/feed/?page='+str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news = soup.find('div', class_='news-list')

    k=0
    for child in news.children:

        k += 1
        if k <= 20:
            i += 1
            big_body_div = child.find('div', class_='news-line-dates')
            release = big_body_div.find('a', class_='section-link')
            data['release'].append(release.text)
            #print(release.text)
            article_title = child.find('div', class_='news-line-item')
            article = article_title.find('a')
            data['title'].append(article.text)
            #print(article.text)
            try:
                data['short_description'].append(article_title.contents[2].text)
                #print(article_title.contents[2].text)
            except:
                data['short_description'].append('Нет краткого описания')
                # print('Нет краткого описания')
            data['href'].append(article.get('href'))
            # print(article.get('href'))


with open('pythondigest_serch.json', 'w') as f:
    f.write(json.dumps(data))
pprint.pprint(data)

print('Кол-во статей: ', i)