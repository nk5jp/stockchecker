import dao
import minkabuPerser

def main():
    stocks = dao.selectAllStock()
    watchByCode = dao.selectAllWatchByCode()
    for stock in stocks:
        code = stock[0]
        stockInfo = minkabuPerser.getStockInfo(code)
        if code == stockInfo[0]:
            dao.insertDaily(code, stockInfo[2], stockInfo[3])
            if (code in watchByCode):
                if (stockInfo[3] < watchByCode[code][0]):
                    print (f'{code}: {stockInfo[3]} is lower than {watchByCode[code][0]}')
                if (stockInfo[3] > watchByCode[code][1]):
                    print (f'{code}: {stockInfo[3]} is upper than {watchByCode[code][1]}')


if __name__ == '__main__':
    main()
