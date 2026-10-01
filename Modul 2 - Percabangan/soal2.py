# PROGRAM Ujian
# Menentukan apakah Tuan Riz berhasil menyelesaikan
# semua soal tepat pada waktunya

# KAMUS
# isian, esai, waktu : int
# sisa_isian, sisa_esai : int

# ALGORITMA

isian = int(input("Masukkan banyak soal isian singkat yang sudah diselesaikan : "))
esai = int(input("Masukkan banyak soal esai yang sudah diselesaikan : "))

# Hitung masing-masing sisa soal yang belum dikerjakan
sisa_isian = 14 - isian
sisa_esai = 2 - esai

# Hitung waktu yang dibutuhkan untuk mengerjakan soal yang tersisa
# Tiap soal isian singkat memakan waktu 10 menit
# Tiap soal esai memakan waktu 20 menit
waktu = (sisa_isian * 10) + (sisa_esai * 20)

# Bandingkan sisa waktu 1 jam (60 menit) ke waktu yang diperlukan
# Jika waktu yang dibutuhkan lebih besar dibandingkan sisa waktu
# , sisa waktu tidak cukup

if (waktu > 60):
    print("Tuan Riz tidak akan berhasil mengerjakan semua soal")
else:
    print("Tuan Riz akan berhasil mengerjakan semua soal")