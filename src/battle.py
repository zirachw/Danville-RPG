# K03-F | src -> F08 - Battle

# Import Libraries & Module
import os
import time
from typing import TextIO
from inventory import *
from printer import *
from helper import *
from random_number_generator import *
from monster import *
from potion import *
from monster_ball import *

# Definisi fungsi
## ally
'''
merupakan fungsi yang menampilkan ui monster yang kita miliki, mengembalikan stats dari monster yang kita miliki
'''

### Algoritma
def ally(choose_monster: int, login_now: dict, monsters_id: list, monster_inventory: list[str], owca_dex: list[str]) :
    ally_id   : int  = monsters_id[choose_monster - 1]
    ally_level: int  = monster_inventory[ally_id]['level'] 

    ## Ally Atributes by Level
    ally_type : str  = owca_dex[ally_id]['type']
    ally_atk  : int  = int(owca_dex[ally_id]['atk_power'] * (100 + (ally_level - 1) * 10) / 100)
    ally_def  : int  = int(owca_dex[ally_id]['def_power'] * (100 + (ally_level - 1) * 10) / 100)
    ally_hp   : int  = int(owca_dex[ally_id]['hp']        * (100 + (ally_level - 1) * 10) / 100)
    ally_stats: dict = {'id' : ally_id, 'level' : ally_level, 'type' : ally_type, 'atk' : ally_atk, 'def' : ally_def, 'hp' : ally_hp}

    # Print Ally
    print(
"""    ∧＿∧
  ( ・∀・)
  (つ⑩  つ
   |     |
   ∪￣∪
""")
    print("RAWRRR, " + login_now['username'] + " mengeluarkan monster Pikachow !!!")
    print()
    print_stats(ally_type, ally_level, ally_atk, ally_def, ally_hp)
    print()

    return ally_stats

# Definisi fungsi
## enemy
'''
merupakan fungsi yang menampilkan ui monster musuh, mengembalikan stats dari monster musuh
'''

### Algoritma
def enemy(enemy_level: int, owca_dex: list[str]) :

    ## Getting Each Monster User have
    enemy_id   : int  = RNG(2, len(owca_dex) - 1)
    ## Enemy Atributes by Level
    enemy_type : str  = owca_dex[enemy_id]['type']
    enemy_atk  : int  = int(owca_dex[enemy_id]['atk_power'] * (100 + (enemy_level - 1) * 10) / 100)
    enemy_def  : int  = int(owca_dex[enemy_id]['def_power'] * (100 + (enemy_level - 1) * 10) / 100)
    enemy_hp   : int  = int(owca_dex[enemy_id]['hp']        * (100 + (enemy_level - 1) * 10) / 100)
    enemy_stats: dict = {'id' : enemy_id, 'level' : enemy_level, 'type' : enemy_type, 'atk' : enemy_atk, 'def' : enemy_def, 'hp' : enemy_hp}

    ## Print Enemy
    print(
"""_.___.
 /      \ 
| () () |
 \  ^  /
  ||||
  ||||
""")
    print("RAWRRR, Monster", owca_dex[enemy_id]['type'], "telah muncul !!!")
    print()
    print_stats(enemy_type, enemy_level, enemy_atk, enemy_def, enemy_hp)
    print()

    return enemy_stats

# Definisi fungsi
## battle
'''
merupakan fungsi yang menampilkan UI battle yang menampilkan beberapa pilihan, lalu mengembalikan data sesuai masukan dari pengguna
'''


