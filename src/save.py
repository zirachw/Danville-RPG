# K03 - F | src -> F15 - Save

# Import Libraries & Modules
from read_csv import *

# Definisi fungsi
## save
'''
fungsi untuk menyimpan data user ke dalam data csv yang ada di dalam folder yang diberikan
'''

def save(user: list[dict], owca_dex: list[dict], monster_inventory: list[dict], item_inventory: list[dict], monster_shop: list[dict], item_shop: list[dict]) :
    folder_name: str = input('Masukkan nama folder : ') # Nama folder tempat menyimpan
    
    if folder_name == '' :
        print('Input tidak valid!')
    
    else :
        formatted: str = ''
        for char in folder_name:
            if char == ' ' :
                char = "_"

            formatted += char

        folder_name = 'data/' + formatted

    print(folder_name)
    # Periksa apakah folder sudah ada
    if os.path.exists(folder_name):
        print_animated("Menyimpan data....")

    # Jika tidak ada folder yang tuliskan
    else:
        print_animated("Menyimpan data...")
        os.makedirs(folder_name) # Membuat folder baru

    write_csv('user.csv',user,folder_name)
    write_csv('monster.csv',owca_dex, folder_name)
    write_csv('monster_inventory.csv',monster_inventory,folder_name)
    write_csv('item_inventory.csv',item_inventory,folder_name)
    write_csv('monster_shop.csv',monster_shop, folder_name)
    write_csv('item_shop.csv',item_shop, folder_name)