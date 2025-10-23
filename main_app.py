from menu_module import Menu

hayvan_listesi = []

def hayvan_ekle():
    print("\n--- Yeni Hayvan Ekle ---")
    ad = input("Hayvanın adı: ")
    tur = input("Hayvanın türü (kedi, köpek vb): ")
    yas = input("Yaşı: ")
    sahip = input("Sahip adı: ")

    hayvan = {
        "Ad": ad,
        "Tür": tur,
        "Yaş": yas,
        "Sahip": sahip
    }
    hayvan_listesi.append(hayvan)
    print(f"{ad} başarıyla eklendi!")

def hayvanlari_listele():
    print("\n--- Kayıtlı Hayvanlar ---")
    if not hayvan_listesi:
        print("Henüz kayıt yok.")
        return

    for i, h in enumerate(hayvan_listesi, start=1):
        print(f"{i}. Ad: {h['Ad']}, Tür: {h['Tür']}, Yaş: {h['Yaş']}, Sahip: {h['Sahip']}")

def hayvan_sil():
    print("\n--- Hayvan Sil ---")
    if not hayvan_listesi:
        print("Silinecek kayıt yok.")
        return

    hayvanlari_listele()
    try:
        no = int(input("Silmek istediğiniz hayvan numarası: "))
        if 1 <= no <= len(hayvan_listesi):
            silinen = hayvan_listesi.pop(no - 1)
            print(f"{silinen['Ad']} başarıyla silindi.")
        else:
            print("Geçersiz numara!")
    except ValueError:
        print("Lütfen sayı girin!")

def main():
    menu = Menu("Veteriner Takip Sistemi")

    menu.oge_ekle("Yeni hayvan ekle", hayvan_ekle)
    menu.oge_ekle("Hayvanları listele", hayvanlari_listele)
    menu.oge_ekle("Hayvan kaydı sil", hayvan_sil)

    menu.baslat()

if __name__ == "__main__":
    main()