# PROGRAM DENDA TERLAMBAT
# Menghitung denda dari keterlambatan.

# KAMUS
# t, b : int

# ALGORITMA

# Kurang lebih konsepnya sama seperti soal1
b = 0
t = int(input("Waktu keterlambatan (menit): "))

b = b + ((t // (24 * 60)) * 800000)
t = t % (24 * 60)

b = b + ((t // 60) * 25000)
t = t % 60

b = b + ((t // 5) * 1000)

# Karena tidak sampai habis menit untuk denda, tidak
# perlu sampai ujung mengurangi t-nya.

print(f"Total denda yang harus dibayar: Rp{b},00")
