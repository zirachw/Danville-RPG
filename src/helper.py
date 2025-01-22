# K03-F | utils -> helper

# Import Libraries
import os
import time
from typing import TextIO
os.system('cls')

# Definisi fungsi
## is_number
'''
'''

def is_number(element : str) -> bool :
    numbers = "0123456789"
    check = False
    for char in element :
        check = False

        for number in numbers :
            if char == number :
                check = True

        if check == False :
            return check

    return check

## is_username_valid
'''
fungsi yang menerima 1 masukan string username kemudian 
mengecek dan mengeluarkan input, yaitu True jika username 
sesuai format dan False jika username tidak sesuai format
'''

def is_username_valid(username : str) -> bool :

    isValid = False

    for char in username :

        if 65 <= ord(char) <= 90 :
            isValid = True

        elif 97 <= ord(char) <= 122 :
            isValid = True
        
        elif ord(char) == 45 :
            isValid = True

        elif ord(char) == 95 :
            isValid = True

        else :
            isValid = False
            break
    
    return isValid

## is_username_taken
'''
fungsi yang menerima 1 masukan string username kemudian 
mengecek dan mengeluarkan input, yaitu True jika username 
sudah ada dan False jika username belum ada
'''

def is_username_taken(list_of_dict: list[dict], username: str) -> bool :
    taken: bool = False
    for rows in range(len(list_of_dict)) :
        if list_of_dict[rows]["username"] == username :
            taken = True
    
    if taken :
        return True
    
    else :
        return False

## password_check
'''
fungsi yang menerima 1 masukan string username kemudian 
mengecek dan mengeluarkan input, yaitu True jika password 
sesuai dan False jika password tidak sesuai
'''

def password_check(list_of_dict: list[dict], username: str, password: str) -> int :
    valid: bool = False
    for rows in range(len(list_of_dict)) :
        if list_of_dict[rows]['username'] == username :
            if list_of_dict[rows]['password'] == password :
                valid = True
    if valid :
        return True
    
    else :
        return False

## get_user_id
'''
fungsi yang menerima masukan 1 list of dictionary dan 1 masukan
string username kemudian mengeluarkan user_id dari username tersebut
'''

def get_user_id(list_of_dict : list[dict], username: str) -> int :
    counter: int = -1
    for rows in range(len(list_of_dict)) :
        counter += 1
        if list_of_dict[rows]["username"] == username :
            return counter
        
def is_input_valid(avai : int, desc : str) -> int :
    valid = False

    while valid == False :
        if (desc == 'register') :
            inputs = input("Monster pilihanmu: ")

            if is_number(inputs) :
                if int(inputs) < 1 or int(inputs) > avai :
                    print("Monster yang dipilih tidak ada")

                else :
                    valid = True
                
            else :
                print('Input tidak valid')

        elif (desc == 'monster') or (desc == 'item'):
            inputs = input("Masukkan id " + desc + ": ")

            if is_number(inputs) :
                if int(inputs) < 1 or int(inputs) > avai :
                    print("Pilihan nomor tidak tersedia!")

                else :
                    valid = True
                
            else :
                print('Input tidak valid')
        
        elif (desc == 'jumlah') :
            inputs = input("Masukkan jumlah: ")

            if is_number(inputs) :
                if int(inputs) > avai :
                    print("Stok tidak cukup!")

                elif int(inputs) < 1 :
                    print('Setidaknya beli 1 bang :/')

                else :
                    valid = True
                
            else :
                print('Input tidak valid')    
   
        else :
            inputs = input("Pilih " + desc + ": ")

            if is_number(inputs) :
                if int(inputs) < 1 or int(inputs) > avai :
                    print("Pilihan nomor tidak tersedia!")

                else :
                    valid = True
                
            else :
                print('Input tidak valid')
    
    return int(inputs)

## is_action_valid
'''
'''

