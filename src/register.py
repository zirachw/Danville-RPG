# K03-F | src -> F01 - Register

# Import Libraries & Module
from printer import *
from helper import *

# Definisi fungsi
## register
'''
Fungsi register adalah fungsi yang menerima pembuatan user baru jika status dalam keadaan tidak login, dan akan melakukan
pengecekan validasi kredensial login username dan password, lalu akan memilih starter monster untuk 
user baru.
'''

def register(login_now: dict, user: list[dict], monster_inventory: list[dict], owca_dex: list[dict]) -> tuple[dict, bool, int] :
    new       : bool = False
    choose_new: int  = 0

    if login_now['status'] == True :
        print(
'''Register gagal!
Anda telah login dengan username ''' + user[login_now['user_id']]['username'] + ''', silakan lakukan "LOGOUT" sebelum melakukan login kembali.
'''
)
        time.sleep(3)
        os.system('cls')

    else :
        print('Buat Username dan Passowrd Anda')
        username: str = input('Username: ')
        password: str = input('Password: ')
        if is_username_valid(username) :
            if is_username_taken(user, username) :    
                print('Username sudah terpakai, silakan gunakan username lain!')

            else :
                new = True
                login_now: dict = {'user_id' : len(user), 'username' : username, 'role' : 'agent', 'status' : True}
                new_data:  dict = {'id' : len(user), 'username' : username, 'password' : password, 'role' : 'agent', 'oc' : 0}
                user += [new_data]

                os.system('cls')
                print('Register berhasil!')
                time.sleep(1.5)
                os.system('cls')

                print()
                print('Silakan pilih salah satu monster sebagai monster awalmu.')
                print_type(owca_dex)
                print()
                choose_new = is_input_valid(len(owca_dex) - 1, 'register')
                print()
                time.sleep(1)
                os.system('cls')

                print('Selamat datang Agent', username,'. Mari kita mengalahkan Dr. Asep Spakbor dengan Charizard!')
                print('Masukkan command "HELP" untuk daftar command yang dapat kamu panggil')
                monster_inventory += [{'user_id' : login_now['user_id'], 'monster_id' : choose_new, 'level' : 1}]

        else :
            print('Username hanya boleh berisi alfabet, angka, underscore, dan strip')
            print()

    return login_now, new, choose_new