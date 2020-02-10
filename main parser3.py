import  requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):# get html
    r = requests.get(url)
    return r.text


def write_csv(data):# write data to csv file
    with open('cms.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'], data['symbol'], data['url'], data['price']])

def get_page_data(html): # parsing
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('tbody').find_all('tr', class_='cmc-table-row')
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a').text
        symbol = tds[5].find('div', class_='').text
        re_symbol = re.findall(r'([A-Z]{1,5})', symbol)
        re_symbol_clear = (re_symbol)[0]
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        clean_price = tds[3].find('a', class_='cmc-link').text
        pre_price = re.findall(r'([0-9]{0,7})', clean_price)
        price = (pre_price)[0]

        data = {'name': name, 'symbol': re_symbol_clear, 'url': url, 'price':price}
        write_csv(data)




















def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))



if __name__ == '__main__':
    main()