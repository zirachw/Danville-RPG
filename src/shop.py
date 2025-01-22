from printer import *
from monster import *
from inventory import *
from read_csv import *

# Definisi fungsi
## merge_monster
'''
fungsi yang menggabungkan data dari monster yang dibeli dengan yang ada diinventory dan
mengeluarkan dictionary baru dengan data yang sudah tergabung
'''

def merge_monster(monster_shop: list[dict], owca_dex: list[dict]) -> list[dict] :
    merged: list[dict] = [{'id' : 'ID', 
                           'type' : 'Type', 
                           'atk_power' : 'ATK Power', 
                           'def_power' : 'DEF Power', 
                           'hp' : 'HP', 
                           'stock' : 'Stok', 
                           'price' : 'Harga'}]

    for row in monster_shop[1:] :
        merged += [{'id' : row['monster_id'],
                      'type' : owca_dex[row['monster_id']]['type'],
                      'atk_power' : owca_dex[row['monster_id']]['atk_power'],
                      'def_power' : owca_dex[row['monster_id']]['def_power'],
                      'hp' : owca_dex[row['monster_id']]['hp'],
                      'stock' : row['stock'],
                      'price' : row['price']}]

    return merged

## merge item
'''
fungsi yang menggabungkan data dari potion yang dibeli dengan yang ada diinventory dan
mengeluarkan dictionary baru dengan data yang sudah tergabung
'''

def merge_item(item_shop: list[dict]) -> list[dict] :
    merged: list[dict] = [{'id' : 'ID', 
                           'type' : 'Type', 
                           'stock' : 'stok', 
                           'price' : 'harga'}]

    items: list[str] = ['strength', 'resilience', 'healing', 'monster_ball']  

    type: str = ''
    idx : int = 0

    for item in items :
        for row in range(len(item_shop)) :
            if item_shop[row]['type'] == item :

                if item == 'strength' :
                    type = 'Strength Potion'
                    idx = 1

                elif item == 'resilience' :
                    type = 'Resilience Potion'
                    idx = 2

                elif item == 'healing' :
                    type = 'Healing Potion'
                    idx = 3

                else :
                    type = 'Monster Ball'
                    idx = 4

                merged.append({'id' : idx,
                               'type'  : type,
                               'stock' : item_shop[row]['stock'],
                               'price' : item_shop[row]['price']})
    
    return merged

def get_id(in_shop: list[dict]) -> list[dict] :

    id_in_shop: list[dict] = []
    for rows in range(len(in_shop)) :
        id_in_shop += [{'id' : in_shop[rows]['id']}]

## shop
'''
fungsi yang menampilkan antarmuka shop yang memungkinkan pengguna untuk membeli monster/potion yang ada dan 
mengembalikan monster/potion yang dibeli oleh pengguna
'''

