# K03-F | src -> F03 - Logout

from printer import *
# Definisi fungsi
## logout
'''
fungsi yang menerima 1 masukan dictionary login_now dan mengeluarkan 
user dari akun yang sedang dipakai sesuai status login user
'''

def logout(login_now: dict) -> dict :
        
    if login_now['status'] == True :
        login_now: dict = {'user_id' : '', 'username' : '', 'role' : '', 'status' : False}
        os.system('cls')
        print_animated('Logout berhasil!')
        time.sleep(1)
        os.system('cls')

    else :
        os.system('cls')
        print(
'''Logout gagal!
Anda belum login, silakan login terlebih dahulu sebelum melakukan logout
''')
        time.sleep(3)
        os.system('cls')

    return login_now