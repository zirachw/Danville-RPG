
from helper import *
from printer import *

# Defini fungsi
## monster_management
'''
menampilkan beberapa opsi yaitu menampil semua monster yang ada pada data owcadex, 
menambahkan monster baru pada data owcadex dengan menentukan: (nama, attack power, 
defense power, dan hp monster), dan opsi keluar dari tampilan monster management.  
'''

def monster_management(owca_dex: list[dict]) -> list[dict] :
        
    loop: bool = True 
    while loop :
        
        valid: bool = False
        while not valid :
            print('''Selamat Datang di Database Para Monster
1. Tampilkan semua Monster
2. Tambah Monster baru
3. Keluar
''')  
            inputs: str = input("Pilih aksi: ")

            if is_number(inputs) :
                if int(inputs) < 1 or int(inputs) > 3 :
                    print("Pilihan nomor tidak tersedia!")

                else :
                    valid = True
                
            else :
                print('Input tidak valid')

            time.sleep(2)
            os.system('cls')

        action: int = int(inputs)

        if action == 1 :
            print_all(owca_dex, 'Owca-Dex') 
            input()
            os.system('cls')

        elif action == 2 :
            print_animated('Memulai pembuatan monster baru')
            print()

            name     : str = is_name_taken(owca_dex)
            atk_power: int = stats_validator('ATK Power')
            def_power: int = stats_validator('DEF Power (0-50)')
            hp       : int = stats_validator('HP')
            time.sleep(2)

            print('Pokemon baru berhasil dibuat')
            print('Type     : ', name)
            print('ATK Power: ', atk_power)
            print('DEF Power: ', def_power)
            print('HP       : ', hp)

            stats: dict = {'id' : len(owca_dex), 'type' : name, 'atk_power' : atk_power, 'def_power' : def_power, 'hp' : hp}
            owca_dex += [stats]

            input()
            os.system('cls')

        else :
            loop = False

    return owca_dex