import dao


def main():
    result = dao.selectAllStock()
    print(result)
    for stock in result:
        code = stock[0]
        print(code)


if __name__ == '__main__':
    main()
