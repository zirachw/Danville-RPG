# K03-F | monster -> F06 - Potion

# Importing Libraries & Modules
from helper import *

# Definisi fungsi
## laboratory
'''
fungsi yang menerima masukan string yang berisi jenis dari potion yang digunakan dan mengembalikan
stat yang dipengaruhi akibat dari potion yang digunakan
'''

def potion_categories(name: str) -> str :
    desc: str = ''
    if name == 'Strength' :
        desc = 'ATK'

    elif name == 'Resilience' :
        desc = 'DEF'

    elif name == 'Healing' :
        desc = 'Heal'

    return desc

## check_potion
'''
merupakan fungsi yang menerima masukan string serta dictionary yang mengembalikan boolean 
yang menentukan
'''

def check_potion(name_potion: str, potion_count: dict, potion_used: dict) -> bool :
    if potion_count[name_potion] == 0 :
        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan yang lain")

    elif potion_used[name_potion] == True :
        print(
'''
Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia menolaknya
seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi
''')
        return True
    
    else :
        return False

## potion
'''
merupakan fungsi yang menerima masukan dari pengguna kemudian menampilkan ui yang menampilkan jenis potion 
beserta jumlahnya, potion yang dimiliki kemudian bisa digunakan dalam battle sesuai efeknya masing masing
'''

def potion(turn: int, ally_stats: dict, invento_stock: list[list], owca_dex: list[dict]) -> int :
    turns      : int = turn
    choosing   : bool = True
    potion_qty : dict = {'Strength' : 0, 'Resilience' : 0, 'Healing' : 0}
    potion_used: dict = {'Strength' : False, 'Resilience' : False, 'Healing' : False }

    for rows in range(len(invento_stock))  :
        if invento_stock[rows][0] == 'Potion' :
            for key, value in potion_qty.items() :
                if invento_stock[rows][1] == key :
                    potion_qty[key] = invento_stock[rows][2]

    print(potion_qty)
    print("============ POTION LIST ============")
    print('1. Strength     ' + '(Qty: ' + str(potion_qty['Strength'])   + ') - ' + potion_categories('Strength'))   
    print('2. Resilience   ' + '(Qty: ' + str(potion_qty['Resilience']) + ') - ' + potion_categories('Resilience'))
    print('3. Healing      ' + '(Qty: ' + str(potion_qty['Healing'])    + ') - ' + potion_categories('Healing'))
    print('4. Cancel')

    while choosing == True :
        
        choose_potion: int = is_input_valid(4, "perintah")

        if 1 <= choose_potion <= 3 :
            if choose_potion == 1 :
                type_potion = 'Strength'

            elif choose_potion == 2 :
                type_potion = 'Resilience'

            else :
                type_potion = 'Healing'

            if potion_qty[type_potion] == 0 :
                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan yang lain")

            else :
                if potion_used[type_potion] :
                    print(
'''
Kamu mencoba memberikan ramuan ini kepada Pikachow, namun dia menolaknya
seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi
''')
                else :
                    if choose_potion == 1 :
                        ally_stats['atk'] = (int(ally_stats['atk'] * 105 / 100))
                        potion_qty['Strength'] -= 1
                        potion_used['Strength'] = True
                        choosing = False

                    elif choose_potion == 2 :
                        ally_stats['def'] = (int(ally_stats['def'] * 105 / 100))
                        potion_qty['Resilience'] -= 1
                        potion_used['Resilience'] = True
                        choosing = False

                    else :
                        potion_qty['Healing'] -= 1
                        potion_used['Healing'] = True
                        ally_stats['hp'] = (ally_stats['hp'] + (int(owca_dex[ally_stats['id']]['hp'] * 25 / 100)))                         
                        choosing = False
        else :
            turns -= 1
            choosing = False

    return turns