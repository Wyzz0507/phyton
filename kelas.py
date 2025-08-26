class siswa:
    def __init__ (self):
        self.data = []

    def tambah_data(self, nama, absen, kelas):
        self.data.append({'nama' : nama, 'absen' : absen, 'kelas' : kelas})
    
    def info(self):
        print(self.data)

fakta = 1       
s = siswa()


while True:

    var1 = input("1/2? : ")
    if var1 == '1':
            asu = 1
            try:
                    nama = input("nama : ")
                    kelas = input("kelas : ")
                    absen = input("absen : ")

                    s.tambah_data(nama, kelas, absen)

                    while fakta > 0:
                        var2 = input("3/4? : ")
                        if var2 == '3':
                            nama = input("nama : ")
                            kelas = input("kelas : ")
                            absen = input("absen : ")
                            s.tambah_data(nama, absen, kelas)
                            
                        elif var2 == '4':
                            s.info()
                            fakta = 0

            except ValueError:
                print("eror")
                continue
        
    elif var1 == '2':
        break

    else:
        print("invalid")
        continue

    