### Algoritma
def battle(option: int, choose_monster: int, enemy_stats: dict, login_now: dict, user: list, owca_dex: list, monster_inventory: list, item_inventory: list) -> tuple[int, bool] :
    monsters_id: list = get_monsters_id(login_now, monster_inventory)
    time.sleep(1)
    ally_stats: dict = ally(choose_monster, login_now, monsters_id, monster_inventory, owca_dex)

    ## Accesing Inventories
    invento_stock: list = get_inventories(login_now, monsters_id, monster_inventory, item_inventory, owca_dex)
    stats        : list = {'win' : True, 'stage' : enemy_stats['level'] - 1, 'ally_sum' : 0, 'enemy_sum' : 0, 'enemy_id' : enemy_stats['id']}

    ## Initializing Condition
    battle       : bool = True
    turn         : int  = 1  

    ## Main Program  
    while battle:
        ## For Different RNG
        time.sleep(1)

        ## Ally Turn
        if turn % 2 == 1 :
            
            if turn != 1 :
                print(
"""    ∧＿∧
  ( ・∀・)
  (つ⑩  つ
   |     |
   ∪￣∪
""")

            ## Print Option
            print("============ TURN", turn , ally_stats['type'] , "============")
            if option == 3 :
                print(
'''
    1. Attack
    2. Use Potion
    3. Quit 
'''
    )
            if option == 4 :
                print(
'''
    1. Attack
    2. Use Potion
    3. Use Monster Ball
    4. Quit 
'''
    )
            choose_battle: int = is_input_valid(option, "perintah")

            ## Attack
            if choose_battle == 1 :
                ### Statistics
                ally_attack    : float = (RNG(ally_stats['atk'] * 70/100, ally_stats['atk'] * 130/100))
                ally_percentage: int   = int((ally_attack - ally_stats['atk']) / ally_stats['atk'] * 100)
                ally_reduced   : float = ally_attack * enemy_stats['def'] / 100
                ally_results   : int   = ally_attack - ally_reduced
                
                stats['ally_sum'] += ally_results
                enemy_stats['hp'] = int(enemy_stats['hp'] - (ally_results))

                if enemy_stats['hp'] < 0 :
                    enemy_stats['hp'] = 0

                print("UWOGHHH", ally_stats['type'], "menyerang", enemy_stats['type'])
                print_stats(enemy_stats['type'], enemy_stats['level'], enemy_stats['atk'], enemy_stats['def'], enemy_stats['hp'])     
                print_results(ally_attack, ally_reduced, enemy_stats['def'], ally_results, ally_percentage)
                print()

            ## Use Potion
            elif choose_battle == 2 :
                turn = potion(turn, ally_stats, invento_stock, owca_dex)

            ## Use Monster Ball if BATTLE / Quit if ARENA
            elif choose_battle == 3 :
                if option == 3 :
                    stats['win']   = False
                    battle = False           
                    oc: int = ending(option, login_now, stats, user, owca_dex)

                elif option == 4 :
                    oc: int = 0
                    turn, battle = monster_ball(turn, battle, enemy_stats, login_now, invento_stock, monster_inventory, item_inventory)

            ## Quit if BATTLE 
            elif choose_battle == 4 :
                if option == 4 :
                    stats['win']   = False
                    battle = False         
                    oc: int = ending(option, login_now, stats, user, owca_dex)

        elif turn % 2 == 0 :
            if turn != 2 :
                print(
"""_.___.
 /      \ 
| () () |
 \  ^  /
  ||||
  ||||
""")
            print("============ TURN", turn , enemy_stats['type'] , "============")
            enemy_attack    : float = (RNG(enemy_stats['atk'] * 70/100, enemy_stats['atk'] * 130/100))
            enemy_percentage: int   = int((enemy_attack - enemy_stats['atk']) / enemy_stats['atk'] * 100)
            enemy_reduced   : float = (enemy_attack * ally_stats['def'] / 100)
            enemy_results   : float = enemy_attack - enemy_reduced
            stats['enemy_sum'] += enemy_results

            ally_stats['hp'] = int(ally_stats['hp'] - int(enemy_results))
            if ally_stats['hp'] < 0 :
                ally_stats['hp'] = 0

            print("UWOGHHH", enemy_stats['type'], "menyerang", ally_stats['type'])
            print_stats(ally_stats['type'], ally_stats['level'], ally_stats['atk'], ally_stats['def'], ally_stats['hp'])
            print_results(enemy_attack, enemy_reduced, ally_stats['def'], enemy_results, enemy_percentage) 
            print()

        if enemy_stats['hp'] == 0 :
            stats['stage'] += 1
            stats['win'] = True
            battle = False     
            oc: int = ending(option, login_now, stats, user, owca_dex)

        elif ally_stats['hp'] == 0 :
            stats['win'] = False
            battle = False
            oc: int = ending(option, login_now, stats, user, owca_dex)

        turn += 1

    return oc, stats['win']

# Definisi fungsi
## ending
'''
merupakan fungsi yang menampilkan tampilan sesuai dengan kondisi dari pengguna, lalu mengembalikan sebuah data oc yang telah diubah
'''

def ending(option: int, login_now: dict, stats: list, user: list, owca_dex: list) -> int :
    if option == 3 :   

        if stats['stage'] == 0 :
            oc = 0
        elif stats['stage'] == 1 :
            oc = 20
        elif stats['stage'] == 2 :
            oc = 50
        elif stats['stage'] == 3 :
            oc = 100
        elif stats['stage'] == 4 :
            oc = 170 
        else :
            oc = 260

        if stats['win'] == True :
            print('Selamat, Anda berhasil mengalahkan monster', owca_dex[stats['enemy_id']]['type'], '!!!')
            print()
            print('STAGE CLEARED! Anda akan mendapatkan', oc, 'OC pada sesi ini')
            print()
            if stats['stage'] == 5 :
                print('Selamat, Anda Berhasil menyelesaikan seluruh stage Arena !!!')
                print()
                print('============== STATS ==============')
                print('Total Hadiah      :', oc, 'OC')
                print('Jumlah stage      :', stats['stage'])
                print('Damage diberikan  :', stats['ally_sum'])
                print('Damage diterima   :', stats['enemy_sum']) 

        elif stats['win'] == False :
            print('Yahh Anda dikalahkan monster ' + str(owca_dex[stats['enemy_id']]['type']) + '. Jangan menyerah, coba lagi !!!')
            print()
            print('GAME OVER! Sesi latihan berakhir pada stage ' + str(stats['stage']) + '!')
            print()
            print('============== STATS ==============')
            print('Total Hadiah      :', oc, 'OC')
            print('Jumlah stage      :', stats['stage'])
            print('Damage diberikan  :', int(stats['ally_sum']))
            print('Damage diterima   :', int(stats['enemy_sum'])) 

    elif option == 4 :
        if stats['win'] == True :
            oc: int = RNG(5,30)
            print("Selamat, Anda berhasil mengalahkan monster", owca_dex[stats['enemy_id']]['type'], "!!!")
            print()
            print("Total OC yang diperoleh:", oc)
            print()
            print('============== STATS ==============')
            print('Total Hadiah      :', oc, 'OC')
            print('Damage diberikan  :', int(stats['ally_sum']))
            print('Damage diterima   :', int(stats['enemy_sum'])) 

        else :
            oc: int = 0
            print("Yahhh, Anda dikalahkan monster " + owca_dex[stats['enemy_id']]['type'] + ". Jangan menyerah, coba lagi !!!")

    return oc