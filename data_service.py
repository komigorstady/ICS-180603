def get_markets():
    with open('./data/markets.txt', encoding="utf8") as markets_file:
        from_file = markets_file.readlines()

    markets_list = []

    for line in from_file:
        line_list = line.split(';')
        markets_list.append(line_list)

def get_inidicators():
    with open('./data/indicators.txt', encoding="utf8") as indicators_file:
        from_file = indicators_file.readlines()

    indicators_list = []

    for line in from_file:
        line_list = line.split()
        indicators_list.append(line_list)

def show_markets(market):
    client_code_from = input("З якого номера супермаркета? ")
    client_code_to   = input("По який номер клієнта? ")

    kol_lines = 0

    for market in
