# K03-F | src -> F02 - Login

# Import Libraries & Module
from helper import *
from printer import *
import time

# Definisi fungsi
## login
'''
fungsi yang menerima 1 masukan dictionary login_now, yaitu
data berisi user yang login dan apabila tidak login, user
menjadi terlogin.
'''

## Algoritma
def login(user: list[dict], login_now: dict) -> None :
    if login_now['status'] == True :
        print(
'''
Login gagal!
Anda telah login dengan username ''' + user[login_now['user_id']]['username'] + ''', silakan lakukan "LOGOUT" sebelum melakukan login kembali.
'''
)
        print()
    
    else :
        print('Isi Username dan Password Anda')
        username: str = input('Username: ')
        password: str = input('Password: ')
        if is_username_taken(user, username) :
            if password_check(user, username, password) :
                user_id: int = get_user_id(user, username)
                if user[user_id]['role'] == 'agent' :
                    login_now: dict = {'user_id' : user_id, 'username' : username, 'role' : 'agent', 'status' : True}
                    os.system('cls')
                    print('Login berhasil!')
                    print_animated('Mengambil data')
                    time.sleep(1.5)
                    os.system('cls')
                    print('Selamat datang, Agent ' + username + '!')
                    print('Masukkan command "HELP" untuk daftar command yang dapat kamu panggil')
                    print()

                else :
                    login_now: dict = {'user_id' : user_id, 'username' : username, 'role' : 'admin', 'status' : True}
                    os.system('cls')
                    print('Login berhasil!')
                    print_animated('Mengambil data')
                    time.sleep(1.5)
                    os.system('cls')

            else :
                print("Password salah!")
                print()
                time.sleep(1)
                os.system('cls')

        else :
            print("Username tidak terdaftar!")
            time.sleep(1)
            os.system('cls')
            print()

    return login_now