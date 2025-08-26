while True:
    print("===============================")
    print("Konversi satuan mata uang asing")
    print("===============================")

    print("Terdapat 2 konversi mata uang asing : ")
    print("1. Mata uang asing ke IDR")
    print("2. IDR ke Mata uang asing")
    print("3. Keluar")
    ans1 = input("Masukkan pilihan anda ( 1 / 2 / 3 ) :  ")

    if ans1 == '1':
        print("Terdapat beberapa macam mata uang asing : ")
        print("1. US")
        print("2. Yen")
        print("3. Baht")
        print("4. Ringgit")
        print("5. Keluar")
        ans2 = input("Masukkan pilihan yang anda inginkan ( US / Yen / Baht / Ringgit / Keluar ):  ")
        ans3 = ans2.lower()
        
        if ans3 == 'us':
            num1 = float(input("Masukkan nominal anda dalam bentuk ($) : "))
            num2 = float(16186.83)
            print(f"Nilai (Rp) : ", num1, '*', num2, '=', (num1 * num2))
        elif ans3 == 'yen':
            num1 = float(input("Masukkan nominal anda dalam bentuk (¥) : "))
            num2 = float(110)
            print(f"Nilai (Rp) : ", num1, '*', num2, '=', (num1 * num2))
        elif ans3 == 'baht':
            num1 = float(input("Masukkan nominal anda dalam bentuk (฿) : "))
            num2 = float(499.12)
            print(f"Nilai (Rp) : ", num1, '*', num2, '=', (num1 * num2))
        elif ans3 == 'ringgit':
            num1 = float(input("Masukkan nominal anda dalam bentuk (MYR) : "))
            num2 = float(3845,95)
            print(f"Nilai (Rp) : ", num1, '*', num2, '=', (num1 * num2))
        elif ans3 == 'keluar' or '5' or '5.':
            print
        else :
            print("Tidak Valid")

    elif ans1 == '2':
        print("Terdapat beberapa macam mata uang asing : ")
        print("1. US")
        print("2. Yen")
        print("3. Baht")
        print("4. Ringgit")
        print("5. Keluar")
        ans2 = input("Masukkan pilihan mata uang yang anda inginkan :  ")
        ans3 = ans2.lower()
        
        if ans3 == 'us':
            num1 = float(input("Masukkan nominal anda dalam bentuk (Rp) : "))
            num2 = float(16186.83)
            print(f"Nilai ($): ", num1, '/', num2, '=', (num1 / num2))
        elif ans3 == 'yen':
            num1 = float(input("Masukkan nominal anda dalam bentuk (Rp) : "))
            num2 = float(110)
            print(f"Nilai (¥): ", num1, '/', num2, '=', (num1 / num2))
        elif ans3 == 'baht':
            num1 = float(input("Masukkan nominal anda dalam bentuk (Rp) : "))
            num2 = float(499.12)
            print(f"Nilai (฿): ", num1, '/', num2, '=', (num1 / num2))
        elif ans3 == 'ringgit':
            num1 = float(input("Masukkan nominal anda dalam bentuk (Rp) : "))
            num2 = float(3845.95)
            print(f"Nilai (MYR): ", num1, '/', num2, '=', (num1 / num2))
        elif ans3 == 'keluar' or '5' or '5.':
            print
        else :
            print("Tidak Valid")

    elif ans1 == '3':
        print("Terima kasih!")
        break 

    else :
        print("Tidak Valid.")