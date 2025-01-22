# K03-F | src -> F04 - Help

# Definisi fungsi
## help
'''
fungsi yang menerima 1 masukan dictionary login_now dan mengeluarkan 
opsi apa saja yang dapat dilakukan oleh user sesuai role user
'''

def helps(login_now: dict) -> None :
    if login_now['status'] == True :

        if login_now['role'] == 'agent' :
            print(
f'''==================================  HELP  ==================================

Halo agent {login_now['username']}. Kamu memanggil command HELP. Kamu memilih jalan yang
benar, semoga kamu tidak sesat kemudian. Berikut List Command yang dapat dilakukan:

    1.  Logout     : Keluar dari akun yang sedang digunakan
    2.  Exit       : Keluar dari Kota Danville
    3.  Right      : Bergerak ke Kanan   
    4.  Left       : Bergerak ke Kiri
    5.  Up         : Bergerak ke Atas
    6.  Down       : Bergerak ke Bawah
    7.  Shop       : Membeli Monster dan Item   (hanya berlaku jika sedang di sekitar sisi "S")
    8.  Laboratory : Upgrade level monster      (hanya berlaku jika sedang di sekitar sisi "L")
    9.  Battle     : Melawan monster lain       (hanya berlaku jika sedang di sekitar sisi "X")
    10. Arena      : Mengakses Arena            (hanya berlaku jika sedang di sekitar sisi "A")
    11. Jackpot    : Tes Keberuntungan          (hanya berlaku jika sedang di sekitar sisi "J")
    
Footnote:
    1. Untuk menentukan aplikasi, silakan masukan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
'''
)

        elif login_now['role'] == 'admin' :
            print(
'''==================================  HELP  ==================================

Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

    1. Logout    : Keluar dari akun yang sedang digunakan
    2. Exit      : Keluar dari Kota Danville
    2. Shop      : Melakukan manajemen pada SHOP sebagai tempat jual beli
                   peralatan agent
    3. Monster   : Melakukan manajemen pada Database Monster

Footnote:
    1. Untuk menentukan aplikasi, silakan masukan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
'''
)

    else :
        print(
'''==================================  HELP  ==================================

Kamu belum login sebagai role apapun. Silakan login terlebih dahulu.

    1. Login    : Masuk ke dalam akun yang sudah terdaftar
    2. Register : Membuat akun baru
    3. Exit     : Keluar dari Kota Danville

Footnote:
    1. Untuk menentukan aplikasi, silakan masukan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
'''
)
