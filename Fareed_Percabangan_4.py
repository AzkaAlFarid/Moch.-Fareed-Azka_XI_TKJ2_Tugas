# Nama      : Moch. Fareed Azka Al-Farid
# kelas     : XI TKJ 2
# No. Absen : 16
# Soal      : Menghitung diskon berdasarkan total belanjaan dan jenis anggota

total_belanja = float(input("Masukan total belanjaan anda : "))
status_keanggotaan = input("Masukan Statu keanggotaan anda : ")

if status_keanggotaan == "premium":
    if total_belanja > 500000:
        diskon = total_belanja * 0.15
    else:
        diskon = total_belanja * 0.10
elif status_keanggotaan == "biasa":
    if total_belanja > 300000:
        diskon = total_belanja * 0.07
    else:
        diskon = total_belanja * 0

total_belanja_setela_diskon = total_belanja - diskon
print("total belanja anda : ", total_belanja_setela_diskon)