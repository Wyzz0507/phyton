class Kurs:

    rate = {
        "us": 16186.83,
        "yen": 110,
        "baht": 499.12,
        "ringgit": 3845.95
    }

    def __init__(self, nominal, mata_uang):
        self.nominal = nominal
        self.mata_uang = mata_uang.lower()
        
    def kurs1(self):
        if self.mata_uang in Kurs.rate:
            return (f"{self.nominal * Kurs.rate[self.mata_uang]}")
        
    def kurs2(self):
        if self.mata_uang in Kurs.rate:
            return (f"{self.nominal / Kurs.rate[self.mata_uang]}")

k = Kurs('nominal' , 'mata_uang')

while True:
    print("========================")
    print("Konversi mata uang asing")
    print("========================")
    print("Terdapat 2 konversi mata uang asing : ")
    print("Hanya terdapat ( US , Yen , Baht , Ringgit )")
    print("1. Mata uang asing ke IDR")
    print("2. IDR ke Mata uang asing")
    print("3. Keluar\n")
    ans1 = input("Masukkan pilihan anda ( 1 / 2 / 3 ) :  ")
    if ans1 == '1':
        mata_uang = input("\nMata uang (us/yen/baht/ringgit) : ").lower()
        try:
            nominal = float(input("Nominal : "))
            k = Kurs(nominal, mata_uang)
            hasil = k.kurs1('nominal','mata_uang') 
            print(f"Hasil : {hasil}")
        except ValueError:
            print("Input anda salah!")
            continue
    elif ans1 == '2':
        mata_uang = input("\nMata uang (us/yen/baht/ringgit) : ").lower()
        try:
            nominal = int(input("Nominal (Rp) : "))
            k = Kurs(nominal, mata_uang)
            hasil = k.kurs2(mata_uang, nominal)
            print(f"Hasil : {hasil}")
        except ValueError:
            print("Input anda salah!")
            continue
    elif ans1 == '3':
        break
    else:
        print("\nInvalid, silahkan input dengan benar!\n")
        continue