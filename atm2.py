class ATM:
    def __init__(self, pin, nama):
        self.nama = nama
        self.pin = pin
        self.saldo = 0

    def setor_tunai(self, nominal):
        self.saldo += nominal
        return print(f"Nominal anda sebesar Rp {nominal} sudah masuk ke rekening anda")
    
    def tarik_tunai(self, nominal):
        if self.saldo < nominal:
            print("Maaf, saldo anda tidak cukup")
        else:
            self.saldo -= nominal
            return print(f"Tarik tunai sebesar Rp {nominal} sudah berhasil")
            
    def info (self):
        print(f"\nNama : {self.nama}")
        print(f"Saldo : {self.saldo}")
        
atm = ATM('050507', 'William')

while True:
    pin = input("Input pin anda : ")
    if pin == '050507':
        while True:
            print(f"\nSelamat datang {atm.nama}")
            print("Silahkan pilih opsi")
            print("1. Cek info")
            print("2. Tarik tunai")
            print("3. Setor tunai")
            print("4. Keluar")

            ans1 = input("\nPilihan anda : ")
            if ans1 =='1':
                atm.info()
                continue
            elif ans1 == '2':
                nominal = (input("Masukkan nominal (Rp) : "))
                atm.tarik_tunai(nominal)
                
            elif ans1 == '3':
                nominal = (input("Masukkan nominal (Rp) : "))
                atm.setor_tunai(nominal)
                
            elif ans1 == '4':
                break
    else:
        print("Pin anda salah. Silahkan dicoba lagi!")
        continue