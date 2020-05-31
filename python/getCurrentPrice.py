import dao
import minkabuPerser
import datetime

def main():
    dt_now =  datetime.datetime.now()
    now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    print(f'{now}: getCurrentPrice start')
    stocks = dao.selectAllStock()
    watchByCode = dao.selectAllWatchByCode()
    for stock in stocks:
        code = stock[0]
        stockInfo = minkabuPerser.getStockInfo(code)
        if code == stockInfo[0]:
            dao.insertDaily(code, stockInfo[2], stockInfo[3])
            if (code in watchByCode):
                if (float(stockInfo[3]) < watchByCode[code][0]):
                    print (f'{code}: {stockInfo[3]} is lower than {watchByCode[code][0]}')
                if (float(stockInfo[3]) > watchByCode[code][1]):
                    print (f'{code}: {stockInfo[3]} is upper than {watchByCode[code][1]}')
    now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    print(f'{now}: getCurrentPrice end')


if __name__ == '__main__':
    main()
