# K03 - F | src -> F14 - Load

# Import Libraries & Modules
import argparse
from read_csv import *
from printer import *
import time

# Definisi fungsi
## load
'''
fungsi untuk memuat data user dari berbagai data csv yang ada di dalam folder yang diberikan
'''

def load() -> tuple[list[dict], list[str], list[str], list[str], list[str], list[str]] :

    parser = argparse.ArgumentParser(usage="python main.py <nama_folder>") 
    parser.add_argument("nama_folder", help="Name of the folder",nargs='?')
    args   = parser.parse_args()

    folder    = args.nama_folder
    data_path = 'data/' + folder if folder else 'data/'
    
    if data_path == 'data/':
        print("Tidak ada nama folder yang diberikan!")
        print("Usage : python main.py <nama_folder>")
        exit()

    elif os.path.exists(data_path) == False :
        print('Folder "' + data_path + '" tidak ditemukan')
        exit()
        
    else:
        print_animated("Mengambil data permainan")
        time.sleep(2)
        print('Memulai Permainan!')
        time.sleep(1)
        os.system('cls')
        user             : list[dict] = read_csv('user.csv', data_path)
        owca_dex         : list[dict] = read_csv('monster.csv', data_path)
        item_inventory   : list[dict] = read_csv('item_inventory.csv', data_path)
        monster_inventory: list[dict] = read_csv('monster_inventory.csv', data_path)
        item_shop        : list[dict] = read_csv('item_shop.csv', data_path)
        monster_shop     : list[dict] = read_csv('monster_shop.csv', data_path)

    return user, owca_dex, item_inventory, monster_inventory, item_shop, monster_shop