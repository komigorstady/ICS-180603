""" Аналіз товарообігу та продуктивності праці
"""
# підключити функції з модуля `data_service`
from data_service import get_markets, get_inidicators

# структура накопичувача записів вихідних даних
table = {
    'name_of_market'               : '',  #назва магазину
    'quarter'                      : '',  #квартал
    'planned_exchange_of_goods'    : 0.0, #запланований товарообiг
    'actual_exchange_of_goods'     : 0.0, #фктичний товарообiг
    'percentage_of_completion'     : 0.0, #вiдсотки
    'planne_productivity'          : 0.0, #планова продуктивнiсть 
    'actual_productivity'          : 0.0  #справжня  продуктивнiсть
}


markets = get_markets()
indicators = get_inidicators()

def create_table():
    
    def get_market_name(market_code):
        """повертає назву клієнта по його коду
            
        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """       

        for market in markets:
            if market[0] == market_code:
                return market[1]
        
        return"*** код клiента не знайнденый"

    # накопычуввч заявок
    table_list = []

    for indicator in indicators:
        # створити копію шаблона
        table_tmp = table.copy()

        table_tmp['name_of_market']            = get_market_name(indicator[1])
        table_tmp['quarter']                   = indicator[0]
        table_tmp['planned_exchange_of_goods'] = indicator[2]
        table_tmp['actual_exchange_of_goods']  = indicator[3]
        table_tmp['percentage_of_completion']  = float(table_tmp['actual_exchange_of_goods']) / float(table_tmp['planned_exchange_of_goods']) * 100
        table_tmp['planne_productivity']       = indicator[4]
        table_tmp['actual_productivity']       = indicator[5]
        
        table_list.append(table_tmp)

    return table_list

result = create_table()

for r in result:
    print(r)