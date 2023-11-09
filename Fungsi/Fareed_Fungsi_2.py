# Nama      : Moch. Fareed Azka Al-Farid
# kelas     : XI TKJ 2
# No. Absen : 16
# Soal      : fungsi untuk menghitung faktiriol dari suatu bilangan

def fac(x):
    if x  == 0:
        return 1
    else:
        return x * fac(x - 1)
    
x = 5
hasil = fac(x)
print(f"faktorial dari {x} adalah {hasil}")