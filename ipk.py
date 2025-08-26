class Mahasiswa:

    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan
        self.nilai = []

    def tambah_nilai(self, nilai):
        return self.nilai.append(nilai)
    
    def rata_rata1(self):
        if len(self.nilai) == 0:
            return 0
        return sum(self.nilai) / len(self.nilai)
    
    def info(self):
        rata_rata = self.rata_rata1()
        print(f"Nama : {self.nama}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Nilai : {self.nilai}")
        print(f"Rata-rata : {rata_rata}")
           

print("Input data terlebih dahulu")
nama = input("Nama : ")
jurusan = input("Jurusan : ")
mahasiswa = Mahasiswa(nama, jurusan)
print(f'\nData mahasiswa {nama} sudah terinput')

while True:
    print("Silahkan pilih : ")
    print("1. Input nilai")
    print("2. Cek info")
    print("3. Keluar")

    ans1 = input("Masukkan pilihan : ")

    if ans1 == '1':
            while True:
                try:
                    nilai = input("nilai : ")
                    mahasiswa.tambah_nilai(nilai)
                    ans2 = input("Apakah ada lagi? : ")
                    if ans2 == 'ya':
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid")
    elif ans1 =='2':
        mahasiswa.info()
        continue
    else:
        break