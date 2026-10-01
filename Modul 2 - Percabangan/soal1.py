# PROGRAM Ganjil-Genap
# Menentukan apakah sebuah bilangan ganjil / genap
# dan positif atau negatif

# KAMUS
# n : int

# ALGORITMA
n = int(input("Masukkan nilai n: "))

# Ada tiga kondisi untuk masalah positif atau negatif
# n > 0 maka positif
# n < 0 maka negatif
# Jika tidak termasuk kedua kondisi di atas, n bernilai nol

if (n > 0):
    # Karena kita tidak ingin membuat baris baru (enter)
    #, setiap akhir print membuat spasi dengan end=' ' 
    print(f"{n} bilangan positif", end=' ')
    
    # Jika n mod 2 hasilnya nol atau terbagi habis
    # , n adalah bilangan genap
    if (n % 2 == 0):
        print("genap")
    # Jika tidak, n adalah bilangan ganjil
    else:
        print("ganjil")

elif (n < 0):
    print(f"{n} bilangan negatif")
else:
    print("0 bilangan nol")