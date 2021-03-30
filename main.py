# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import Parser as pa

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options, executable_path='geckodriver.exe')

URL = 'https://catalog.onliner.by/videocard/gigabyte/gvn306tgamingocp'
URL_M = 'https://catalog.onliner.by/videocard?desktop_gpu[0]=rtx3060ti&desktop_gpu[1]=rtx3070&desktop_gpu[operation]=union'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = pa.Parser(URL_M,pages=1)
    parser.get_data()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
