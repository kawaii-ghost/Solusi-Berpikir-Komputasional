# PROGRAM Kelipatan 10 terkecil
# Mencari kelipatan 10^x > n dengan 10^x terdekat ke n

# KAMUS
# n, near : int

# ALGORITMA

n = int(input("Masukkan nilai n: "))

# Sebenarnya ada cara konstan tanpa harus menggunakan perulangan untuk menyelesaikan masalah ini.
# near = ((n // 10) + 1) * 10

# Asumsikan disuruh pakai perulangan, kita pakai while karena kita tidak menggunakan rentang nilai sampai x sekian

near = 10
while (n > near):
    near = near * 10

print(near)