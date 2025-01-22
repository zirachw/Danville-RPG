# K03-F | src -> F11 - Laboratory

# Import Libraries & Module
import os
from helper import *
from printer import *

os.system('cls')

# Definisi fungsi
## laboratory
'''
fungsi yang menampilkan antarmuka laboratorium yang memungkinkan pengguna untuk meng-upgrade monster yang dimilikinya sesuai dengan
inventorynya dan akan mengembalikan monster yang sudah diupgrade
'''

def lab(login_now: dict, user: list[dict], monsters_id: list[dict], monster_inventory: list[dict], owca_dex: list[dict]) -> None :

    os.system('cls')
    print_animated("Mengakses Lab")
    time.sleep(1)
    os.system('cls')
    
    upgrade: bool = False
    while not upgrade :

        valid: bool = False

        while not valid :

            counter: int = print_lab(monsters_id, monster_inventory, owca_dex)
            choice : str = input("Pilih monster: ")

            if is_number(choice) :
                if int(choice) < 1 or int(choice) > counter :
                    print("Pilihan monster tidak tersedia!")
                    time.sleep(1)
                    os.system('cls')

                else :
                    valid = True
                
            else :
                print('Input tidak valid')
            
            time.sleep(1)
        
        monster_id: int = int(choice)

        if monster_id == counter :

            os.system('cls')
            print_animated("Keluar dari Lab")
            time.sleep(1)
            os.system('cls')

            upgrade = True

        elif monster_inventory[monsters_id[monster_id - 1]]['level'] < 5 :
            print(owca_dex[monsters_id[monster_id - 1]]['type'] + ' akan di-upgrade ke level ' + str(monster_inventory[monsters_id[monster_id - 1]]['level'] + 1) + '.' )
            
            oc : int = 0

            if monster_inventory[monsters_id[monster_id - 1]]['level'] == 1 :
                oc = 300

            elif monster_inventory[monsters_id[monster_id - 1]]['level'] == 2 :
                oc = 500

            elif monster_inventory[monsters_id[monster_id - 1]]['level'] == 3 :
                oc = 800

            else : 
                oc = 1000

            print('Harga untuk melanjutkan upgrade ' + owca_dex[monsters_id[monster_id - 1]]['type'] + ' adalah ' + str(oc) + ' OC.')

            sure: bool = sure_validator('Lanjutkan upgrade ')
            if sure :
                if user[login_now['user_id']]['oc'] >= oc :
                    monster_inventory[monsters_id[monster_id - 1]]['level'] += 1
                    user[login_now['user_id']]['oc'] -= oc
                    
                    os.system('cls')
                    print_animated('Monster sedang di-upgrade')
                    time.sleep(1)
                    print()
                    print('Selamat, ' + owca_dex[monsters_id[monster_id - 1]]['type'] + ' berhasil di-upgrade ke level ' + str(monster_inventory[monsters_id[monster_id - 1]]['level']) + ' !')
                    time.sleep(2)
                    os.system('cls')

                else :
                    print()
                    print_animated(owca_dex[monsters_id[monster_id - 1]]['type'] + ' gagal di-upgrade, OC Anda kurang')
                    time.sleep(2)   

            else :
                print()
                print_animated(owca_dex[monsters_id[monster_id - 1]]['type'] + ' gagal di-upgrade')
                time.sleep(2)
    
        else :
            print('Maaf, monster yang Anda pilih sudah memiliki level maksimum')

        os.system('cls')