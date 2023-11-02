#Nama           : Moch. Fareed Azka Al-Farid
#Kelas          : XI TKJ 2
#Nomor Absen    : 16
#Soal           : Buatlah progam yang menghitung berapa tahun yang dibutuhkan agar investasi melebihi 20.000 dollar

investasi_awal = 10000
target_investasi = 20000
tahun = 0

while investasi_awal < target_investasi:
    investasi_awal = investasi_awal + 0.06 * investasi_awal
    tahun += 1
    print(f'Nilai investasi {investasi_awal} pada tahun ke {tahun}')

print(f'Dibutuhkan {tahun} tahun agar nilai investasi mencapai 20.000 dollar')