def shop(login_now: dict, user: list[str], item_shop: list[str], monster_inventory: list[str], item_inventory: list[str], owca_dex: list[str], monster_shop: list[str]) :

    os.system('cls')
    print_animated("Mengakses Shop")
    time.sleep(1)
    os.system('cls')
    
    shop: bool = True

    monsters_id    : list[dict] = get_monsters_id(login_now, monster_inventory)
    invento_stock  : list[list] = get_inventories(login_now, monsters_id, monster_inventory, item_inventory, owca_dex)

    monster_in_shop: list[dict] = merge_monster(monster_shop, owca_dex)
    item_in_shop   : list[dict] = merge_item(item_shop)

    while shop :

        print('Selamat Datang di SHOP !!!')
        action: str = is_action_valid('shop_agent')

        if action == 'lihat' :

            pick = is_action_valid('lihat')
            time.sleep(1)
            os.system('cls')

            if pick == 'monster' :

                time.sleep(0.5)
                print_animated("Bos Razi sedang menyiapkan Monster")
                time.sleep(1)
                os.system('cls')

                print_all(monster_in_shop, 'Monsters Available')
            
            else :
                    
                os.system('cls')
                time.sleep(0.5)
                print_animated("Bos Razi sedang menyiapkan Item")
                time.sleep(1)
                os.system('cls')

                print_all(item_in_shop, 'Items Available')

            input()

        elif action == 'beli' :

            pick: str = is_action_valid('beli')
            time.sleep(1)
            os.system('cls')

            if pick == 'monster' :
                
                time.sleep(0.5)
                print_animated("Bos Razi sedang menyiapkan Monster")
                time.sleep(1)
                os.system('cls')
                print_all(monster_in_shop, 'Monsters Available')
                print()
                print('Jumlah O.W.C.A Coin-mu sekarang', user[login_now['user_id']]['oc'])
                
                id_in_shop: list[int] = []
                for rows in range(len(monster_in_shop)) :
                    id_in_shop += [{'id' : monster_in_shop[rows]['id']}]
                
                monster_id  : int = is_id_valid(id_in_shop, 'monster')
                in_inventory: bool = False

                for idx in range(len(monster_in_shop)) :
                    if monster_in_shop[idx]['id'] == monster_id :
                        monster_id = idx

                for rows in range(len(invento_stock)) :
                    if monster_in_shop[monster_id]['type'] == invento_stock[rows][1] :
                        in_inventory = True
                        print()
                        print('Monster', monster_in_shop[monster_id]['type'], 'sudah ada dalam inventory-mu!')
                        print_animated('Pembelian dibatalkan')
                        time.sleep(2)

                if not in_inventory :
                    id: int = monster_id
                    for row in range(len(owca_dex)) :
                        if owca_dex[row]['type'] == monster_in_shop[monster_id]['type'] :
                            id = row

                    if user[login_now['user_id']]['oc'] >= monster_shop[monster_id]['price'] :
                        ### Adding new monster to inventory
                        monster_inventory.append({'user_id' : login_now['user_id'], 'monster_id' : id, 'level' : 1})    
                        monster_in_shop[monster_id]['stock'] -= 1
                        monster_shop[monster_id]['stock'] -= 1

                        ## Updating user oc
                        user[login_now['user_id']]['oc'] -= monster_in_shop[monster_id]['price']

                        ## Expected Output
                        os.system('cls')
                        print('Berhasil membeli item: ' + monster_in_shop[monster_id]['type'] + '.')
                        print_animated('Menambahkan monster')
                        time.sleep(2)
                        print()
                        print('Monster sudah masuk ke inventory-mu!')
                        time.sleep(2)

                    else :
                        ## Expected Output
                        print()
                        print('OC-mu tidak cukup.')

            else : ## {pick == item}
                                                
                time.sleep(0.5)
                print_animated("Bos Razi sedang menyiapkan Item")
                time.sleep(1)
                os.system('cls')

                print_all(item_in_shop, 'Items Available')
                print()
                print('Jumlah O.W.C.A Coin-mu sekarang', user[login_now['user_id']]['oc'])     

                id_in_shop: list[str] = []
                for rows in range(len(item_in_shop)) :
                    id_in_shop += [{'id' : item_in_shop[rows]['id']}]

                item_id: int = is_id_valid(id_in_shop, 'item')

                item_format = [{'type' : 'type'},
                                   {'type' : 'strength'},
                                   {'type' : 'resilience'},
                                   {'type' : 'healing'},
                                   {'type' : 'monster_ball'}]

                type = item_format[item_id]['type']

                for idx in range(len(item_in_shop)) :
                    if item_in_shop[idx]['id'] == item_id :
                        item_id = idx

                qty    : int = is_input_valid(item_in_shop[item_id]['stock'], 'jumlah')
                print(item_id)

                if user[login_now['user_id']]['oc'] >= qty * item_in_shop[item_id]['price'] :
                    ### Check if the potion is new or not
                    check_new = False
                  
                    print(item_id)
                    idx = 0
                    for row in range(len(item_inventory)) :
                        if item_inventory[row]['type'] == type and item_inventory[row]['user_id'] == login_now['user_id']:
                            print(item_inventory[row]['type'], type, item_inventory[row]['user_id'], login_now['user_id'], row)
                            check_new = True
                            idx = row

                    if check_new :
                        item_inventory[idx]['quantity'] += qty   

                    else : # {not check_new}
                        item_inventory += [{'user_id' : login_now['user_id'], 'type' : type, 'quantity' : qty}]           

                    item_in_shop[item_id]['stock'] -= qty
                    item_shop[item_id]['stock'] -= qty

                    ## Updating user oc
                    user[login_now['user_id']]['oc'] -= (item_in_shop[item_id]['price'] * qty)

                    ### Expected Output
                    if item_in_shop[item_id]['type'] == 'Strength Potion' :
                        desc = 'Potion of Attack'

                    elif item_in_shop[item_id]['type'] == 'Resilience Potion' :
                        desc = 'Potion of Defense'

                    elif item_in_shop[item_id]['type'] == 'Healing Potion' :
                        desc = 'Potion of Heal'
                    
                    else :
                        desc = 'Monster Ball'

                    os.system('cls')
                    print('Berhasil membeli item: ' + str(qty) + ' ' + desc)
                    print_animated('Menambahkan item')
                    time.sleep(2)
                    print()
                    print('Item sudah masuk ke inventory-mu!')
                    time.sleep(2)

                else :
                    ## Expected Output
                    print()
                    print('OC-mu tidak cukup.')

        else :
            shop = False
            os.system('cls')
            print('Bos Razi bilang makasih, belanja lagi ya nanti :)')
            print_animated('Keluar dari SHOP')
            time.sleep(2)
            
        time.sleep(1)
        os.system('cls')
