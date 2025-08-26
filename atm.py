saldo = 10000000

while True:
    print("Selamat datang di ATM abc")

    digit = input("Silahkan masukkan 6 digit pin anda :\n")

    if digit == '050507':
        print("Silahkan pilih menu dibawah ini :")
        print("1. Cek saldo")
        print("2. Tarik tunai")
        print("3. Setor tunai")
        print("4. Kembali")

    else:
        print("Maaf pin yang ada masukkan salah / tidak valid, silahkan diulang kembali.")
        continue

    ans = input("Silahkan masukkan No. 1/2/3/4 : ")

    if ans == '1':
        print(f"Saldo sekarang adalah : Rp {saldo}")
    
        ans2 = input("Apakah melakukan transaksi lagi? ( Ya / Tidak ) :\n")
        ans3 = ans2.lower()

        if ans3 == 'ya':
            continue
        else: 
            break

    elif ans == '2':
        nominal = (input("Masukkan nominal anda :\n Rp "))
        
        if nominal <= saldo:
            print("Saldo sekarang tersisa : ")
            saldo -= nominal
            print(saldo)

        elif nominal >= saldo:
            print("Maaf anda miskin!")

        ans2 = input("Apakah melakukan transaksi lagi? ( Ya / Tidak ) :\n")
        ans3 = ans2.lower()

        if ans3 == 'ya':
            continue
        else: 
            break
    
    elif ans == '3':
        nominal = input("Masukkan setoran anda :\n Rp ")
        nominal = (nominal)
        
        print("Saldo anda sekarang : ")
        saldo += nominal
        print(saldo)

        ans2 = input("Apakah melakukan transaksi lagi? ( Ya / Tidak ) :\n")
        ans3 = ans2.lower()

        if ans3 == 'ya':
            continue
        elif ans3 == 'tidak':
            break
        else: 
            print("Tidak Valid.")
            break

    elif ans == '4':
        break