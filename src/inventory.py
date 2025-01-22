# K03-F | src -> F07 - Inventory

# Import Libraries & Module
import os
import time
from typing import TextIO

from helper import *
from printer import *
from monster import *
from potion import *

os.system('cls')

# Definisi fungsi
## get_inventories
'''
fungsi yang mengambil seluruh item yang dimiliki oleh user
'''

def get_inventories(login_now: dict, monsters_id: list[str], monster_inventory: list[str], item_inventory: list[str], owca_dex: list[str]) -> list[list] :

    temp = []

    for id in monsters_id :
        idx = 0
        for row in range(len(monster_inventory)) :
            if monster_inventory[row]['monster_id'] == id :
                idx = row

        nama  : str  = owca_dex[id]['type']
        level : int  = monster_inventory[idx]['level']
        hp    : int  = owca_dex[id]['hp']
        stats : list = ['Monster', nama, level, hp]
        temp += [stats]

    for rows in range(len(item_inventory)) :
        if (item_inventory[rows]['user_id'] == login_now['user_id']) and (item_inventory[rows]['quantity'] > 0) :
            type             : str = item_inventory[rows]['type']
            if type != 'monster_ball' :
                type_capitalized : str  = type[0].upper() + type[1:]
                desc             : str  = potion_categories(type_capitalized)
                qty              : int  = item_inventory[rows]['quantity']
                stats            : list = ['Potion', type_capitalized, qty, desc]
                temp += [stats]

    for rows in range(len(item_inventory)) :
        if (item_inventory[rows]['user_id'] == login_now['user_id']) and (item_inventory[rows]['quantity'] > 0)  :
            type             : str = item_inventory[rows]['type']

            if type == 'monster_ball' :
                type_capitalized : str  = type[0].upper() + type[1:7] + ' '+ type[8].upper() + type[9:]
                qty              : int  = item_inventory[rows]['quantity']
                stats            : list = ['Monster Ball', type_capitalized, qty, "Get Monster"] 
                temp += [stats]

    return temp

## inventory
'''
fungsi yang menerima 1 masukan string user_id dan menampilkan
seluruh monster dan item yang memiliki oleh user tersebut.
'''

def inventory(login_now: dict, monster_inventory: list[str], item_inventory: list[str], owca_dex: list[str], user: list[str]) -> None :
    
    os.system('cls')
    print_animated("Mengakses Inventory-mu")
    time.sleep(1)
    os.system('cls')

    monsters_id : list      = get_monsters_id(login_now, monster_inventory)
    invento_stock: list[str] = get_inventories(login_now, monsters_id, monster_inventory, item_inventory, owca_dex)
    
    exit : bool = False
    while exit == False :

        n_monsters : int       = 0
        option, n_monsters = print_inventory(n_monsters, login_now, user, invento_stock)

        validator = False

        while validator == False :
            id = input("Masukkan id inventory: ")

            if is_number(id) :
                if int(id) < 1 or int(id) > option :
                    print("Pilihan nomor tidak tersedia!")

                else :
                    validator = True
                
            else :
                print('Input tidak valid')
                time.sleep(1)
                os.system('cls')
                option, n_monsters = print_inventory(option, n_monsters, login_now, user, invento_stock)

        
        time.sleep(1)
        os.system('cls')

        search : int = int(id)

        if search == option :
            print_animated("Keluar dari Inventory")
            time.sleep(1)
            exit = True
    
        else:
            if invento_stock[search - 1][0] == 'Monster' :
                type     : str = owca_dex[monsters_id[search - 1]]['type']
                atk_power: int = owca_dex[monsters_id[search - 1]]['atk_power']
                def_power: int = owca_dex[monsters_id[search - 1]]['def_power']
                hp       : int = owca_dex[monsters_id[search - 1]]['atk_power']
                level    : int = invento_stock[search - 1][2]

                print('============='+ '=' * len(type) + '===')
                print('| Monster    '+ ' ' * len(type) + '  |')
                print('============='+ '=' * len(type) + '===')
                print('| Name      :', type      , '|')
                print('| ATK Power :', atk_power , ' ' * (len(type) - len(str(atk_power)) - 1), '|')
                print('| DEF Power :', def_power , ' ' * (len(type) - len(str(def_power)) - 1), '|')
                print('| HP        :', hp        , ' ' * (len(type) - len(str(hp))        - 1), '|')
                print('| Level     :', level     , ' ' * (len(type) - len(str(level))     - 1), '|')
                print('==============' + '=' * len(type) + '==')
                print()

            elif invento_stock[search - 1][0] == 'Potion' :
                counter_idx = 0
                for rows in range(len(invento_stock)) :
                    if invento_stock[rows][0] == 'Potion' :
                        counter_idx += 1

                        if counter_idx == search - n_monsters :
                            type = invento_stock[rows][3]
                            qty  = invento_stock[rows][2]
                            
                            print('============'+ '=' * len(type) + '===')
                            print('| Potion    '+ ' ' * len(type) + '  |')
                            print('============'+ '=' * len(type) + '===')
                            print('| Type     :', type, '|')
                            print('| Quantity :', qty , ' ' * (len(type) - len(str(qty)) - 1), '|')
                            print('============'+ '=' * len(type) + '===')
                            print()
            else :
                for rows in range(len(invento_stock)) :
                    if invento_stock[rows][0] == 'Monster Ball' :
                        qty = invento_stock[rows][2]
                        print('=============='+ '=' * len(str(qty))  + '=')
                        print('| Monster Ball'+ ' ' * len(str(qty))  + '|')
                        print('=============='+ '=' * len(str(qty))  + '=')
                        print('| Quantity :'  , qty ,                  '|')
                        print('=============='+ '=' * len(str(qty))  + '=')
                        print()
            input()

        os.system('cls')