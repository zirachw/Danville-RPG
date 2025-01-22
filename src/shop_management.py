
from shop import *
from monster import *
from inventory import *

def add_monster_data(monster_id, monster_shop, stock, price) -> list[dict]:
    
    data = []
    insert = 1

    for idx in range(1, len(monster_shop)) :
        if monster_id < monster_shop[idx]['monster_id'] :
            insert = idx
            break

    counter = 0
    for row in monster_shop :
        if counter < insert :
            data += [row]

        else :
            data += [{'monster_id' : monster_id, 'stock' : stock, 'price' : price}]
            break
        
        counter += 1

    counter = 0
    for row in monster_shop :
        if counter >= insert :
            data += [row]

        counter += 1
    
    return data

def add_item_data(item_id, item_shop, not_in_shop, stock, price) :
    data = []
    insert = 1
    type = ['type', 'strength', 'resilience', 'healing', 'monster_ball']

    for idx in range(1, len(not_in_shop)) :
        if item_id < not_in_shop[idx]['id'] :
            insert = idx
            break

    counter = 0
    for row in item_shop :
        if counter < insert :
            data += [row]

        else :
            data += [{'type' : type[item_id], 'stock' : stock, 'price' : price}]
            break
        
        counter += 1

    counter = 0
    for row in item_shop :
        if counter >= insert :
            data += [row]

        counter += 1

    return data

