# K03-F | bonus -> B03 - Monster Ball

# Import Libraries & Module
from random_number_generator import *

# Definisi fungsi
## monster_ball
'''

'''

### Kamus Lokal
'''
'''

### Algoritma
def monster_ball(turn: int, battle: bool, enemy_stats: dict, login_now: dict, invento_stock: list[list], monster_inventory: list[dict], item_inventory: list[dict]) -> bool :

    idx: int = -1

    for rows in range(len(item_inventory)) :
        if item_inventory[rows]['type'] == "monster_ball" :
            idx = rows
    
    if idx == -1 :
        print("Anda tidak memiliki Monster Ball di dalam Inventory!")
    
    else :
        chance         : int = RNG(1,100)
        check_inventory: bool = False
        for rows in range(len(invento_stock)) :
            if invento_stock[rows][1] == enemy_stats['type'] :
                check_inventory = True
                
        if check_inventory :
            turn -= 1
            print('Anda sudah memiliki monster', enemy_stats['type'], 'di dalam inventory')       
        
        if not check_inventory :
            if enemy_stats['level'] == 1 :
                if 1 <= chance <= 75 :
                    item_inventory[idx]['quantity'] -= 1
                    print("Sisa Monster Ball Anda:", item_inventory[idx]['quantity'])
                    monster_inventory.append({'user_id' : login_now['user_id'], 'monster_id' : enemy_stats['id'], 'level' : enemy_stats['level']})
                    battle = False

                else :
                    print("Yahh, Anda belum berhasil mendapatkan monster", enemy_stats['type'])
                    
            elif enemy_stats['level'] == 2 :
                if 1 <= chance <= 50 :
                    item_inventory[idx]['quantity'] -= 1
                    print("Sisa Monster Ball Anda:", item_inventory[idx]['quantity'])
                    monster_inventory.append({'user_id' : login_now['user_id'], 'monster_id' : enemy_stats['id'], 'level' : enemy_stats['level']})
                    battle = False

                else :
                    print("Yahh, Anda belum berhasil mendapatkan monster", enemy_stats['type'])

            elif enemy_stats['level'] == 3 :
                if 1 <= chance <= 25 :
                    item_inventory[idx]['quantity'] -= 1
                    print("Sisa Monster Ball Anda:", item_inventory[idx]['quantity'])
                    monster_inventory.append({'user_id' : login_now['user_id'], 'monster_id' : enemy_stats['id'], 'level' : enemy_stats['level']})
                    battle = False

                else :
                    print("Yahh, Anda belum berhasil mendapatkan monster", enemy_stats['type'])

            elif enemy_stats['level'] == 4 :
                if 1 <= chance <= 10 :
                    item_inventory[idx]['quantity'] -= 1
                    print("Sisa Monster Ball Anda:", item_inventory[idx]['quantity'])
                    monster_inventory.append({'user_id' : login_now['user_id'], 'monster_id' : enemy_stats['id'], 'level' : enemy_stats['level']})
                    battle = False

                else :
                    print("Yahh, Anda belum berhasil mendapatkan monster", enemy_stats['type'])

            else :
                if 1 <= chance <= 5 :
                    item_inventory[idx]['quantity'] -= 1
                    print("Sisa Monster Ball Anda:", item_inventory[idx]['quantity'])
                    monster_inventory.append({'user_id' : login_now['user_id'], 'monster_id' : enemy_stats['id'], 'level' : enemy_stats['level']})
                    battle = False

                else :
                    print("Yahh, Anda belum berhasil mendapatkan monster", enemy_stats['type'])

    return turn, battle