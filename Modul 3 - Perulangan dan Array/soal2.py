# PROGRAM Segitiga Angka
# Membuat pola segitiga angka

# KAMUS
# i, j, n

# ALGORITMA

n = int(input("Masukkan nilai n: "))

# Kita butuh dua perulangan
# Perulangan untuk mencetak angka (horizontal)
# Perulangan untuk mencetak baris baru (vertikal)

for i in range(n):
    # Nilai i dimulai dari 0 hingga n - 1
    # Bertambah setiap mengulang
    # Berulang sebanyak n kali

    for j in range(1, i + 2):
        # Setiap berulang nilai i semakin bertambah
        # Kita mencetak angka hingga nilai i.
        print(f"{j}", end=" ")
    print("")