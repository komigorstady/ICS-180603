""" модуль для отримання даних про постачання та вивід їх на екран
"""

def get_markets():
    """ повертає вміст файла 'markets.txt` у вигляді списка
    """
    with open('./data/markets.txt', encoding="utf8") as indicators_file:
        from_file = indicators_file.readlines()

    markets_list = []

    for line in from_file:
        line_list = line.split(';')
        markets_list.append(line_list)
    
    return markets_list

def get_inidicators():
    """ повертає вміст файла 'indicators.txt` у вигляді списка
    """
    with open('./data/indicators.txt', encoding="utf8") as indicators_file:
        from_file = indicators_file.readlines()

    indicators_list = []

    for line in from_file:
        line_list = line.split()
        indicators_list.append(line_list)
    
    return indicators_list


def show_markets(markets):
    # задати інтервал виводу
    market_code_from = input("З якого кода клієнта?")
    market_code_to   = input("По який код клієнта?")

    # накопичує кількість виведених рядків
    kol_lines = 0

    for market in markets:
        if int(market_code_from) <= int(market[0]) <= int(market_code_to):
            print("номер: {:3} назва: {:16}".format(market[0], market[1]))
            kol_lines += 1
    
    # перевірити чи був вивід хоча б одного рядка
    if kol_lines == 0:
        print("Повашому запыту магазинiв не знайдено")



def show_indicators(indicators):
    # задати інтервал виводу
    indicators_code_from = input("З якого кода клієнта? ")
    indicators_code_to   = input("По який код клієнта? ")

    # накопичує кількість виведених рядків
    kol_lines = 0

    for indicator in indicators:
        if int(indicators_code_from) <= int(indicator[1]) <= int(indicators_code_to):
            print("квартал: {:16} номер: {:3} товарообiг плановый: {:3} товарообiг фактичний: {:3} продуктивнiсть планова: {:3}продуктивнicть фактична: {:3}".format(indicator[0], indicator[1], indicator[2], indicator[3], indicator[4], indicator[5]))
            kol_lines += 1

    # перевірити чи був вивід хоча б одного рядка
    if kol_lines == 0:
        print("Повашому запыту магазинiв не знайдено")



markets = get_markets()
show_markets(markets)

indicators = get_inidicators()
show_indicators(indicators)