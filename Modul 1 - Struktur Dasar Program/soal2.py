# PROGRAM CERMIN KURSI
# Cermin Kursi posisi dua dimensi
# KAMUS
# n, m, k, cermin : int
# ALGORITMA

# Masukkan nilai n, m, dan k
n = int(input("Jumlah baris kursi (n): "))
m = int(input("Jumlah kolom kursi (m): "))
k = int(input("Nomor kursi yang dipilih (k): "))

# Abaikan petunjuk karena kalian akan tersesat
# jika mengikutinya

# Solusinya cukup mudah
# Asumsikan model kursi satu dimensi
# 1 2 3 4 5 6 7 9 10
# Jika kita memilih kursi ke-4 dari *kiri*,
# kursi cerminannya (dari kanan) adalah
# kursi ke-6.

# Darimana kita bisa mengetahuinya?
# Tinggal kita hitung mundur alias kurangkan
# saja dari kanan.
# terdepan - jarak + 1

# Dibalik dari 0 + jarak (kiri)
# ke kursi paling kanan - jarak + 1 (kanan)

# Berlaku juga hal untuk susunan dua dimensi.
# Jarak dari depan dan kiri jika dibalik menjadi
# jarak dari belakang dan kanan.
# Gunakan m * n untuk mendapatkan kursi paling kiri
# dan belakang.

cermin = (m * n) - k + 1
print(f"Nomor kursi mirror: {cermin}")