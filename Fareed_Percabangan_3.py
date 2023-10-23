# Nama      : Moch. Fareed Azka Al-Farid
# kelas     : XI TKJ 2
# No. Absen : 16
# Soal      : Membuat program Python yang memeriksa apakah suatu file sudah ada di direktori server.
#             Jika file sudah ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada."

nama_file = "data.txt" #input("Masukan nama file beserta formatnya : ")
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File sudah ada!")
else:
    print("File belum ada!")