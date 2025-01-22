# IF1210 - Dasar Pemrograman 2024
> Tugas Besar - IF1210 Dasar Pemrograman 2024
Kelompok K03 - F

# About
Tugas besar ini meminta untuk membuatkan program sebuah permainan RPG (Role Playing Game) dimana kita berperan sebagai agen O.W.C.A (Organisasi Warga Cool Abiez) yang ingin membantu Purry si Platypus mengalahkan Dr, Asep Spakbor, caranya yaitu dengan melatih monster-monster yang kita miliki untuk mengalahkan monster-monster kuat yang dimiliki oleh Dr. Asep Spakbor, Latar permainan dimulai di hutan terpencil di pinggir kota danvile untuk mencari monster-monster yang akan membantu dalam mengahkan Dr. Asep Spakbor. Role didalam permainan ini dibagi menjadi dua yaitu agent sebagai orang yang ingin mengalahkan monster-monster dan juga Admin sebagai pengelola dari kota Danville.

# Contributors
1. Razi Rachman Widyadhana	19623163
2. M. Abizzar Gamadrian	19623173
3. Achmad Arians Fadhil	16523253
4. Monika Edith Amadea Purba	16523093
5. Emir Rasyadi Mas Avicen	16523113

# Features
- F14 (Load) yaitu fungsi yang menjalankan source code utama di terminal dengan menyertakan lokasi penyimpanan file csv. data game dari csv kemudian akan dibaca dan dipindahkan kedalam sebuah dictionary ataupun sebuah array yang akan diakses dan diubah selama program berjalan.
- F00 (Random Number Generator) merupakan fungsi yang memberikan nilai-nilai secara  acak yang kemudian digunakan untuk menentukan kemungkinan-kemungkinan yang dapat terjadi didalam game
- F01 (Register) merupakan fungsi yang memungkinkan pengguna untuk membuat akun sebagai agent yang kemudian datanya akan masuk ke database sehingga pengguna dapat melakukan login dengan akun tersebut
- F02 (Login) fungsi yang memungkinkan pengguna meluntuk akukan login dengan akun yang sudah ada didalam database, ada 2 jenis akun yang bisa diakses oleh pengguna, yaitu Agent dan Admin yang memiliki akses yang berbeda-beda
- F03 (Logout) fungsi yang digunakan untuk keluar dari akun, hanya dapat diakses jika pengguna sudah login terlebih dahulu
- F04 (Menu & Help) fungsi yang menampilkan semua command yang dapat dilakukan oleh pengguna, fungsi ini akan menampilkan tampilan yang berbeda sesuai dengan status login-nya
- F05 (Monster) fungsi yang digunakan untuk merekam data monster yang ada yang kemudian dapat digunakan sesuai dengan kebutuhan pengguna
- F06 (Potion) fungsi yang digunakan untuk merekam data potion yang ada didalam database yang kemudian dapat digunakan sesuai dengan kebutuhan pengguna
- F07 (Inventory) fungsi yang memungkinkan pengguna untuk mengecek inventory yang mereka miliki sesuai dengan akun yang sedang login, Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Agent
- F08 (Battle) fungsi yang memungkinkan pengguna untuk melakukan battle dengan monster yang tipenya akan muncul secara acak berdasarkan random number generator, Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Agent
- F09 (Arena) fungsi yang memungkinkan pengguna untuk berlatih dengan bertarung dengan monster didalam arena yang jika kemudian menyelesaikan stage dari arena tersebut akan mendapatkan hadiah sesuai dengan tingkat kesulitan stage, Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Agent
- F10 (Shop & Currency) merupakan fungsi yang memungkinkan pengguna untuk mengakses Shop untuk melakukan pembelian monster dan ataupun potion sesuai dengan harganya masing-masing, Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Agent
- F11 (Laboratory) fungsi yang memungkinkan bagi pengguna untuk mengakses laboratory untuk melakukan upgrade terhadap monster yang dimiliki, semakin tinggi level monster yang ingin di-upgrade maka semakin tinggi pula harga untuk upgrade monster tersebut. Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Agent
- F12 (Shop Management) fungsi yang memungkinkan bagi admin untuk melihat, mengubah, serta menghapus monster ataupun potion yang dijual didalam Shop, Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Admin
- F13 (Monster Management) fungsi yang memungkinkan untuk admin melakukan perubahan database monster yang ada dengan melakukan penambahan jenis monster yang baru, Fungsi ini adalah fungsi khusus yang hanya dapat diakses oleh Admin
- F15 (Save) fungsi yang digunakan untuk menyimpan data yang telah diubah oleh pengguna selama permainan kedalam file eksternal csv baru
- F16 (Exit) fungsi yang digunakan untuk keluar dari program, pengguna dapat memilih untuk keluar tanpa melakukan penyimpanan data terlebih dahulu ataupun dengan melakukan penyimpanan data.
- B03 (Monster Ball) fungsi yang memungkinkan bagi pengguna untuk melakukan penangkapan monster yang telah ia lawan dengan kemungkinan keberhasilan yang acak
- B04 (JACKPOT!!!) fungsi yang memungkinkan bagi agent untuk mengundi keberuntungannya dengan membayar sejumlah uang, hasil yang didapatkan diacak sesuai dengan RNG
- B05 (Peta Kota Danville) fungsi yang memungkinkan bagi agent untuk mengelilingi kota danville, dan juga untuk mengakses tempat tempat yang ada didalam kota danville

# How to Run
```
python main.py
```
