# Nama      : Moch. Fareed Azka Al-Farid
# kelas     : XI TKJ 2
# No. Absen : 16
# Soal      : menghitung total deretan ganjil dari hingga batas yang di tentukan pengguna

def total_deratan(batas):
    total = 0
    for i in range(1, batas + 1):
        bil_ganjil = 2 * i -1
        total += bil_ganjil
    return total

batas = 10
hasil = total_deratan(batas)
print(f"total deret bilangan ganjil hingga batas {batas} adalah {hasil}")