import parsing


def main():
    hands_url = 'https://hands.ru/company/about/'
    repetitors_url = 'https://repetitors.info/'
    print(parsing.get_telephone_num(hands_url))
    print(parsing.get_telephone_num(repetitors_url))


if __name__ == '__main__':
    main()
