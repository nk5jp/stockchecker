import requests
import sys
from html.parser import HTMLParser
from decimal import Decimal
import dao

baseURL = 'https://minkabu.jp/stock/'

class MinkabuParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_in_stockname_tag = False
        self.has_stock_name = False
    def handle_starttag(self, tag, attrs):
        if tag == 'p' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'md_stockBoard_stockName':
            self.is_in_stockname_tag = True
            self.has_stock_name = True
    def handle_endtag(self, tag):
        if self.is_in_stockname_tag == True and tag == 'p':
            self.is_in_stockname_tag = False
    def handle_data(self, data):
        if self.is_in_stockname_tag:
            self.name = data

def main():
    for code in range(1000, 10000):
        URL = baseURL + str(code)
        request = requests.get(URL)
        parser = MinkabuParser()
        parser.feed(request.text)
        if parser.has_stock_name:
            dao.insertStock(str(code), parser.name)
            print(f'{code}: {parser.name}')
        else:
            print(f'{code}: Not Found')

if __name__ == '__main__':
    main()

