
talabalar = {}

def qoshish():
    ism = input("Ism: ")
    yosh = int(input("Yosh: "))
    talabalar[ism] = yosh

def korish():
    if len(talabalar) == 0:
        print("Talabalar yo'q")
    else:
        for ism, yosh in talabalar.items():
            print(ism, yosh)

def ortacha():
    if len(talabalar) == 0:
        print("Talabalar yo'q")
    else:
        jami = sum(talabalar.values())
        print("O'rtacha yosh:", jami / len(talabalar))

while True:
    print("\n1. Talaba qo'shish")
    print("2. Talabalarni ko'rish")
    print("3. O'rtacha yoshni hisoblash")
    print("4. Chiqish")

    tanlov = input("Tanlov: ")

    if tanlov == "1":
        qoshish()
    elif tanlov == "2":
        korish()
    elif tanlov == "3": 
        ortacha()
    elif tanlov == "4":
        print("Dastur yakunlandi.")
        break
    else:
        print("Noto'g'ri tanlov!")
