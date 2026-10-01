# PROGRAM Reverse
# Mencetak ulang angka yang sudah dimasukkan

# KAMUS
# n, i : int
# arr : array [0..n - 1]

# ALGORITMA

n = int(input("Masukkan n: "))

# Buat array dengan kapasitas n
arr = [0 for i in range(n)]

# Isi array hingga n kali
for i in range(n):
    arr[i] = int(input())

# Alih-alih iterasi array dari awal, iterasi dari akhir ke belakang
# Ulangi dari n - 1 (indeks ujung array)
# sampai 0 (di atas -1)
# -1 karena indeksnya mundur sehingga berkurang
# Tidak bertambah seperti isi array di atas

# Alih-alih
# 0 1 2 3 ... n - 1
# Jadi
# n - 1, ..., 3, 2, 1
# Semakin berkurang bukan?
# Tiap perulangan nilai i + (-1) agar berkurang
# Berbeda dengan perulangan pertama yang nilainya 
# ditambah 1 tiap kembali ke atas

for i in range(n - 1, -1, -1):
    print(f"{arr[i]}", end=' ')
print("")