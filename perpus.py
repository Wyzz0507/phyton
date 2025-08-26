import os

class Perpus:
    def __init__ (self):
        self.nama = []
        self.tanggal = []
        self.buku = []
        
    def cek_data (self):
        if os.path.exists("dataperpus1.txt"):
            with open ("dataperpus1.txt", "r") as file:
                pass
            print("Data masih ada!")
        else:
            with open ("dataperpus1.txt", "w") as file:
                pass
            print("Data tidak ditemukan dan otomatis dibuatkan folder baru!")

    def cek_pinjaman (self):
        if os.path.exists("dataperpus1.txt"):
            lines = open("dataperpus1.txt")
            print(lines.read())
        elif os.path.exists("dataperpus1.txt"):
            var_count = 0
            self.nama[var_count]
            for i,b in enumerate(self.nama, start=1):
                tanggal = self.tanggal[var_count]
                print (f"\n{i}. Nama : {b}, Tanggal {tanggal}, Buku yang dipinjam : {buku}")
                var_count += 1
        else:
            print("Data masih kosong")
            
    def peminjaman (self, nama, tanggal, buku):
        self.nama.append(nama)
        self.tanggal.append(tanggal)
        self.buku.append(buku)
        with open ("dataperpus1.txt", "a") as f:
            f.write(f"Nama : {nama}, Tanggal : {tanggal}, Buku : {buku}\n")

    def pengembalian (self):
        self.nama.pop(var3)
        self.tanggal.pop(var3)
        self.buku.pop(var3)

        with open ("dataperpus1.txt", "w") as fr:
            lines = fr.readlines()
            ptr = 1
            with open ("dataperpus1.txt", "w") as fw:     
                for line in lines:
                    if ptr != var3:
                        fw.lines(line)

p = Perpus()
a = 1

while a > 0:
    print("\nSelamat datang di perpustakaan!")
    print("Silahkan pilih opsi dibawah ini!\n")
    print("1. Cek data")
    print("2. Daftar pinjaman")
    print("3. Peminjaman buku")
    print("4. Pengembalian buku")
    print("5. Keluar")

    ans = input("\nInput opsi : ")

    if ans == "1":
        p.cek_data()
    elif ans == "2":
        p.cek_pinjaman()
    elif ans == "3":
        nama = str(input("\nMasukkan nama : "))
        tanggal = (input("Masukkan tanggal peminjaman (2025) : "))
        buku = str(input("Masukkan nama dari buku yang dipinjam : "))
        p.peminjaman(nama, tanggal, buku)
        print("\nData anda sudah keinput")
    elif ans == "4":
        var3 = str(input("\nMasukkan nama dari buku yang anda pinjam : "))
        p.pengembalian(var3)
        print("Terimakasih telah mengembalikan buku yang anda pinjam ke perpustakaan")
    elif ans == "5":
        print("Terimakasih!")
        a = 0