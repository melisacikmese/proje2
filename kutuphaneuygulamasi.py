from menumodul import Menu

kutuphane = []

def kitap_ekle():
    print("\nYeni Kitap Ekle")
    ad = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yil = input("Basım yılı: ")
    kitap = {"Ad": ad, "Yazar": yazar, "Yıl": yil}
    kutuphane.append(kitap)
    print(f"{ad} eklendi.")

def kitaplari_listele():
    print("\nKayıtlı Kitaplar")
    if not kutuphane:
        print("Henüz kitap yok.")
        return
    for i, k in enumerate(kutuphane, start=1):
        print(f"{i}. {k['Ad']} - {k['Yazar']} ({k['Yıl']})")

def kitap_sil():
    print("\nKitap Sil")
    if not kutuphane:
        print("Silinecek kitap yok.")
        return
    kitaplari_listele()
    try:
        no = int(input("Silmek istediğiniz kitabın numarası: "))
        if 1 <= no <= len(kutuphane):
            silinen = kutuphane.pop(no - 1)
            print(f"{silinen['Ad']} silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen sayı girin.")

def main():
    menu = Menu("Kütüphane Takip Sistemi")
    menu.oge_ekle("Yeni kitap ekle", kitap_ekle)
    menu.oge_ekle("Kitapları listele", kitaplari_listele)
    menu.oge_ekle("Kitap sil", kitap_sil)
    menu.baslat()

if __name__ == "__main__":
    main()