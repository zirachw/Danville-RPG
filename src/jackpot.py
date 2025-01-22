
import time
from random_number_generator import *
from helper import *
from printer import *

def jackpot(login_now: dict, user: list[str], monster_inventory: list[str], owca_dex: list[str]) -> None :

    os.system('cls')
    print_animated("Tes Keberuntungan Anda!")
    time.sleep(3)
    os.system('cls')

    panas     : bool = True
    items     : list = ['Hat', 'Sword', 'Coin', 'Potion', 'Monster', '7']
    monster_id: int  = RNG(1, len(owca_dex) - 1)
    monster   : str  = owca_dex[monster_id]['type']
    while panas :
        print_jackpot(monster)
        validator: bool = False

        while not validator :
            sure: str = input('       Mulai bermain (Y/N) : ').upper()

            if sure == 'Y' or sure == 'N':
                validator = True

            else :
                print('          Input tidak valid')
                time.sleep(1)
                os.system('cls')
                print_jackpot(monster)

        print()
        sum_oc: int = 0
        if sure == 'Y' :
            if user[login_now['user_id']]['oc'] >= 500 :
                st: int = items[RNG(0,5)]
                time.sleep(0.1)
                nd: int = items[RNG(0,5)]
                time.sleep(0.1)
                rd: int = items[RNG(0,5)]

                gacha: list = [st, nd, rd]

                print('=====================================')
                print('|  ' + st + ' ' * (9 - len(st))  + '|  ' + nd + ' ' * (9 - len(nd))  + '|  ' + rd + ' ' * (9 - len(rd))  + '|')
                print('=====================================')
                
                if st == nd and st == rd :
                    if st == '7' :
                        print('SUPER JACKPOT!!! Selamat, Anda mendapatkan 5000 OC dan', monster)

                    else :
                        print('JACKPOT!!! Selamat, Anda mendapatkan monster ' + monster + '.')
                    
                    time.sleep(2)
                    os.system('cls')

                    have: bool = False
                    for rows in range(len(monster_inventory)) :
                        if monster_inventory[rows]['user_id'] == login_now['user_id'] and monster_inventory[rows]['monster_id'] == monster_id :
                            print('Anda telah memiliki Monster ini, Hadiah akan dikonversi menjadi 1000 OC')
                            sum_oc = 1000
                            have = True

                    if not have :
                        monster_inventory += [{'user_id' : login_now['user_id'], 'monster_id' : monster_id, 'level' : 1 }]
                        print('Monster telah ditambahkan ke dalam inventory Anda.')
                        time.sleep(1)

                else :
                    for item in gacha :
                        if item == 'Hat' :
                            sum_oc += 10
                        
                        elif item == 'Sword' :
                            sum_oc += 20
                        
                        elif item == 'Coin' :
                            sum_oc += 50
                        
                        elif item == 'Potion' :
                            sum_oc += 100
                        
                        elif item == 'Monster' :
                            sum_oc += 200
                        
                        else :
                            sum_oc += 500

                user[login_now['user_id']]['oc'] = user[login_now['user_id']]['oc'] + sum_oc - 500
                print()
                time.sleep(1)
                print(sum_oc, 'OC telah ditambahkan ke akun Anda!')
                input()

            else :
                print('Mff, Anda tidak memiliki cukup OC untuk bermain JACKPOT.')

        else :
            time.sleep(1)
            os.system('cls')
            print_animated('Keluar dari JACKPOT')
            panas = False

        time.sleep(1)
        os.system('cls')