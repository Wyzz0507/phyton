while True:
    print("Selamat datang di kalkulator sederhana")
    print("Silahkan pilih operasi = ")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")
    ans = input("Tuliskan angka dari level yang ingin dipilih = ")

    if ans in ('1', '2', '3', '4'):
        num1 = (input("Tuliskan angka pertama : "))
        num2 = (input("Tuliskan angka kedua : "))
    else :
        print("Tidak valid.")

    if ans == ('1'):
            print("Hasil : ", num1, "+", num2, "=", (num1+num2))
    elif ans == ('2'):
            print("Hasil : ", num1, "-", num2, "=", (num1-num2))
    elif ans == ('3'):
            print("Hasil : ", num1, "*", num2, "=", (num1*num2))
    elif ans == ('4'):
            print("Hasil : ", num1, "/", num2, "=", (num1/num2))

    opsi = input("Apakah ingin melanjutkan? Ya/Tidak? = ")

    if opsi == ('Tidak'):
           print('Terimakasih')
           break
    