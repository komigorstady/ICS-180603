""" Формування заявок на устатткування по магазину
"""
from data_service import get_markets, get_inidicators

analysis_of_turnover = {
    'name_of_market'               : '',
    'quarter '                     : '',
    'planned_exchange_of_goods'    : 0.0,
    'actual_exchange_of_goods'     : 0.0,
    'percentage_of_completion'     : 0,
    'planne_productivity'          : 0.0,
    'actual_productivity'          : 0.0
}

market = get_markets()
indicators = get_inidicators()

"""
def create_zajavka():
    Формування заявок на товары
    
    def get__name(client_code)
    повертаэ назву його коду
    

    for indicator in indicators:
        if inidicator[0] == inidicator_code:
            return client[1]
        return "код клиета не знайденый"

    # накопычувач заявок
    zajavka_list = []

    for inidicator in inidicators:
        zajavka_tmp = zajavka.copy()

        zajavka_tmp['around_name'] = inidicator[2]
        #zajavka_tmp['client_name'] =
        zajavka_tmp['order_number'] = inidicator[1]
        zajavka_tmp['kol'] = inidicator[3]
        zajavka_tmp['price'] = inidicator[4]
        zajavka_tmp['tottal'] = zajavka_tmp['kol'] * zajavka_tmp['price']

        zajavka_list.append(zajavka_tmp)

    return zajavka_list

result = create_zajavka()


for r in result:
    print(r)
"""