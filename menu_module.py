class Menu:
    def __init__(self, baslik):
        self.baslik = baslik
        self.ogeler = []  

    def oge_ekle(self, ad, fonksiyon):
        """Menüye yeni seçenek ekler"""
        self.ogeler.append((ad, fonksiyon))

    def baslat(self):
        """Menüyü çalıştırır"""
        while True:
            print(f"\n==== {self.baslik} ====")
            for i, (ad, _) in enumerate(self.ogeler, start=1):
                print(f"{i}. {ad}")
            print("0. Çıkış")

            secim = input("Bir seçenek girin: ")

            if secim == "0":
                print("Programdan çıkılıyor...")
                break

            try:
                secim = int(secim)
                if 1 <= secim <= len(self.ogeler):
                    _, fonksiyon = self.ogeler[secim - 1]
                    fonksiyon()
                else:
                    print("Geçersiz seçim!")
            except ValueError:
                print("Lütfen sayı girin!")