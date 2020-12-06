""" головний модуль задачі
- виводить розрахункову таблицю на екран та в файл
- виводить первинні данні на екран
"""

import os
from process_data import create_table
from data_service import show_markets, show_indicators, get_markets, get_inidicators
 
MAIN_MENU = \
"""
~~~~~~~  ОБРОБКА ТАБЛИЦЬ ПОКАЗНИКIВ ~~~~~~~

1 - вивід таблицi на екран
2 - запис таблиць в файл
3 - вивід списка cупермаркетiв
4 - вивід списка показникiв
0 - завершення роботи
----------------------------
"""

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ ПО МАГАЗИНУ"

HEADER = \
"""
=============================================================================================================================================================================================================================================
  Устаткування   |         Клієнт         |           Номер заказа           |                                Кількість           |      Ціна           |                      Сума
=============================================================================================================================================================================================================================================
"""

FOOTER = \
'''
==========================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter>'

def show_table(table_list):
    """виводиить таблицю заявок 

    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n\n{TITLE:^91}")
    print(HEADER)

    for table in table_list:
        print(f"{table['name_of_market']:20}",
              f"{table['quarter']:20}",
              f"{table['planned_exchange_of_goods']:20}",
              f"{table['actual_exchange_of_goods']:20}",
              f"{table['percentage_of_completion']:20}",
              f"{table['planne_productivity']:20}",
              f"{table['actual_productivity']:20}/n"
              )

    print(FOOTER)

def write_table(table_list):
    
    """
    записує список заявок у текстовий файл
    Args:
        zajavka_list ([type]): список заявок
    """
    
    with open('./data/table.txt', 'w', encoding="utf8") as table_file:
        for table in table_list:
            line = \
               table['name_of_market'] + ';' +  \
               table['quarter'] + ';' +  \
               str(table['planned_exchange_of_goods']) + ';' +  \
               str(table['actual_exchange_of_goods']) + ';' +  \
               str(table['percentage_of_completion'])  + ';' + \
               str(table['planne_productivity']) + ';' + \
               str(table['actual_productivity'])  + '\n'
            
            table_file.write(line)  
            
    print('Файл успішно записано ...')             


while True:
    
    # вивід головного меню
    os.system('clear')   
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)
        
    elif command_number == '1':
        table_list = create_table()
        show_table(table_list)
        input(STOP_MESSAGE)
    
    elif command_number == '2':
        table_list = create_table()
        write_table(table_list)
        input(STOP_MESSAGE)
    
    elif command_number == '3':
        indicators = get_inidicators()
        show_indicators(indicators)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        markets = get_markets()
        show_markets(markets)
        input(STOP_MESSAGE)

