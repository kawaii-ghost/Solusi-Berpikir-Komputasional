# PROGRAM Kembalian
# Menyusun kembalian menggunakan pecahan 50.000, 
#   20.000, 10.000, 5.000, dan 1.000

# KAMUS
# p, b, k, lima_puluh, dua_puluh, sepuluh, lima, satu : int

# ALGORITMA

# Pertama, kita masukkan masing-masing jumlah pembayaran
# dan harga barangnya.

p = int(input("Masukkan jumlah pembayaran (rupiah): "))
b = int(input("Masukkan harga barang rupiah (rupiah): "))

# Kemudian, kita dapatkan kembaliannya dengan cara p - b dan
# disimpan di variabel k.

k = p - b

# Langkah ketiga, tinggal kita bagi masing-masing ke pecahan mata uang
# dimulai dari yang terbesar.
# Kita menggunakan operator // karena kita tidak mungkin membagi (memotong) uang
# kertas karena berupa pecahan, bukan?
# Yang tidak habis dibagi menjadi sisa, bukan pecahan.
# Jumlah uang kertas berupa bilangan bulat, bukan pecahan.

lima_puluh = k // 50000

# Kembalian kita kurangi dengan jumlah 50000 yang kita dapatkan
# k = k - (limpul * 50000)
# Akan tetapi, cara yang sama bisa dilakukan dengan menggunakan modulo
k = k % 50000

# Berlaku ke pecahan mata uang lainnya

dua_puluh = k // 20000
k = k % 20000

sepuluh = k // 10000
k = k % 10000

lima = k // 5000
k = k % 5000

satu = k // 1000

# Terakhir, kita cetak masing-masing nilainya
print(f"Nona sal perlu memberikan {lima_puluh} lembar uang Rp50.000,00")
print(f", {dua_puluh} lembar uang Rp20.000,00")
print(f", {sepuluh} lembar uang Rp10.000,00")
print(f", {lima} lembar uang Rp5.000,00")
print(f", dan {satu} lembar uang Rp1.000,00")
