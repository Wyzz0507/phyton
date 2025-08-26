import random
     
def questionlvl1():
    operation = random.choice (["+", "-"])
    num1 = random.randint (10, 60)
    num2 = random.randint (30, 40)

    if operation == '+':
        correct_answer = (num1 + num2)
    elif operation == '-':
        correct_answer = (num1 - num2)
    
    soal = f"Berapakah hasil dari operasi ini? {num1} {operation} {num2}"
    return soal, correct_answer

def questionlvl2():
    operation = random.choice (["*", "/"])
    num1 = random.randint (10, 100)
    num2 = random.randint (20, 60)

    if operation == '*':
        correct_answer = (num1 * num2)
    elif operation == '/':
        correct_answer = round (num1 / num2, 2)
    
    soal = f"Berapakah hasil dari operasi ini? {num1} {operation} {num2}"
    return soal, correct_answer

skor = 0
nyawa = 3
all_question = 5

while True: 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Selamat datang di kuis matematika")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("Terdapat aturan di dalam kuis ini : ")
    print("1. Anda memiliki 3 nyawa dalam setiap opsi level.")
    print("2. Terdapat 4 level")
    print("3. Apabila nyawa anda = 0, maka anda dinyatakan gugur.")

    ans1 = input("Apakah anda bersedia? ( Yes / No ) : ")
    ans2 = ans1.lower()

    if ans2 == 'yes':
        print("Silahkan memilih opsi level dibawah ini : ")
        print("1. Level Easy ")
        print("2. Level Hard ")

    elif ans2 == 'no':
        print("Terimakasih!")
        break

    else : 
        print("Input anda tidak valid.")
        continue 
    
    
    ans_level = input("Silahkan memilih level ( 1 / 2 ) : ")

    if ans_level == '1':
        print("Level Easy")
        for i in range(all_question):
            soal, correct_answer = questionlvl1()
            print(f"Soal{i+1}: {soal}")
            jawaban = input("Jawaban anda :\n")
            try:
                if float(jawaban) == correct_answer:
                    skor += 100
                    print(f"Benar!, skor anda {skor}\n")
                else:
                    print(f"Salah! Jawaban yang benar adalah {correct_answer}, nyawa anda {nyawa}\n")
                    nyawa -= 1
            except:
                nyawa -= 1
                print(f"Input tidak valid. Nyawa anda tersisa {nyawa}\n")

    if nyawa == 0:
                print("💀 Nyawa habis! Kamu gugur.")

    elif ans_level == '2':
        print("Level Hard")
        for i in range(all_question):
            soal, correct_answer = questionlvl2()
            print(f"Soal{i+1}: {soal}")
            jawaban = input("Jawaban anda :\n")
            try:
                if float(jawaban) == correct_answer:
                    skor += 100
                    print(f"Benar!, skor anda {skor}\n")
                else:
                    print(f"Salah! Jawaban yang benar adalah {correct_answer}, nyawa anda {nyawa}\n")
                    nyawa -= 1
            except:
                nyawa -= 1
                print(f"Input tidak valid. Nyawa anda tersisa {nyawa}\n")

    if nyawa == 0:
                print("💀 Nyawa habis! Kamu gugur.")
    
    break 

print(f"Permainan selesai! Skor akhir kamu: {skor} dari {all_question} pertanyaan \n")