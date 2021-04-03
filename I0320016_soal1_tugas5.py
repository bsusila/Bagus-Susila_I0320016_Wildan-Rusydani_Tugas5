# Input nama dan jenis kelamin
nama = input("Nama :")
jenis_kelamin = input("Jenis Kelamin (Pria/Wanita) :")
# Percabangan dan output
if jenis_kelamin == "Pria" :
    print("Selamat datang, Tuan",nama,"!")
elif jenis_kelamin == "Wanita" :
    print("Selamat datang, Nyonya",nama,"!")
else :
    print("Masukkan data dengan benar!")
