# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests as req
from bs4 import BeautifulSoup as bs
import re
import lxml
# URL = 'https://catalog.onliner.by/videocard?desktop_gpu%5B0%5D=rtx3060ti&desktop_gpu%5B1%5D=rtx3070&desktop_gpu%5Boperation%5D=union'
URL = 'https://catalog.onliner.by/videocard/gigabyte/gvn306tgamingocp'
URL_M = 'https://catalog.onliner.by/videocard?desktop_gpu[0]=rtx3060ti&desktop_gpu[1]=rtx3070&desktop_gpu[operation]=union'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_html(url,params = None):
    res = req.get(url,headers=HEADERS,params=params)
    return res

def get_content(html):
    soup = bs(html,'html.parser')
    # print(soup)
    item1 = soup.find_all('h1', class_='catalog-masthead__title')
    print(item1[0].getText())

    item2 = soup.find_all('a', class_="offers-description__link offers-description__link_subsidiary offers-description__link_nodecor")
    # print(item2)
    item3 = item2[0].find('span', class_="helpers_hide_tablet")
    str = item3.getText()
    # print(str)
    ilist=(str.split('-'))[0].split('\xa0')
    mlist = ilist[0].split(' ')
    f = float(mlist[0].replace(',','.'))
    print(f)
    lm = []
    lm.append({
        item1[0].getText().strip(),
        f
    })
    print(lm)

def get_hrefs(url):
    res = get_html(url)
    soup = bs(res.text, 'html.parser')

    refs = soup.find_all('div', class_='schema-product__title')
    # refs = soup.find('a', href='True')
    # refs = soup.findAll('a')
    print(refs)
    # refs =soup('a')
    # links = [link['href'] for link in soup('a') if 'href' in link.attrs]
    # print(links)
    # link = refs[0].find('a')
    # print(link)

def parse():
    res = get_html(URL)
    # print(res.text)
    if res.status_code == 200:
        get_content(res.text)
    else:
        print('something going wrong!!')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # parse()
    get_hrefs(URL_M)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
