# K03-F | src -> F09 - Arena

# Import Libraries & Module
from monster import *
from battle import *

# Definisi fungsi
## arena
'''

'''

### Kamus Lokal
'''
'''

### Algoritma
def arena(option: int, login_now: dict, user: list[dict], owca_dex: list[dict], monster_inventory: list[dict], item_inventory: list[dict]) -> int :

    enemy_stats   : dict = enemy(1, owca_dex)
    choose_monster: dict = get_monster(login_now, monster_inventory, owca_dex)

    oc, win = battle(option, choose_monster,  enemy_stats, login_now, user, owca_dex, monster_inventory, item_inventory)

    if win :
        for stage in range(2, 5 + 1) :
            enemy_stats = enemy(stage, owca_dex)
            oc, win = battle(option, choose_monster, enemy_stats, login_now, user, owca_dex, monster_inventory, item_inventory)
            if not win :
                break

    return oc

            