def is_action_valid(desc: str) -> str :
    valid = False

    while valid == False :
        if desc == 'shop_agent' :
            inputs = input('>>> Pilih aksi (lihat/beli/keluar) : ')
            actions = ['lihat', 'beli', 'keluar']

        elif desc == 'shop_admin' :
            inputs = input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar) : ')
            actions = ['lihat', 'tambah', 'ubah', 'hapus', 'keluar']

        elif (desc == 'lihat') or (desc == 'beli') or (desc == 'tambah') or (desc == 'ubah') or (desc == 'hapus') :
            inputs = input('>>> Mau ' + str(desc) + ' apa? (monster/item): ')
            actions = ['monster', 'item']

        for action in actions :
            if inputs == action :
                valid = True

        if not valid :
            print('Pilihan aksi tidak tersedia!')

    return inputs

## is_id_valid
'''
'''

def is_id_valid(not_in_shop: list[dict], desc : str) :
    valid = False

    while not valid :
        inputs = input('Masukkan id ' + desc + ': ')

        if is_number(inputs) :
            for rows in range(1, len(not_in_shop)) :
                if int(inputs) == not_in_shop[rows]['id'] :
                    valid = True

            if not valid :
                print('Pilihan tidak tersedia')
        else :
            print('Input tidak valid')  



    return int(inputs)

## validate_add
'''
'''

def validate_add(desc) -> int :
    valid = False

    while not valid :
        if desc == 'stock' :
            inputs = input("Masukkan stok awal: ")

        else :
            inputs = input('Masukkan harga: ')

        if is_number(inputs) :
            valid = True
            
        else :
            print('Input tidak valid')  

    if not valid :
        print('Pilihan monster tidak tersedia')

    return int(inputs)

## validate_add
'''
'''

def validate_mod(desc) -> int :
    valid = False

    while not valid :
        if desc == 'stock' :
            inputs = input("Masukkan stok baru: ")

        else :
            inputs = input('Masukkan harga baru: ')

        if is_number(inputs) or inputs == '' :
            if is_number(inputs) :
                inputs = int(inputs)

            valid = True
            
        else :
            print('Input tidak valid')  

    return inputs

## sure_validator
'''
'''

def sure_validator(desc: str) -> bool :
    valid = False
    
    while not valid :
        inputs = input(desc + '(Y/N): ')

        if inputs.upper() == 'Y' or inputs.upper() == 'N':
            valid = True
            if inputs.upper() == 'Y' :
                return valid

            else :
                return not valid
        else :
            return not valid

## is_name_taken
'''
'''

def is_name_taken(owca_dex: list[dict]) -> str :

    valid = False
    while not valid :
        type = input('Masukkan Type / Nama : ')
        taken = False
        for rows in range(len(owca_dex)) :
            if owca_dex[rows]['type'] == type :
                taken = True
        
        if taken :
            print('Nama sudah terdaftar coba lagi')

        else :
            if type == '' :
                print('Input tidak valid!')

            else :
                valid = True

    return type

## stats_validator
'''
''' 

def stats_validator(desc : str) -> str :

    valid = False

    while not valid :
        inputs = input('Masukkan ' + desc + ' : ')

        numbers = "0123456789"
        check = False
        for char in inputs :
            check = False
            for number in numbers :
                if char == number :
                    check = True

            if not check :
                print('Masukkan input bertipe Integer Positif, coba lagi!')
                break

        if check :
            if desc == 'DEF Power (0-50)' :
                if 0 <= int(inputs) <= 50 :
                    valid = True

                else :
                    print('DEF Power harus bernilai 0-50, coba lagi')
            else :
                valid = True
    

    return inputs

## convert_peta
'''
'''

def convert_peta(path: str) -> list[str] :
    file: TextIO = open(path, 'r')

    data_peta: list[str] = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

    for row in file :
        temp: list = []
        row : str = row.rstrip()
        temp += ['*']

        for char in row :
            
            if char == '#' :
                char = ' '

            temp += [char]
        temp += ['*']
        
        data_peta += [temp]
    
    data_peta += [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

    return data_peta