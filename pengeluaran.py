import os

def input_pengeluaran(tanggal, jumlah, keterangan, bulan, tahun):

    bulan = input("\nBulan : ")
    tanggal = input("Tanggal (Dalam bentuk angka!) : ")
    tahun = input("Tahun : ")
    jumlah = input("Jumlah (Rp) : ")
    keterangan = input("Keterangan : ")

    with open(f"pengeluaran{bulan}.txt" , "a") as file:
        file.write(f"\nTanggal : {tanggal} , Bulan : {bulan} , Tahun : {tahun} , Harga (Rp) : {jumlah} , Keterangan : {keterangan}\n")

keluar = 1

jan1 = 1
jan2 = 1

feb1 = 1
feb2 = 1

mar1 = 1
mar2 = 1

apr1 = 1
apr2 = 1

mei1 = 1
mei2 = 1

jun1 = 1
jun2 = 1

jul1 = 1
jul2 = 1

agu1 = 1
agu2 = 1

sep1 = 1
sep2 = 1

okt1 = 1
okt2 = 1

nov1 = 1
nov2 = 1

des1 = 1
des2 = 1


while keluar > 0:
    
        print("\n===================")
        print("Catatan pengeluaran")
        print("===================\n")

        print("Silahkan pilih bulan mana yang ingin anda cek dan input : ")
        print("1. Januari")
        print("2. Februari")
        print("3. Maret")
        print("4. April")
        print("5. Mei")
        print("6. Juni")
        print("7. Juli")
        print("8. Agustus")
        print("9. September")
        print("10. Oktober")
        print("11. November")
        print("12. Desember")
        print("13. Keluar")

        ans7 = input("\nMasukkan opsi anda ( 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 ) : ")
        
        if ans7 == '1':
            while jan1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1j = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    
                    if ans1j == '1':
                        if os.path.exists("pengeluaran1.txt"):
                            with open("pengeluaran1.txt") as f:
                                print(f.read())

                                ans3j = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3j == 'ya':
                                    jan1 = 1
                                if ans3j == 'tidak':
                                    jan1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1j == '2':
                            while jan2 > 0:
                                if os.path.exists("pengeluaran1.txt"):
                                    with open("pengeluaran1.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while jan2 > 0:
                                            ans2j = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2j == 'ya':
                                                with open("pengeluaran1.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2j == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                jan2 = 0

                    elif ans1j == '3':
                            break

        elif ans7 == '2':
            while feb1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1f = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1f == '1':
                        if os.path.exists("pengeluaran2.txt"):
                            with open("pengeluaran2.txt") as f:
                                print(f.read())

                                ans3f = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3f == 'ya':
                                    feb1 = 1
                                if ans3j == 'tidak':
                                    feb1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1f == '2':
                            while feb2 > 0:
                                if os.path.exists("pengeluaran2.txt"):
                                    with open("pengeluaran2.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while feb2 > 0:
                                            ans2f = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2f == 'ya':
                                                with open("pengeluaran2.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2f == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                jan2 = 0

                    elif ans1f == '3':
                            break
                                                   
        elif ans7 == '3':
            while mar1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1mar = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1mar == '1':
                        if os.path.exists("pengeluaran3.txt"):
                            with open("pengeluaran3.txt") as f:
                                print(f.read())

                                ans3mar = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3mar == 'ya':
                                    mar1 = 1
                                if ans3mar == 'tidak':
                                    mar1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1mar == '2':
                            while mar2 > 0:
                                if os.path.exists("pengeluaran3.txt"):
                                    with open("pengeluaran3.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while mar2 > 0:
                                            ans2mar = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2mar== 'ya':
                                                with open("pengeluaran3.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2mar == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                mar2 = 0

                    elif ans1mar == '3':
                            break
                    
        elif ans7 == '4':
            while apr1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1apr = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1apr == '1':
                        if os.path.exists("pengeluaran4.txt"):
                            with open("pengeluaran4.txt") as f:
                                print(f.read())

                                ans3apr = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3apr == 'ya':
                                    apr1 = 1
                                if ans3apr == 'tidak':
                                    apr1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1apr == '2':
                            while apr2 > 0:
                                if os.path.exists("pengeluaran4.txt"):
                                    with open("pengeluaran4.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while apr2 > 0:
                                            ans2apr = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2apr == 'ya':
                                                with open("pengeluaran4.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2apr == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                apr2 = 0

                    elif ans1apr == '3':
                            break
                    
        elif ans7 == '5':
            while mei1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1mei = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1mei == '1':
                        if os.path.exists("pengeluaran5.txt"):
                            with open("pengeluaran5.txt") as f:
                                print(f.read())

                                ans3mei = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3mei == 'ya':
                                    mei1 = 1
                                if ans3mei == 'tidak':
                                    mei1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1mei == '2':
                            while mei2 > 0:
                                if os.path.exists("pengeluaran5.txt"):
                                    with open("pengeluaran5.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while mei2 > 0:
                                            ans2mei = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2mei == 'ya':
                                                with open("pengeluaran5.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2mei == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                mei2 = 0

                    elif ans1mei == '3':
                            break
                    
        elif ans7 == '6':
            while jun1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1jun = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1jun == '1':
                        if os.path.exists("pengeluaran6.txt"):
                            with open("pengeluaran6.txt") as f:
                                print(f.read())

                                ans3jun = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3jun== 'ya':
                                    jun1 = 1
                                if ans3jun == 'tidak':
                                    jun1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1jun == '2':
                            while jun2 > 0:
                                if os.path.exists("pengeluaran6.txt"):
                                    with open("pengeluaran6.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while jun2 > 0:
                                            ans2jun = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2jun == 'ya':
                                                with open("pengeluaran6.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2jun == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                jun2 = 0

                    elif ans1jun == '3':
                            break
                    
        elif ans7 == '7':
            while jul1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1jul = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1jul == '1':
                        if os.path.exists("pengeluaran7.txt"):
                            with open("pengeluaran7.txt") as f:
                                print(f.read())

                                ans3jul = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3jul == 'ya':
                                    jul1 = 1
                                if ans3jul == 'tidak':
                                    jul1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1jul == '2':
                            while jul2 > 0:
                                if os.path.exists("pengeluaran7.txt"):
                                    with open("pengeluaran7.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while jul2 > 0:
                                            ans2jul = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2jul == 'ya':
                                                with open("pengeluaran7.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2jul == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                jul2 = 0

                    elif ans1jul == '3':
                            break
                    
        elif ans7 == '8':
            while agu1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1agu = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1agu == '1':
                        if os.path.exists("pengeluaran8.txt"):
                            with open("pengeluaran8.txt") as f:
                                print(f.read())

                                ans3agu = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3agu == 'ya':
                                    agu1 = 1
                                if ans3agu == 'tidak':
                                    agu1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1agu == '2':
                            while agu2 > 0:
                                if os.path.exists("pengeluaran8.txt"):
                                    with open("pengeluaran8.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while agu2 > 0:
                                            ans2agu = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2agu == 'ya':
                                                with open("pengeluaran8.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2agu == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                agu2 = 0

                    elif ans1agu == '3':
                            break
                    
        elif ans7 == '9':
            while sep1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1sep = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1sep == '1':
                        if os.path.exists("pengeluaran9.txt"):
                            with open("pengeluaran9.txt") as f:
                                print(f.read())

                                ans3sep = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3sep == 'ya':
                                    sep1 = 1
                                if ans3sep == 'tidak':
                                    sep1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1sep == '2':
                            while sep2 > 0:
                                if os.path.exists("pengeluaran9.txt"):
                                    with open("pengeluaran9.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while sep2 > 0:
                                            ans2sep = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2sep == 'ya':
                                                with open("pengeluaran9.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2sep == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                sep2 = 0

                    elif ans1sep == '3':
                            break
                    
        elif ans7 == '10':
            while okt1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1okt = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1okt == '1':
                        if os.path.exists("pengeluaran10.txt"):
                            with open("pengeluaran10.txt") as f:
                                print(f.read())

                                ans3okt = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3okt == 'ya':
                                    okt1 = 1
                                if ans3okt == 'tidak':
                                    okt1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1okt == '2':
                            while okt2 > 0:
                                if os.path.exists("pengeluaran10.txt"):
                                    with open("pengeluaran10.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while okt2 > 0:
                                            ans2okt = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2okt == 'ya':
                                                with open("pengeluaran10.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2okt == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                okt2 = 0

                    elif ans1okt == '3':
                            break
                    
        elif ans7 == '11':
            while nov1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1nov = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1nov == '1':
                        if os.path.exists("pengeluaran11.txt"):
                            with open("pengeluaran11.txt") as f:
                                print(f.read())

                                ans3nov = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3nov == 'ya':
                                    nov1 = 1
                                if ans3nov == 'tidak':
                                    nov1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1nov == '2':
                            while nov2 > 0:
                                if os.path.exists("pengeluaran11.txt"):
                                    with open("pengeluaran11.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while nov2 > 0:
                                            ans2nov = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2nov == 'ya':
                                                with open("pengeluaran11.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2nov == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                nov2 = 0

                    elif ans1nov == '3':
                            break
                    
        elif ans7 == '12':
            while des1 > 0:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Silahkan pilih opsi dibawah ini : ")
                    print("1. Cek pengeluaran anda")
                    print("2. Input pengeluaran anda")
                    print("3. Keluar")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    ans1des = input("Masukkan opsi ( 1 / 2 / 3 ) : ")

                    if ans1des == '1':
                        if os.path.exists("pengeluaran12.txt"):
                            with open("pengeluaran12.txt") as f:
                                print(f.read())

                                ans3des = input("Apakah anda ingin kembali ke menu ( Ya ) : ").lower()
                                if ans3des == 'ya':
                                    des1 = 1
                                if ans3des == 'tidak':
                                    des1 = 0
                        else:
                            print("\nMaaf, anda harus memasukkan data terlebih dahulu!")
                            continue

                    elif ans1des == '2':
                            while des2 > 0:
                                if os.path.exists("pengeluaran12.txt"):
                                    with open("pengeluaran12.txt", "w") as f:
                                        input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun') 
                                        
                                else: 
                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun' )

                                    while des2 > 0:
                                            ans2des = input("\nApakah ingin melanjutkan menambah data? ( Ya / Tidak ) : ").lower()

                                            if ans2des == 'ya':
                                                with open("pengeluaran12.txt", "a") as f:
                                                    input_pengeluaran(f'jumlah', 'keterangan', 'tanggal', 'bulan', 'tahun')
                                            elif ans2des == 'tidak':
                                                print("\nPengeluaran anda telah diinput ke dalam database dan anda akan dibawa ke menu utama")
                                                des2 = 0

                    elif ans1des == '3':
                            break

        elif ans7 == '13':
            print("\nTerimakasih\n")
            keluar = 0