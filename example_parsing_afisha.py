import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

url = 'https://www.afisha.ru/spb/schedule_cinema/'
domain = 'https://www.afisha.ru'
movie_list = []

req = session.get(url, headers = headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    movie_table = bsObj.find('div', {'class': 'cards cards-grid'})

    movies = movie_table.find_all('div', {'class': 'card cards-grid__item'})
    print (len(movies))
    for movie in movies:
        name = movie.find('h3', {'itemprop': 'name'}).text.strip()
        rating = 'no info'
        find_rtng = movie.find('div', {'class': 'rating-static__item rating-badge rating-badge_color_blue'})
        if find_rtng:
            rating = find_rtng.text

        genre = movie.find('a', {'class': 'card__badge'}).text
        href = movie.find('a', {'itemprop': 'url'})['href']
        descr = movie.find('p', {'itemprop': 'description'}).text.strip()

        movie_list.append({'title': name, 'rating': rating, 'genre': genre, 'descr': descr, 'href': domain + href})

template = '<!doctytpe html><html lang="en"><head><meta charset= "utf-8"></head><body>'
end = '</body></html>'

content = '<h2> Сегодня в кино</h2>'

for film in movie_list:
    content += '<a href = "{href}" target = "_blank">{title}</a><br/><p>Рейтинг: {rating}</p><p>Жанр: {genre}</p><p>{descr}</p><br/>'.format(**film)
    content += '<hr/><br><br/>'
data = template + content + end
handle = codecs.open('movie_today.html', "w", 'utf-8')
handle.write(str(data))
handle.close()