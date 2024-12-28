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
        self.is_in_stockdividend_tag = False
        self.dividend = ''
    def handle_starttag(self, tag, attrs):
        if tag == 'span' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'md_stockBoard_stockName':
            self.is_in_stockname_tag = True
            self.has_stock_name = True
        elif tag == 'span' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'dividend-state__amount__integer':
            self.is_in_stockdividend_tag = True
    def handle_endtag(self, tag):
        if self.is_in_stockname_tag == True and tag == 'span':
            self.is_in_stockname_tag = False
        elif self.is_in_stockdividend_tag == True and tag == 'span':
            self.is_in_stockdividend_tag = False
            self.dividend = self.dividend.replace('.', '').replace(',', '')
    def handle_data(self, data):
        if self.is_in_stockname_tag:
            self.name = data
        elif self.is_in_stockdividend_tag:
            self.dividend += data

def main():
    for code in range(1000, 10000):
        URL = baseURL + str(code) + '/dividend'
        request = requests.get(URL)
        parser = MinkabuParser()
        parser.feed(request.text)
        if parser.dividend == '':
            parser.dividend = '0'
        if parser.has_stock_name and not(dao.checkTheStockRegistered(code)):
            dao.insertStock(str(code), parser.name, int(parser.dividend))
            print(f'{code}: {parser.name} add')
        elif parser.has_stock_name and dao.checkTheStockRegistered(code):
            dao.updateStock(str(code), parser.name, int(parser.dividend))
            print(f'{code}: {parser.name} update')
        # else:
        #     print(f'{code}: Not Found')
    for i in range(65, 91):
        for code_min in range(130, 999):
            code = str(code_min) + chr(i)
            URL = baseURL + code + '/dividend'
            request = requests.get(URL)
            parser = MinkabuParser()
            parser.feed(request.text)
            if parser.dividend == '':
                parser.dividend = '0'
            if parser.has_stock_name and not(dao.checkTheStockRegistered(code)):
                dao.insertStock(code, parser.name, int(parser.dividend))
                print(f'{code}: {parser.name} add')
            elif parser.has_stock_name and dao.checkTheStockRegistered(code):
                dao.updateStock(code, parser.name, int(parser.dividend))
                print(f'{code}: {parser.name} update')
            # else:
            #     print(f'{code}: Not Found')
if __name__ == '__main__':
    main()

