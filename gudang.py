import os

class Gudang:
    def __init__(self):
        with open ("gudang1.txt", "a") as file:
            pass
        self.nama_barang = []
        self.stok = []
    
    def cek_filetxt (self):
        if os.path.getsize("gudang1.txt") == 0:
            return print("The file is empty")
        else:
            return print("The file is not empty")           
    
    def cek_stok(self):
        if len(self.nama_barang) == 0:
            return print("-")
        else:
            var_count = 0
            self.nama_barang[var_count]
            for i,c in enumerate(self.nama_barang, start=1):
                    stok = self.stok[var_count]
                    print (f"{i}. The stuff : {c} | The quantity : {stok}")
                    var_count += 1

    def input_barang1(self, nama, stok):

        self.nama_barang.append(nama)
        self.stok.append(stok)
        with open ("gudang1.txt", "a") as file:
            file.write(f"Stuff : {nama}, Stock : {stok}\n")
        return nama, stok

    def hapus_barang(self, var3):
        self.nama_barang.pop(var3-1)
        self.stok.pop(var3-1)
        with open('gudang1.txt', 'r') as fr:
            lines = fr.readlines()
            ptr = 1
            with open('gudang1.txt', 'w') as fw:
                for line in lines:
                    if ptr != var3:
                        fw.write(line)
                    ptr += 1
        print(f"\nThe stuff has been removed from database warehouse")

    def cari_barang(self, var5):
        if var5 in self.nama_barang:
            index = self.nama_barang.index(var5)
            stok = self.stok[index]
            print(f"\nThe stuff {var5} is available and the stock : {stok}")
        else: 
            print(f"\nThe stuff is {var5} not available")
            
g = Gudang()
b = 1
a = 1

while b > 0:
    print("\nWelcome to Will Warehouse!")
    print("\nChoose the number")
    print("1. Check file")
    print("2. Check info")
    print("3. Input stock")
    print("4. Remove stock")
    print("5. Searching")
    print("6. Exit")

    var1 = input("\nInput the number (1/2/3/4/5) : ")
    if var1 == "1":
        g.cek_filetxt()
        
    elif var1 == "2":
        print("\nIn Will Warehouse, the stuff that available :")
        g.cek_stok()

    elif var1 == "3":
        while True :
            try:
                nama = str(input("\nInput name of the stuff :  "))
                stok = (input("Input the Quantity : "))
                g.input_barang1(nama, stok)

                print(f"\nThe stuff : {nama} & Quantity : {stok} has been added to the database warehouse")
                var2 = (input("\nDo you want to input the stuff again? ( Yes / No ) : ")).lower()
                if var2 == "yes":
                    continue
                elif var2 == "no":
                    print("\nYour data has been added to the Will Warehouse!")
                    break
                else:
                    print("Invalid")
                    continue
            except ValueError:
                print("Invalid")
                continue
            
    elif var1 == "4":
        g.cek_stok()
        var3 = (input("\nWrite the number stuff that you want to delete : "))
        g.hapus_barang(var3)

    elif var1 == "5":
        var5 = (input("\nInput the name of the stuff that you want to if the stuff was available or not : "))
        g.cari_barang(var5)
        
    elif var1 == "6":
        print("Thankyou!")
        b = 0

    else:
        print("\nInvalid answer, Try Again!")
        continue