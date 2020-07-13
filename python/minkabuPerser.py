import requests
import sys
from html.parser import HTMLParser
from decimal import Decimal
import dao
import datetime

baseURL = 'https://minkabu.jp/stock/'

class MinkabuParser(HTMLParser):


    def __init__(self):
        super().__init__()
        self.is_in_stockname_tag = False
        self.is_in_stockdate_tag = False
        self.is_in_stockdate_fsm_tag = False
        self.is_in_stockprice_tag = False
        self.has_stock_name = False
        self.price = ''


    def checkAttrs(self, attrs, key, value): 
        return len(attrs) > 0 and attrs[0][0] == key and attrs[0][1] == value


    def handle_starttag(self, tag, attrs):
        if tag == 'p' and self.checkAttrs(attrs, 'class', 'md_stockBoard_stockName'):
            self.is_in_stockname_tag = True
            self.has_stock_name = True
        elif tag == 'span' and self.checkAttrs(attrs, 'class', 'fsm') and self.is_in_stockdate_tag:
            self.is_in_stockdate_fsm_tag = True
        elif tag == 'h2' and self.checkAttrs(attrs, 'class', 'stock_label fsl'):
            self.is_in_stockdate_tag = True
        elif tag == 'div' and self.checkAttrs(attrs, 'class', 'stock_price'):
            self.is_in_stockprice_tag = True


    def handle_endtag(self, tag):
        if self.is_in_stockname_tag == True and tag == 'p':
            self.is_in_stockname_tag = False
        elif self.is_in_stockdate_tag == True and tag == 'h2':
            self.is_in_stockdate_tag = False
        elif self.is_in_stockdate_fsm_tag == True and tag == 'span':
            self.is_in_stockdate_fsm_tag = False
        elif self.is_in_stockprice_tag == True and tag == 'div':
            self.is_in_stockprice_tag = False
            self.price = self.price.replace('円', '').replace(',', '').replace(' ', '').replace('\n', '')


    def handle_data(self, data):
        if self.is_in_stockname_tag:
            self.name = data
        elif self.is_in_stockdate_fsm_tag:
            self.date = data.replace('(', '').replace(')', '')
        elif self.is_in_stockprice_tag:
            self.price += data


def getStockInfo(code):
    URL = baseURL + str(code)
    request = requests.get(URL)
    parser = MinkabuParser()
    parser.feed(request.text)
    if parser.has_stock_name and not '-' in parser.price and ':' in parser.date:
        return (code, parser.name, datetime.datetime.now().strftime('%Y%m%d'), parser.price)
    else:
        print(f'{code} is skipped: {parser.price}, {parser.date}')
        return (0, '', '', 0.0)
