#Nama           : Moch. Fareed Azka Al-Farid
#Kelas          : XI TKJ 2
#Nomor Absen    : 16
#Soal           : Buatlah program yang menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.

waktu_rentang = 120
waktu_pembelahan= 20
jumlah_pembelahan = 0

while waktu_pembelahan <= waktu_rentang:
    waktu_rentang -= waktu_pembelahan
    jumlah_pembelahan += 1
    print(f'Bakteri melakukan penjumlahan sebanyak {jumlah_pembelahan} pada sisa {waktu_rentang} menit')
print(f'Dalam rentang waktu 2 jam, bakteri akan mengalami pembelahan sebanyak {jumlah_pembelahan} kali.')