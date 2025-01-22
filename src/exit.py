# K03-F | src -> F16 - Exit

# Import Libraries & Modules
from helper import *
from save import *

# Definisi fungsi
## exit
'''
'''

### Algoritma
def exits(end: bool, user: list[dict], owca_dex: list[dict], monster_inventory: list[dict], item_inventory: list[dict], monster_shop: list[dict], item_shop: list[dict]) :
    sure: bool = sure_validator('Apakah Anda ingin menyimpan Progress ')
    if sure :
        save(user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)
        end = True
    
    else :
        end = True

    return end
