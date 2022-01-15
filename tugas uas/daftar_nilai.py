nama = []

def daftar_nilai () :
    while True :
        print ("kakak mau ngapain ? Lihat data (L) Tambah data (T) Delete data (D)")
        pilihan = input ("masukan pilihan :")
        if pilihan == "T" :
            nama1 = input ("masukan nama kamu : ")
            nama.append (nama1)
            print ("data di tambahkan")
        elif pilihan == "L":
            print (nama)
            break
        elif pilihan == "D" :
            hapus = input ("Siapa yang ingin di hapus ?")
            del nama[hapus]
      
