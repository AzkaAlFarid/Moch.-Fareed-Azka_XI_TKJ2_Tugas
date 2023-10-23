# Nama      : Moch. Fareed Azka Al-Farid
# kelas     : XI TKJ 2
# No. Absen : 16
# Soal      : Buat progam yang mengambil status persiapan proyek  dana menentukan proyek siap diluncurkan atau tidak

status = input("Masukan status proyek (siap/tunda) : ")

if status == "siap":
    print("Proyek diluncurkan")
elif status == "tunda":
    print("Proyek ditunda")
else:
    print("Input tdak valid!")