# PROGRAM Bravo
# Bilangan adalah Bravo jika jumlah digit-digitnya habis dibagi oleh setiap digitnya.

# KAMUS
# ribuan, ratusan, puluhan, satuan, n, total : int

# ALGORITMA

# Soal ini kurang lebih sama seperti soal di modul 1 no. 1 dan 3

# Asumsikan sebuah bilangan dengan empat digit
# ABCD
# Untuk mendapatkan digit ribuan, kita menggunakan pembagian
# Operator bagi mana yang akan kita pakai?
# // atau /?
# Digit yang menempati sebuah posisi ribuan hingga satuan merupakan sebuah bilangan bulat

# Misalnya bilangan 143
# Jika kita menggunakan operator /, ratusan = 143 / 100
# Alih-alih mendapat 1, kita akan mendapatkan 1.43
# Karena kita hanya ingin bilangan bulatnya saja tanpa pecahan, kita menggunakan //
# sehingga ratusan = 143 // 100 = 1
# Sampai di situ sudah benar.

# Sekarang bagaimana jika kita ingin menghilangkan digit ratusannya?
# Manfaatkan sisa bagi
# 143 / 100 memiliki hasil 1 dan *sisa* 43
# Kata kuncinya di *sisa*.
# Gunakan operator modulo untuk mendapatkan sisa
# n = 143 % 100 = 43

# Yap, sekarang kita akan coba terapkan :3.

n = int(input("Masukkan sebuah bilangan: "))
ribuan = n // 1000
n = n % 1000

ratusan = n // 100
n = n % 100

puluhan = n // 10

# Alih-alih
# n = n % 10
# satuan = n

# Kita langsung saja dapatkan digit satuan dari sisa bagi
satuan = n % 10

total = ribuan + ratusan + puluhan + satuan

# Jika masing-masing sisa bagi dengan digit adalah nol, bilangan tersebut Bravo

if ((total % ribuan == 0) and (total % ratusan == 0) and (total % puluhan == 0) and (total % satuan == 0)):
    print("Bilangan tersebut adalah bilangan Bravo.")
else:
    print("Bilangan tersebut adalah bilangan biasa.")