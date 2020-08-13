from configparser import ConfigParser
import MySQLdb
import os
import numpy

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
user = config.get('mysql', 'user')
password = config.get('mysql', 'password')
host = config.get('mysql', 'host')
database = config.get('mysql', 'database')



def returnConnect():
    return MySQLdb.connect(
        user=user,
        passwd=password,
        host=host,
        db=database
    )


def insertStock(code, name):
    insertSQL = 'insert into stock(code, name) values (%s, %s)'
    conn = returnConnect()
    cursor = conn.cursor()
    try:
        cursor.execute(insertSQL, (code, name))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def selectAllStock():
    conn = returnConnect()
    cursor = conn.cursor()
    try:
        cursor.execute('select * from stock')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def selectStockByCode(code, max):
    conn = returnConnect()
    cursor = conn.cursor()
    try:
        cursor.execute('select * from daily where code = %s order by get_date desc', (code,))
        result = numpy.empty((0,0))
        min_max = max if cursor.rowcount > max else cursor.rowcount
        for i in range(min_max):
            daily = cursor.fetchone()
            result_append = numpy.array([i],[float(daily[2])])
            result = numpy.append(result, result_append, axis=1)
        return result
    finally:
        cursor.close()
        conn.close()


def insertDaily(code, date, price):
    insertSQL = 'insert into daily(code, get_date, price) values (%s, %s, %s)'
    conn = returnConnect()
    cursor = conn.cursor()
    try:
        cursor.execute(insertSQL, (code, date, price))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def selectAllWatchByCode():
    conn = returnConnect()
    cursor = conn.cursor()
    try:
        cursor.execute('select code, is_upper_bound+0, price from watch_by_code')
        results = cursor.fetchall()
        rules = {}
        for result in results:
            code = result[0]
            if (not code in rules):
                rules[code] = [0, 999999] 
            if result[1]:
                rules[code][1] = result[2]
            else:
                rules[code][0] = result[2]
        return rules
    finally:
        cursor.close()
        conn.close()
