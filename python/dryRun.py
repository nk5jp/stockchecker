import dao
import minkabuParser
import numpy

def main():
    print(f'dryRun start')
    stocks = dao.selectAllStock()
    for stock in stocks:
        try:
            code = stock[0]
            latest40 = dao.selectStockByCode(code, 40)
            if latest40.shape[1] != 40:
                continue
            if numpy.corrcoef(latest40)[0, 1] > -0.7:
                continue
            latest10 = latest40[0:10]
            if numpy.corrcoef(latest10)[0, 1] > 0.7:
                print (f'{code} is recommended. {numpy.corrcoef(latest40)[0, 1]} and {numpy.corrcoef(latest10)[0, 1]}')
        except Exception as e:
            print(f'{code}: some error has been occered and skipped.')
            print(e)
            continue
    print('dryRun end')


if __name__ == '__main__':
    main()
