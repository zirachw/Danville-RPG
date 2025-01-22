# K03-F | utils -> printer

# Import Libraries
import sys
import os
import time
from typing import TextIO

# Definisi fungsi
## print_type
'''
'''

def print_type(list_of_dict: dict) -> None :
    counter: int = 0
    for rows in range(1, len(list_of_dict)) :
        counter += 1
        print(str(counter) + '. ' + list_of_dict[rows]['type'])

## print_all
'''
'''

def print_all(list_of_dict: list[dict], desc: str) -> None :

    key_counter = 0
    for rows in range(len(list_of_dict)) :
        total_length = 0
        for key in list_of_dict[rows] :
            key_counter += 1
            length: int = 0
            for i in range(len(list_of_dict)) :
                if len(str(list_of_dict[i][key])) > length :
                    length = len(str(list_of_dict[i][key]))
            total_length += length
        break

    print('=' + '=' * total_length + '=' * 3 * key_counter)
    print('| ' + desc + ' ' * (total_length + 3 * key_counter - len(desc) - 2) + '|')
    print('=' + '=' * total_length + '=' * 3 * key_counter)

    for rows in range(len(list_of_dict)) :
        header: str = '|'
        for key in list_of_dict[rows] :
            length: int = 0
            for i in range(len(list_of_dict)) :
                if len(str(list_of_dict[i][key])) > length :
                    length = len(str(list_of_dict[i][key]))
            header += (' ' + (str(list_of_dict[rows][key])) + ' ' * (length - len(str(list_of_dict[rows][key]))) + ' |')

        print(header)
        if rows == 0 :
            print('=' + '=' * total_length + '=' * 3 * key_counter)

    print('=' + '=' * total_length + '=' * 3 * key_counter)

## print_stat
'''
'''

def print_stats(type: str, level: int, attack: int, defense: int, hp: int) -> None :
        print('Name      :', type   )
        print('ATK Power :', attack )
        print('DEF Power :', defense)
        print('HP        :', hp     )
        print('Level     :', level  )

## print_results
'''
'''

def print_results(attacks: float, reduced: float, defense: float, results: int, percentage : float) -> None :
    if percentage >= 0 :
        attack = 'ATT: ' + str(attacks) + ' (+' + str(percentage) + '%)'

    else :
        attack = 'ATT: ' + str(attacks) + ' (' + str(percentage) + '%)'

    reduce = 'Reduced by: ' + str(reduced) + ' (+' + str(defense) + '%)'
    result = 'ATT Results: ' + str(results)
    print(attack + ', ' + reduce + ', ' + result) 

## print_results
'''
'''

def print_ally(login_now: dict, ally_stats: dict, owca_dex: list[dict]) -> None :
    print("RAWRRR", login_now['username'], "mengeluarkan monster", owca_dex[ally_stats['id']]['type'])
    print()
    print_stats(ally_stats['type'], ally_stats['level'], ally_stats['atk'], ally_stats['def'], ally_stats['hp'])
    print()

## print_jackpot
'''
'''

def print_jackpot(monster) -> None :
        
    print(
    '''
     ===========================''')
    today = '     | ' + ' ' * ((8 - len(monster)) // 2) + 'Monster Gacha: ' + monster + ' ' * ((8 - len(monster)) // 2)
    if ((8 - len(monster)) // 2) != ((8 - len(monster)) / 2)  :
        today += '  |'
    else :
        today += ' |'
    print(today)
    print(
    '''     |  Use 500 OC to Play !!  |
     ===========================
     |        Item List        |
     |  Hat       :     10 OC  |
     |  Sword     :     20 OC  |
     |  Coin      :     50 OC  |
     |  Potion    :    100 OC  |
     |  Monster   :    200 OC  |
     |  7         :    500 OC  |
     ===========================
    ''')

## print_animated
'''
'''

def print_animated(desc: str) -> None :
    while True :
        sys.stdout.write('\r' + desc + ' .')
        time.sleep(0.3)
        sys.stdout.write('\r' + desc + ' ..')
        time.sleep(0.3)
        sys.stdout.write('\r' + desc + ' ...')

        break

## print_inventory
'''
'''

def print_inventory(n_monsters, login_now: dict, user: list[dict], invento_stock: list[dict]) :

    option: int = 1
    print('=' * 12 + ' INVENTORY LIST (User ID: ' + str(login_now['user_id']) + ') ' + '=' * 12)
    print()
    print('Jumlah O.W.C.A. Coin-mu sekarang', user[login_now['user_id']]['oc'])
    for rows in range(len(invento_stock)) :

        if invento_stock[rows][0] == 'Monster' :
            n_monsters += 1
            print(str(option) + '. ' + 'Monster' + ' ' * 9 + '(Name: ' + str(invento_stock[rows][1]) + ', Lvl: ' + str(invento_stock[rows][2]) + ', HP: ' + str(invento_stock[rows][3]) + ')')

        elif invento_stock[rows][0] == 'Potion' and invento_stock[rows][2] > 0 :
            print(str(option) + '. ' + 'Potion' + ' ' * 10 + '(Type: ' + str(invento_stock[rows][1]) + ', Qty: ' + str(invento_stock[rows][2]) + ')')

        else :
            if invento_stock[rows][2] > 0 :
                print(str(option) + '. ' + 'Monster Ball' + ' ' * 4 + '(Qty: ' + str(invento_stock[rows][2]) + ')')

        option += 1

    print(str(option) + '. Keluar')
    print()
    print('=====================================================')
    print()
    print('Ketikkan id untuk menampilkan detail item:')

    return option, n_monsters

## print_lab
'''
'''

def print_lab(monsters_id: list, monster_inventory: list[dict], owca_dex: list[dict]) -> int :

    print('Selamat Datang di Lab Dokter Asep')
    print()
    print('============ MONSTER LIST ============')
    print()
    length = 0
    for id in monsters_id :
        if len(owca_dex[id]['type']) > length :
            length = len(owca_dex[id]['type'])
    
    counter = 1
    for id in monsters_id :
        print(str(counter) + '. ' + owca_dex[id]['type'] + '   ' + ' ' * ((length - len(owca_dex[id]['type'])) + 1) + '(Level: ' + str(monster_inventory[id]['level']) + ')')
        counter += 1

    print(str(counter) + '. Keluar' )

    print('''
============ UPGRADE PRICE ============

1. Level 1 -> Level 2: 300 OC
2. Level 2 -> Level 3: 500 OC
3. Level 3 -> Level 4: 800 OC
4. Level 4 -> Level 5: 1000
              
=======================================
''')
    
    return counter

## print_peta
'''
'''

def print_peta(login_now, data_peta) -> tuple[int, int]:
    x = 0
    y = 0

    for i in range(12) :
        baris = ''
        for j in range(12) :
            if data_peta[i][j] == 'P' :
                x = j
                y = i
    
    print(f"Agent {login_now['username']} di posisi ({x - 1},{y - 1}) ")
    print()

    for i in range(12) :
        baris = ''
        for j in range(12) :
            if j > 0 :
                baris += ' ' + data_peta[i][j]

            else :
                baris += data_peta[i][j]

        print(baris)

    print()

    return x, y