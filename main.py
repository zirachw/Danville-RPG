# K03-F | main -> main.py

# Import Libraries
import os
from typing import TextIO
import sys

# Clear Terminal
os.system('cls')

# Read path
sys.path.append('src')

## Utils
from read_csv import *
from printer import *
from helper import *

## Spesifikasi
from random_number_generator import *
from register import *
from login import *
from logout import *
from help import *
from monster import *
from potion import *
from inventory import *
from battle import *
from arena import *
from shop import *
from laboratory import *
from monster_management import *
from shop_management import *
from load import *
from save import *
from jackpot import *
from peta import *
from exit import *

## Read Data
user, owca_dex, item_inventory, monster_inventory, item_shop, monster_shop = load()

## Initialisation
login_now: dict = {'user_id' : '', 'username' : '', 'role' : '', 'status' : False}
end: bool = False

## Main Program
while end == False :
    if login_now['role'] == '' : 
        print('''
==========================================
|    Selamat Datang di kota Danville!    |
==========================================
  ~  Petualangan Besar menunggu Anda!  ~    

Halooo, Butuh bantuan?
Ketik HELP untuk melihat menu
~ The Mighty God
''')
        action: str = input('>>> ').upper()
        time.sleep(1)
        os.system('cls')

        if action == 'REGISTER' :
            login_now, new, choose_new = register(login_now, user, monster_inventory, owca_dex)

            if login_now['role'] == 'agent' :
                login_now, end = peta(end, login_now, user, item_shop, monster_inventory, item_inventory, owca_dex, monster_shop)

        elif action == 'LOGIN' :
            login_now = login(user, login_now)

            if login_now['role'] == 'agent' :
                login_now, end = peta(end, login_now, user, item_shop, monster_inventory, item_inventory, owca_dex, monster_shop)

        elif action == 'LOGOUT' :
            login_now = logout(login_now)

        elif action == "HELP" :
            helps(login_now)
        
        elif action == 'SAVE' :
            save(user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)

        elif action == 'EXIT' :
            end = exits(end, user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)

        else :
            print('Input tidak valid')

    elif login_now['role'] == 'admin' :
        print('Selamat datang, Admin!')
        print('Masukkan command "help" untuk daftar command yang dapat kamu panggil')

        action: str = input('>>> ').upper()
        time.sleep(1)
        os.system('cls')

        if action == 'MONSTER' :
            monster = monster_management(owca_dex)
            
        elif action == 'SHOP' :
            monster_shop, item_shop = shop_management(login_now, item_shop, monster_inventory, owca_dex, monster_shop)

        elif action == 'DATABASE' : 

            print_all(user, 'Users')
            print()

            print_all(monster_inventory, 'Monsters of All User')
            print()

            print_all(item_inventory, 'Items of All User')
            print()

            print_all(monster_shop, 'Monsters Available')
            print()

            print_all(item_shop, 'Items Available')
            print()

            print_all(owca_dex, 'Owca-Dex')

        elif action == 'SAVE' :
            save(user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)

        elif action == 'LOGOUT' :
            login_now = logout(login_now)

        elif action == 'HELP' :
            helps(login_now)

        elif action == 'EXIT' :
            end = exits(end, user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)
        else :
            print('Input tidak valid')

    
