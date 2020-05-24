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
