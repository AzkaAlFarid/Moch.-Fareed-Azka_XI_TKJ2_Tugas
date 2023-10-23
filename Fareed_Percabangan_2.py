# Nama      : Moch. Fareed Azka Al-Farid
# kelas     : XI TKJ 2
# No. Absen : 16
# Soal      : Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai.
#             Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu,"
#             jika tidak, program harus mencetak "Terlambat."

from datetime import datetime

estimasi_selsai = input("Masukan estimasi waktu selesai (YYYY-MM-DD) : ")
tanggal_target = input("Masukan tanggal target selasi (YYYY-MM-DD): ")

tanggal_estimasi_selesai = datetime.strptime(estimasi_selsai, '%Y-%m-%d')
tanggal_target_selesai = datetime.strptime(tanggal_target, '%Y-%m-%d')

if tanggal_estimasi_selesai <= tanggal_target_selesai:
    print("Tepat Waktu")
else:
    print("Terlambat!!")