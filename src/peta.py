import os
from typing import TextIO
from helper import *
from logout import *
from help import *
from inventory import *
from battle import *
from arena import *
from shop import *
from laboratory import *
from monster_management import *
from save import *
from exit import *
from jackpot import *

def peta(end: bool, login_now: dict, user: list[dict], item_shop: list[dict], monster_inventory: list[dict], item_inventory: list[dict], owca_dex: list[dict], monster_shop: list[dict]) -> bool :

    danville: list[str] = convert_peta(r"data\peta.txt")
    loopbreak: bool = False

    while not loopbreak :
        x, y = print_peta(login_now, danville)
        action: str = input('>>> ').upper()

        if action == "UP":
            if danville[y-1][x] != " ":
                print_animated('Agent ' + login_now['username'] + ' tidak bisa pindah karena terdapat Obstacle!')

            else:
                print_animated('Agent ' + login_now['username'] + " akan pindah ke atas!")
                danville[y][x] = " "
                danville[y-1][x] = "P"
                
        elif action == "DOWN":
            if danville[y+1][x] != " ":
                print_animated('Agent ' + login_now['username'] + ' tidak bisa pindah karena terdapat Obstacle!')
            else:
                print_animated('Agent ' + login_now['username'] + " akan pindah ke bawah!")
                danville[y][x] = " "
                danville[y+1][x] = "P"

        elif action == "RIGHT":
            if danville[y][x+1] != " ":
                print_animated('Agent'  + login_now['username'] + ' tidak bisa pindah karena terdapat Obstacle!')

            else:
                print_animated('Agent ' + login_now['username'] + " akan pindah ke kanan!")
                danville[y][x] = " "
                danville[y][x+1] = "P"

        elif action == "LEFT":
            if danville[y][x-1] != " ":
                print_animated('Agent ' + login_now['username'] + ' tidak bisa pindah karena terdapat Obstacle!')
            else:
                print_animated('Agent ' + login_now['username'] + " akan pindah ke kiri!")
                danville[y][x] = " "
                danville[y][x-1] = "P"

        elif action == 'INVENTORY' :
            inventory(login_now, monster_inventory, item_inventory, owca_dex, user)
            
        elif action == "SHOP":
            if danville[y+1][x] == "S" or danville[y-1][x] == "S" or danville[y][x-1] == "S" or danville[y][x+1] == "S":
                
                shop(login_now, user, item_shop, monster_inventory, item_inventory, owca_dex, monster_shop)

            else:
                print('Agent ' + login_now['username'] + ' tidak berada di area Shop!')

        elif action == "ARENA":
            if danville[y+1][x] == "A" or danville[y-1][x] == "A" or danville[y][x-1] == "A" or danville[y][x+1] == "A":
                print_animated("Mengakses Arena!")
                option = 3
                oc = arena(option, login_now, user, owca_dex, monster_inventory, item_inventory)
                user[login_now['user_id']]['oc'] += oc

            else:
                print('Agent ' + login_now['username'] + ' tidak berada di area Arena!')

        elif action == "LABORATORY":
            if danville[y+1][x] == "L" or danville[y-1][x] == "L" or danville[y][x-1] == "L" or danville[y][x+1] == "L":
                monsters_id = get_monsters_id(login_now, monster_inventory)
                lab(login_now, user, monsters_id, monster_inventory, owca_dex)
                
            else:
                print('Agent ' + login_now['username'] + ' tidak berada di area Lab!')

        elif action == "BATTLE":
            if danville[y+1][x] == "X" or danville[y-1][x] == "X" or danville[y][x-1] == "X" or danville[y][x+1] == "X":
                print_animated("Mengakses BATTLE!")
                option = 4
                enemy_level: int = RNG(1, 5)
                enemy_stats = enemy(enemy_level, owca_dex)
                choose_monster = get_monster(login_now, monster_inventory, owca_dex)
                oc, win = battle(option, choose_monster, enemy_stats, login_now, user, owca_dex, monster_inventory, item_inventory)
                user[login_now['user_id']]['oc'] += oc

            else:
                print('Agent ' + login_now['username'] + ' tidak berada di area Bush untuk melakukan Battle!')

        elif action == "JACKPOT" :
            if danville[y+1][x] == "J" or danville[y-1][x] == "J" or danville[y][x-1] == "J" or danville[y][x+1] == "J":
                jackpot(login_now, user, monster_inventory, owca_dex)

            else :     
                print('Agent ' + login_now['username'] + ' tidak berada di area GACHA!')

        elif action == "HELP":
            helps(login_now)
        
        elif action == 'LOGOUT' : 
            login_now = logout(login_now)
            loopbreak = True

        elif action == 'SAVE' :
            save(user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)
            
        elif action == 'EXIT' :
            loopbreak = True
            end = exits(end, user, owca_dex, monster_inventory, item_inventory, monster_shop, item_shop)

        else:
            print("Maaf command yang diketik tidak diketahui! ketik HELP untuk melihat list command!")

        input()
        os.system('cls')
        
    return login_now, end