import dao
import minkabuParser
import datetime
import notification
import numpy
import locale

locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

def main():
    dt_now =  datetime.datetime.now()
    now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    print(f'{now}: getCurrentPrice start')
    stocks = dao.selectAllStock()
    watchByCode = dao.selectAllWatchByCode()
    messageString = ''
    messageStringFormat = '{0}({1}), '
    for stock in stocks:
        try:
            code = stock[0]
            stockInfo = minkabuParser.getStockInfo(code)
            if code == stockInfo[0]:
                dao.insertDaily(code, stockInfo[2], stockInfo[3])
#                if (code in watchByCode):
#                    if (float(stockInfo[3]) < watchByCode[code][0]):
#                        print (f'{code}: {stockInfo[3]} is lower than {watchByCode[code][0]}')
#                        messageString = messageString + messageStringFormat.format(code, stockInfo[3])
#                    if (float(stockInfo[3]) > watchByCode[code][1]):
#                        print (f'{code}: {stockInfo[3]} is upper than {watchByCode[code][1]}')
#                        messageString = messageString + messageStringFormat.format(code, stockInfo[3])
#                latest40 = dao.selectStockByCode(code, 40)
#                if latest40.shape[1] != 40:
#                    continue
#                if numpy.corrcoef(latest40)[0, 1] > -0.7:
#                    continue
#                latest10 = latest40[:, 0:10]
#                if numpy.corrcoef(latest10)[0, 1] > 0.7:
#                    print (f'{code} is recommended. {numpy.corrcoef(latest40)[0, 1]} and {numpy.corrcoef(latest10)[0, 1]}')
#                    messageString = messageString + messageStringFormat.format(code, 'Rec')
        except Exception as e:
            print(f'{code}: some error has been occered and skipped.')
            print(e)
            continue
#    notification.sendMessage({'date': dt_now.strftime('%Y%m%d'), 'message': messageString})
    dt_now =  datetime.datetime.now()
    now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    print(f'{now}: getCurrentPrice end')


if __name__ == '__main__':
    main()
