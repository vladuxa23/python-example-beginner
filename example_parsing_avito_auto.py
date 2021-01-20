import requests
from bs4 import BeautifulSoup
import csv
import time
import os

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)

def write_csv(data):
    with open('avitoAuto.csv', 'a', encoding = 'utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        try:
            writer.writerow((data['time'],
                             data['title'],
                             data['price'],
                             data['url']))
        except:
            pass

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:

        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''

        try:
            price = ad.find('div', class_='about').text.strip().strip('  ')
        except:
            price = ''

        ad_time = time.strftime("%H:%M:%S %d.%m.%Y", time.localtime())
        data = {'time': ad_time,
                'title': title,
                'price': price,
                'url': url
                }
        write_csv(data)

def main():
    url = 'https://www.avito.ru/sankt-peterburg/avtomobili/avtomat/levyy_rul?f=188_6045b0.1375_0b15520.1374_15786b0&p=1&pmax=600000&pmin=400000&radius=0'
    base_url = 'https://www.avito.ru/sankt-peterburg/avtomobili/avtomat/levyy_rul?f=188_6045b0.1375_0b15520.1374_15786b0&'
    page_part = 'p='
    query_part = '&pmax=600000&pmin=400000&radius=0'

    total_pages = get_total_pages(get_html(url))

    try:
        os.remove('avitoAuto.csv')
        print('Старый отчёт удалён')
    except:
        print('Старый отчёт не найден')
        pass
    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        get_page_data(html)

while True:
    i = 600
    main()
    print('Отчёт сформирован')
    while i > -1:
        print('Отчёт будет обновлён через ' + str(i//60) + ' минут ' + str(i%60) + ' секунд')
        i -= 30
        time.sleep(30)
