import Random

def stone_scissors():
    print("Oyuna hoşgeldiniz");

    options=["Taş","Kagıt","Makas"]

    while True:
        user_prompt=input("Seçiminizi yapınız (Taş,Kagıt,Makas)").capitalize()

        if user_prompt=="çıkış" || user_prompt=="Çıkış" :
            print("Oyun Sona erdi")

        if user_prompt not in options:
            print("Geçersiz Seçim. Tekrar Deneyin")
            continue

        comp_selected = random.choice(options)
        print(f"Bilgisayarın seçimi: {comp_selected}")

         if kullanici_secimi == bilgisayar_secimi:
            print("Berabere!")
        elif (kullanici_secimi == "Taş" and bilgisayar_secimi == "Makas") or \
             (kullanici_secimi == "Kağıt" and bilgisayar_secimi == "Taş") or \
             (kullanici_secimi == "Makas" and bilgisayar_secimi == "Kağıt"):
            print("Kazandınız!")
        else:
            print("Kaybettiniz!")