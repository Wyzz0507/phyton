### 9. Nilai Siswa
# Input nama siswa + nilai DONE
# Hitung rata-rata DONE
# Cari nilai tertinggi/terendah DONE
# Tentukan grade A/B/C/D DONE

nama_siswa = []
nilai_siswa = []

print("Silahkan memilih opsi yang tersedia : ")
print("1. Input data")
print("2. Keluar")

keluar = 1
while keluar > 0:
    ans1 = input("Masukkan pilihan anda ( 1 / 2 ) : ")

    while keluar > 0:
            
            if ans1 == '1':
                  
                while True:

                    try:
                        nama = str(input("Masukkan nama : ").lower().strip())

                        if nama and not nama.replace(" ", "").isdigit():
                            nama_siswa.append(nama)
                        break

                    except ValueError: 
                        print("Input tidak valid")
                    continue

                while True:
                    try:
                        nilai = (input("Masukkan nilainya : "))
                        nilai_siswa.append(nilai)
                        break

                    except ValueError:
                        print("Input tidak valid")
                        continue

                ans2 = input("Apakah masih ada lagi? ( Ya / Tidak ) : ").lower()

                if ans2 == 'ya':
                    continue
                    
                elif ans2 == 'tidak':
                    
                    while True:
                            print("Silahkan memilih opsi dibawah ini : ")
                            print("1. Cek data yang terinput")
                            print("2. Cek rata - rata")
                            print("3. Cek nilai tertinggi")
                            print("4. Cek nilai terendah")
                            print("5. Cek grade")

                            ans3 = input("Masukkan pilihan anda ( 1 / 2 / 3 / 4 / 5 ) : ")

                            if ans3 == '1':
                                for i,b in enumerate(nama_siswa):
                                        print(f"Nama siswa : {nama_siswa[i]} dan Nilai : {nilai_siswa[i]}")

                                ans4 = input ("Apakah ingin kembali? ( Ya / Tidak ) : ").lower()

                                if ans4 == 'ya':
                                    continue
                                
                                if ans4 == 'tidak':
                                    keluar = 0
                                    break

                                else:
                                    print("Maaf input anda tidak valid.")
                                    continue

                            elif ans3 == '2':
                                print("Banyaknya siswa yang ada sekarang adalah : ")
                                lenght = len(nama_siswa)
                                print(lenght)

                                print("Total nilai dari data siswa yang ada sekarang adalah : ")
                                total1 = sum(nilai_siswa)
                                print(total1)

                                print("Rata - ratanya adalah :")
                                print(float(total1 / lenght))

                            elif ans3 == '3':
                                var1 = -1
                                var2 = []
                                var4 = ""
                                for b in (nama_siswa):
                                    var2.append(b)
                                for i in (nilai_siswa):
                                    if i > var1:
                                        var1 = i
                                        var4 = var2[0]
                                        if len(var2) == 1:
                                            var4 = var2[0]
                                            break
                                        else:
                                            var2.pop(0)
                                    else:
                                        var2.pop(0)

                                    
                                print(f"Nilai tertinggi adalah {var1} dan nama {var4}")

                                ans4 = input ("Apakah ingin kembali? ( Ya / Tidak ) : ").lower()

                                if ans4 == 'ya':
                                    continue
                                
                                if ans4 == 'tidak':
                                    keluar = 0
                                    break

                                else:
                                    print("Maaf input anda tidak valid.")
                                    continue

                                    
                            elif ans3 == '4':
                                var1 = 101
                                var2 = []
                                var4 = ""
                                for b in (nama_siswa):
                                    var2.append(b)
                                for i in (nilai_siswa):
                                    if i < var1:
                                        var1 = i
                                        var4 = var2[0]
                                        if len(var2) == 1:
                                            var4 = var2[0]
                                            break
                                        else:
                                            var2.pop(0)
                                    else:
                                        var2.pop(0)

                                print(f"Nilai terendah adalah {var1} dan nama {var4}")

                                ans4 = input ("Apakah ingin kembali? ( Ya / Tidak ) : ").lower()

                                if ans4 == 'ya':
                                    continue
                                
                                if ans4 == 'tidak':
                                    keluar = 0
                                    break

                                else:
                                    print("Maaf input anda tidak valid.")
                                    continue

                                
                            elif ans3 == '5':

                                for i,b in enumerate(nama_siswa):
                                        print(f"Nama siswa : {nama_siswa[i]} dan Nilai : {nilai_siswa[i]}")

                                ans6 = (input("Masukkan nilai dari nama anak yang ingin anda cek gradenya : "))

                                if ans6 >= 90:
                                        print("Grade A")
                                elif ans6 >= 80:
                                        print("Grade B")
                                elif ans6 >= 70:
                                        print("Grade C")
                                elif ans6 >= 60:
                                        print("Grade D")
                                elif ans6 >= 50:
                                        print("Grade E")
                                else:
                                        print("Grade F")

                                ans4 = input ("Apakah ingin kembali? ( Ya / Tidak ) : ").lower()

                                if ans4 == 'ya':
                                    continue
                                
                                if ans4 == 'tidak':
                                    keluar = 0
                                    break

                                else:
                                    print("Maaf input anda tidak valid.")
                                    continue

            elif ans1 == '2':
                keluar = 0
                print("Terimakasih!")
            
            else:
                print("Maaf input anda tidak valid. Terima Kasih!")
                continue