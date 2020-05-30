from configparser import ConfigParser
import MySQLdb

config = ConfigParser()
config.read('config.ini')
user = config.get('mysql', 'user')
password = config.get('mysql', 'password')
host = config.get('mysql', 'host')
database = config.get('mysql', 'database')


def insertStock(code, name):
    insertSQL = 'insert into stock(code, name) values (%s, %s)'
    conn = MySQLdb.connect(
        user=user,
        passwd=password,
        host=host,
        db=database
    )
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
    conn = MySQLdb.connect(
        user=user,
        passwd=password,
        host=host,
        db=database
    )
    cursor = conn.cursor()
    try:
        cursor.execute('select * from stock')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def insertDaily(code, date, price):
    insertSQL = 'insert into daily(code, get_date, price) values (%s, %s, %s)'
    conn = MySQLdb.connect(
        user=user,
        passwd=password,
        host=host,
        db=database
    )
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
    conn = MySQLdb.connect(
        user=user,
        passwd=password,
        host=host,
        db=database
    )
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
