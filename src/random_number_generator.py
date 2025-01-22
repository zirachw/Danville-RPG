# K03-F | F00 - Random Number Generator

# Import Libraries
import os
from datetime import datetime

os.system('cls')

# Kamus Local
'''
## Linear Congruential Generator
m           : int   {dengan  rentang  m >= 0         sebagai  "modulus atau sisa bagi"}
a           : int   {dengan  rentang  0 <= a < m     sebagai  "pengali"               }
c           : int   {dengan  rentang  0 <= a < m     sebagai  "penambah"              }
seed        : int   {dengan  rentang  0 <= seed < m  sebagai  "nilai awal"            }
n           : int   {dengan  rentang  n >= 0         sebagai  "suku bilangan ke-"     }
i           : int   {dengan  rentang  0 <= i < n     sebagai  "iterator for loop"     }

## Limiter
lower_bound : int   {batas bawah nilai random yang dapat dikeluarkan}
upper_bound : int   {batas atas  nilai random yang dapat dikeluarkan}
range       : int   {rentang     nilai random yang dapat dikeluarkan}
'''

# Output Optimisation with Maximum Period
'''
~ Hull-Dobel Theorem ~

Ketika c != 0, pemilihan parameter yang baik memungkinkan periode dapat sepanjang m,
untuk semua kondisi awal. Hal ini terjadi, jika dan hanya jika

1. m dan c koprima atau secara matematis ialah fpb(m,c) = 1
2. a - 1 dapat dibagi semua faktor prima dari m
3. a - 1 dapat dibagi 4 jika m dapat dibagi 4

Bentuk ini dapat digunakan untuk sembarang m, namun hanya bekerja dengan baik untuk
m yang memiliki banyak faktor prima yang berulang, seperti perpangkatan angka 2.

Jika m bilangan bebas-kuadrat, akibatnya a ≡ 1 mod m, menjadikannya pembangkit acak
yang sangat buruk. Pengali dengan periode maksimum hanya tersedia ketika m memiliki
faktor prima yang berulang.

Pasangan parameter optimal yang umum digunakan salah satunya dari Numerical Recipes
m = 2 ** 32, a = 1664525, c = 1013904223
'''

# Definisi fungsi
## random_number_generator
'''
fungsi yang menerima 2 masukan lower_bound dan upper_bound, kemudian mengeluarkan 
sebuah angka random dengan algoritma Linear Congruential Generator dalam rentang
di antara lower_bound dan upper_bound
'''

def random_number_generator(lower_bound : int, upper_bound : int) -> int :

    ### From Hull-Dobel Theorem
    m = 2 ** 32
    a = 1664525
    c = 1013904223

    ### seed taken from microsecond of the current time
    seed = datetime.now().microsecond       

    ### generating random number with LCG
    seed = (a * seed + c) % m

    ### limiting the range of random number expected
    range = (upper_bound - lower_bound) + 1

    ### return random number in limited range
    return lower_bound + (seed % range)