def shop_management(login_now: dict, item_shop: list[dict], monster_inventory: list[dict], owca_dex: list[dict], monster_shop: list[dict]) -> tuple[list[dict], list[dict]]:
    print('Selamat Datang kembali,', login_now['username'])
    shop: bool = True
    
    monster_in_shop = merge_monster(monster_shop, owca_dex)
    item_in_shop  = merge_item(item_shop)

    while shop :
        action = is_action_valid('shop_admin')
        if action == 'lihat' :

            pick = is_action_valid('lihat')
            time.sleep(1)
            os.system('cls')

            if pick == 'monster' :

                time.sleep(0.5)
                print_animated("Sedang menyiapkan Monster")
                time.sleep(1)
                os.system('cls')

                print_all(monster_in_shop, 'Monsters Shop')
            
            else :
                    
                os.system('cls')
                time.sleep(0.5)
                print_animated("Sedang menyiapkan Item")
                time.sleep(1)
                os.system('cls')

                print_all(item_in_shop, 'Items Shop')

            input()
            os.system('cls')

        elif action == 'tambah' :
            pick = is_action_valid(action)
            if pick == 'monster' :
                in_shop = [row["monster_id"] for row in monster_shop]
                not_in_shop = [{'id' : 'ID', 'type' : 'Type', 'atk_power' : 'ATK Power', 'def_power' : 'DEF Power', 'hp' : 'HP'}]
                
                for rows in owca_dex[1:]:
                    found = False
                    for id in in_shop[1:] :
                        if id == rows['id'] :
                            found = True

                    if not found :
                        data = {'id'        : rows['id'],
                                'type'      : rows['type'],
                                'atk_power' : rows['atk_power'],
                                'def_power' : rows['def_power'],
                                'hp'        : rows['hp'],}

                        not_in_shop += [data]
                
                if not_in_shop == [{'id' : 'ID', 'type' : 'Type', 'atk_power' : 'ATK Power', 'def_power' : 'DEF Power', 'hp' : 'HP'}] :
                    print('Seluruh Monster telah ada di SHOP')

                else :
                    print_all(not_in_shop, 'Monsters Data')

                    monster_id = is_id_valid(not_in_shop, 'monster')
                    stock      = validate_add('stock')
                    price      = validate_add('price')

                    monster_shop = add_monster_data(monster_id, monster_shop, stock, price)
                    print_all(monster_shop, 'd')
                    monster_in_shop = merge_monster(monster_shop, owca_dex)
                    print(owca_dex[monster_id]['type'], 'telah berhasil ditambahkan ke dalam shop!')

                time.sleep(2)
                os.system('cls')

            else : ## {pick == potion}
                in_shop = ['type', 'strength', 'resilience', 'healing', 'monster_ball']
                not_in_shop = [{'id' : 'ID', 'type' : 'Type'}]
     
                for type in range(1, len(in_shop)) :
                    
                    check = False
                    for rows in item_shop :
                        if rows['type'] == in_shop[type] :
                            check = True

                    if check == False :
                        not_in_shop += [{'id' : (type), 'type': in_shop[type]}]
                
                if not_in_shop == [{'id' : 'ID', 'type' : 'Type'}] :
                    print('Seluruh Item telah ada di SHOP')

                else :
                    print_all(not_in_shop, 'Items Data')

                    item_id    = is_id_valid(not_in_shop, 'item')
                    stock      = validate_add('stock')
                    price      = validate_add('price')
                    
                    item_shop = add_item_data(item_id, item_shop, not_in_shop, stock, price)
                    print(item_shop)
                    print(not_in_shop)
                    item_in_shop  = merge_item(item_shop)
                    print_all(item_shop, 'Items Data')
                    input()

                    if in_shop[item_id] == 'strength' :
                        desc = 'Strength Potion'
                            
                    elif in_shop[item_id]== 'resilience' :
                        desc = 'Resilience Potion'
                            
                    elif in_shop[item_id] == 'healing' :
                        desc = 'Healing Potion'
                
                    else :
                        desc = 'Monster Ball'

                    print(desc, 'telah berhasil ditambahkan ke dalam shop!')
                    print()
                time.sleep(2)
                os.system('cls')

        elif action == 'ubah' :
            pick = is_action_valid(action)
            if pick == 'monster': 
                in_shop = [{'id' : row["monster_id"]} for row in monster_shop]

                print_all(monster_in_shop, 'Monsters Shop')
                monster_id = is_id_valid(in_shop, 'monster')
                stock      = validate_mod('stock')
                price      = validate_mod('price')
                print(stock, price, " ")
                print(monster_id)
                for row in monster_shop :
                    print(row['monster_id'], monster_id)
                    if row['monster_id'] == monster_id :
                        if stock != '' :
                            print(stock)
                            row['stock'] = stock
                        
                        if price != '' :
                            print(price, '.')
                            row['price'] = price

                        print(monster_shop)
                        print(owca_dex[(row['monster_id'])]['type'] + ' telah berhasil diubah')
                        print('Stok baru :', row['stock'])
                        print('Harga baru:', row['price'])
                
                monster_in_shop = merge_monster(monster_shop, owca_dex)

            elif pick == 'item' :  
                in_shop = [{'id' : row['id'], 'type' : row['type']} for row in item_in_shop]
                print_all(item_in_shop, 'Items Shop')
                item_id = is_id_valid(in_shop, 'item')
                stock      = validate_mod('stock')
                price      = validate_mod('price')

                for idx in range(len(item_in_shop)) :
                    if item_in_shop[idx]['id'] == item_id :
                        item_id = idx

                for row in item_shop :
                    
                    if row['type'] == 'strength' :
                        type = 'Strength Potion'
                    
                    elif row['type'] == 'resilience' :
                        type = 'Resilience Potion'
                    
                    elif row['type'] == 'healing' :
                        type = 'Healing Potion'

                    else :
                        type = 'Monster Ball'

                    print(row['type'], type, in_shop[item_id]['type'])

                    if type == in_shop[item_id]['type'] :
                        print('kena')
                        if stock != '' :
                            row['stock'] = stock
                        
                        if stock != '' :
                            row['price'] = price
                    
                        print(type  + ' telah berhasil diubah')
                        print('Stok baru :', row['stock'])
                        print('Harga baru:', row['price'])

                item_in_shop = merge_item(item_shop)
        
        elif action == 'hapus' :
            pick = is_action_valid(action)
            if pick =='monster':

                print_all(monster_in_shop, 'Monsters Shop')
                monster_id = is_id_valid(monster_in_shop, 'monster')
                sure    = sure_validator('Apakah Anda yakin menghapus Monster dari shop ')

                for idx in range(len(monster_in_shop)) :
                    if monster_in_shop[idx]['id'] == monster_id :
                        monster_id = idx

                if sure :
                    data   : list[dict] = []
                    counter: int        = 0

                    for row in monster_shop :
                        if counter != idx :
                            data += [row]

                        counter += 1

                    monster_shop = data
                
                monster_in_shop = merge_monster(monster_shop, owca_dex)

            elif pick  == 'item':
                in_shop = [{'id' : row['id']} for row in item_in_shop]
                print_all(item_in_shop, 'Items Shop')
                item_id = is_id_valid(in_shop, 'item')
                sure    = sure_validator('Apakah Anda yakin menghapus Item dari shop ')

                for idx in range(len(in_shop)) :
                    if in_shop[idx]['id'] == item_id :
                        item_id = idx

                if sure :
                    data   : list[dict] = []
                    counter: int        = 0

                    for row in item_shop :
                        if counter != idx :
                            data += [row]

                        counter += 1

                    item_shop = data
                
                item_in_shop = merge_item(item_shop)


        else :
            shop = False         
            print('Dadah ' + login_now['username'] + ' sampai jumpa lagi!')

    return monster_shop, item_shop