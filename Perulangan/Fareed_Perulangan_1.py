#Nama           : Moch. Fareed Azka Al-Farid
#Kelas          : XI TKJ 2
#Nomor Absen    : 16
#Soal           : membutuhkan waktu berapa bulan agar pertumbuh ayam dari jumlah awal 100 menjadi 200 ayam dengan pertumbuhan 5%/bulan

jumlah_ayam_awal = 100
target_ayam_akhir = 200
bulan = 0

while jumlah_ayam_awal <= target_ayam_akhir:
    bulan += 1
    pertambahan_ayam = jumlah_ayam_awal * 0.05
    jumlah_ayam_awal += pertambahan_ayam
    print(f'pertumbuhan ayam {jumlah_ayam_awal} pada bulan ke {bulan}')

print(f'Dibutuhkan {bulan} bulan agar jumlah ayam melebihi {target_ayam_akhir} ekor.')