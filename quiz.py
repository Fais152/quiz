def quiz():
    tebak = []
    periksa = 0
    tanya = 1
    text = '-'

    for key in pertanyaan:
        print(f'{text:->39}')
        print(key)
        for i in opsi[tanya-1]:
            print(i)
        guess = input("Jawab : ")
        guess = guess.upper()
        tebak.append(guess)

        periksa += jawaban(pertanyaan.get(key),guess)
        tanya += 1

    score(periksa, tebak)

def jawaban(jawab, guess):
    
    if jawab == guess:
        print("Benar!")
        return 1
    else: 
        print('Salah!')
        return 0

def score(periksa, tebak):
    tes = "-"
    print(f'{tes:->39}')
    print("Hasil!!")
    print(f'{tes:->39}')

    print("Jawaban : ", end="")
    for i in pertanyaan:
        print(pertanyaan.get(i), end=" ")
    print()

    print("Tebakan : ", end="")
    for i in tebak:
        print(i, end=" ")
    print()

    hasil = int((periksa/len(pertanyaan))*100)
    print("Score : "+str(hasil)+"%")

pertanyaan = {
    "Siapakah nama gubernur disamarinda? ": "A",
    "Siapakah presiden pertama indonesia?": "C",
}

opsi = [
    ["A. Isran Noor", "B. Munir", "C. Elon Musk"],
    ["A. Naruto", "B. Hashirama", "C. Jokowi"]
]

quiz()