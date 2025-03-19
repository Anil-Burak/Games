while True:
    sonMesaj = []
    sonuc = []
    kelime = input("Kelime: ")
    for i in range(0,6): #  Oyuncunun 6 hakkı var
        tahmin = input("Tahmin: ")
        if tahmin != kelime:
            for k in range(0,5):
                if tahmin[k] == kelime[k]:
                    sonuc.append("🟩")
                elif tahmin[k] != kelime[k] and tahmin[k] in kelime:
                    sonuc.append("🟨")
                else:
                    sonuc.append("⬜")
            sonMesaj += tahmin + " " + "".join(sonuc)
            sonuc = []
            for l in range(0, len(sonMesaj), 11):
                print("".join(sonMesaj[l:l + 11]))
            if i == 5:
                print("Deneme hakkı bitti")
        else:
            print("Kazandınız")
            break