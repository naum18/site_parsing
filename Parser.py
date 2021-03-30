from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
class Parser(object):
    """docstring"""

    def __init__(self, main_url,pages = 1,headers = None):
        """Constructor"""
        self.m_url = main_url
        self.headers = headers
        self.options = Options()
        self.options.headless = True
        self.browser = webdriver.Firefox(options=self.options, executable_path='geckodriver.exe')
        self.pages = pages

    def get_html(self, url, params=None):
        self.browser.get(url)
        self.browser.implicitly_wait(7)
        html = self.browser.page_source
        return html

    def get_content(self, html):
        soup = bs(html, 'html.parser')
        item1 = soup.find_all('h1', class_='catalog-masthead__title')
        item2 = soup.find_all('a', class_="offers-description__link offers-description__link_subsidiary offers-description__link_nodecor")
        # print(item2)
        if (len(item2) == 0):
            return ()
        item3 = item2[0].find('span', class_="helpers_hide_tablet")
        str = item3.getText()
        # print(str)
        ilist = (str.split('-'))[0].split('\xa0')
        # print(ilist)
        mlist = ilist[0].split(' ')
        # print(mlist)
        f = float(mlist[0].replace(',', '.'))
        # print(f)
        lm = {}
        s = item1[0].getText().strip().replace('\n', '')
        # print(s)
        lm = {'name': s, 'price': f}
        # print(lm)
        return lm

    def get_hrefs(self,url):

        res = self.get_html(url)
        soup = bs(res, 'html.parser')

        refs = soup.find_all('div', class_='schema-product__title')
        links_with_text = []
        for item in refs:
            for a in item.find_all('a', href=True):
                if a.text:
                    links_with_text.append(a['href'])
        return links_with_text

    def parse(self,url):
        res = self.get_html(url)
        content = self.get_content(res)
        return content

    def get_data(self):
        # parse()
        i = 0
        links = []
        len_old = 0
        while (i < self.pages):
            i += 1
            newurl = self.m_url + '&page=' + str(i)
            links.extend(self.get_hrefs(newurl))
            # print(len(res))
            len_new = len(links)
            delta = len_new - len_old
            if (delta == 0):
                break
            len_old = len_new

        print(links)
        print(len(links))

        values = []
        for a in links:
            l = self.parse(a)
            # условие с расчетом на то, что товары, которые не в наличии идут последними
            if (len(l) == 0):
                break
            values.append(l)
            print(l)

        # print(values)
        self.browser.close()
        file = open("vc.txt", 'w')
        index = 1
        for m in values:
            file.write(str(index) + "   " + str(m['price']) + "   " + str(m['name']) + " \n")
            index += 1
        file.close()

    def __del__(self):
        self.browser.quit()