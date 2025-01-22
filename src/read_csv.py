# K03-F | utils -> read_csv

# Import Libraries
from typing import TextIO
from printer import *
from helper import *

# Definisi fungsi
## read_csv
'''
fungsi yang menerima 1 masukan string path yang merupakan 
file csv yang ingin dibaca dan mengeluarkan matriks sehingga
data dapat diolah lebih lanjut.
'''

def read_csv(file: str, path) -> list[dict] :

    file: TextIO = open(path + '/' + file, 'r')
    list_data: list[str] = []

    for row in file :
        temp: list = []
        string: str = ''

        for char in row :

            if char != "," :
                string += char

            else :
                temp += [string]
                string = ''

        temp += [string[:-1]]
    
        list_data += [temp]

    list_of_dict: list = []

    for row in list_data :
        keys: dict = {}
        
        for columns in range(len(list_data[0])) :

            if is_number(row[columns]) :
                row[columns] = int(row[columns])
                
            keys[list_data[0][columns]] = row[columns]

        list_of_dict += [keys]

    return list_of_dict

## write_csv
'''
fungsi yang menerima masukan 1 string path, 1 list of dictionary, dan
1 strin folder yang merupakan list yang ingin dikonversi dan mengeluarkan 
file csv yang akan terletak di folder yang diinginkan
'''

def write_csv(name : str, list_of_dict : list, folder : str) -> None:
    # Menyalin data dari list of dictionary ke file csv

    file: TextIO = open(os.path.join(folder, name),'w') 

    for dict in list_of_dict : # pengulangan untuk setiap baris pada list of dictionary
        row: str = '' # variabel yang akan diisi dengan element dari dictionary 1 baris
        for key in dict : # pengulanan untuk setiap elemen dalam 1 dictionary
            row += str(dict[key]) + ',' # setiap diambil satu elemen, ditambahkan ';' sebagai pemisah

        row = row[:-1] # Menghilangkan tanda ';' terakhir
        row += '\n' # Membuat pemisah antar baris
        file.write(row) # menuliskan isi sabagai 1 baris ke file csv

    file.close()