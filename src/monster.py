# K03-F | src -> F05 - Monster

# Import Library & Module
from helper import *

# Definisi fungsi
## get_monster_id
'''
merupakan fungsi yang menerima masukan data sesuai dengan kondisi login pengguna dan mengembalikan
id dari monster yang dipilih
'''

def get_monsters_id(login_now: dict, monster_inventory: list[dict]) -> list[dict] :
    monsters_id: list = []
    for rows in range(len(monster_inventory)) :
        if monster_inventory[rows]['user_id'] == login_now['user_id'] :
            monsters_id += [monster_inventory[rows]['monster_id']]

    return monsters_id

## get_monster
'''
merupakan fungsi yang menerima masukan data sesuai dengan kondisi login pengguna dan mengembalikan
jenis dari monster yang dipilih
'''

def get_monster(login_now: dict, monster_inventory: list[dict],  owca_dex: list[dict]) -> dict : 
    monsters_id: list = get_monsters_id(login_now, monster_inventory)
    print('============ MONSTER LIST ============')

    counter: int = 0
    for id in monsters_id :
        counter += 1
        print(str(counter) + '. ' + owca_dex[id]['type'])
    print()

    ## Choosing Ally Monster for Battle
    choose_monster: int = is_input_valid(counter, "monster untuk bertarung")

    return choose_monster