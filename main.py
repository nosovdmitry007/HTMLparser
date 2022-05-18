import requests
from bs4 import BeautifulSoup
#
def HTMLparser(SERCH,pages=1):

    i = 0
    serchs=[]
    for page in range(1, pages+1):


        url = f'https://pythondigest.ru/feed/?q={SERCH}&page={str(page)}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        news = soup.find('div', class_='news-list')

        k=0
        for child in news.children:
            answer = []
            k += 1
            if k <= 20:
                i += 1
                big_body_div = child.find('div', class_='news-line-dates')
                release = big_body_div.find('a', class_='section-link')
                answer.append(release.text)
                answer.append('\n\n')
                article_title = child.find('div', class_='news-line-item')
                article = article_title.find('a')
                answer.append(article.text)
                answer.append('\n\n')
                try:
                    answer.append(article_title.contents[2].text)
                    answer.append('\n\n')
                except:
                    answer.append('Нет краткого описания')
                    answer.append('\n\n')
                answer.append(article.get('href'))
                string = "".join(answer)

                serchs.append(string)

    return serchs
