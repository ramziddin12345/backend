class Belgi:
    def __init__(self, ism, daraja, salomatlik, hujum_kuchi):
        self.ism = ism
        self.daraja = daraja
        self.salomatlik = salomatlik
        self.hujum_kuchi = hujum_kuchi

    def __str__(self):
        return f"{self.ism} (Daraja: {self.daraja}, Salomatlik: {self.salomatlik}, Hujum kuchi: {self.hujum_kuchi})"

class Jangchi(Belgi):
    def __init__(self, ism, daraja):
        super().__init__(ism, daraja, 100 + 10 * daraja, 10 + 2 * daraja)

    def hujum(self, boshqa):
        zarar = self.hujum_kuchi
        boshqa.salomatlik -= zarar
        print(f"{self.ism} {boshqa.ism}ga hujum qildi va {zarar} zarar berdi.")

class Mage(Belgi):
    def __init__(self, ism, daraja):
        super().__init__(ism, daraja, 60 + 8 * daraja, 15 + 3 * daraja)
        self.mana = 50 + 5 * daraja

    def use_magic(self, boshqa):
        zarar = self.hujum_kuchi + 5
        boshqa.salomatlik -= zarar
        self.mana -= 10
        print(f"{self.ism} {boshqa.ism}ga sehr ishlatdi va {zarar} zarar berdi. Mana qolgan: {self.mana}")

class Archer(Belgi):
    def __init__(self, ism, daraja):
        super().__init__(ism, daraja, 80 + 9 * daraja, 12 + 3 * daraja)

    def hujum(self, boshqa):
        zarar = self.hujum_kuchi
        boshqa.salomatlik -= zarar
        print(f"{self.ism} {boshqa.ism}ga kamondan otib hujum qildi va {zarar} zarar berdi.")

def main():
    belgilar = []
    while True:
        print("\nMenyu:")
        print("1. Yangi belgi yaratish")
        print("2. Belgilar ro'yxatini ko'rsatish")
        print("3. Belgilar bilan muloqot qilish")
        print("4. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == '1':
            ism = input("Ismni kiriting: ")
            print("Belgi turini tanlang:")
            print("1. Jangchi")
            print("2. Mage")
            print("3. Archer")
            tur_tanlov = input("Tanlang: ")
            daraja = int(input("Darajasini kiriting: "))

            if tur_tanlov == '1':
                belgi = Jangchi(ism, daraja)
            elif tur_tanlov == '2':
                belgi = Mage(ism, daraja)
            elif tur_tanlov == '3':
                belgi = Archer(ism, daraja)
            else:
                print("Noto'g'ri tanlov.")
                continue

            belgilar.append(belgi)
            print(f"{belgi} yaratildi.")

        elif tanlov == '2':
            for belgi in belgilar:
                print(belgi)

        elif tanlov == '3':
            if len(belgilar) < 2:
                print("Kamida 2 ta belgi bo'lishi kerak.")
                continue

            hujumchi = input("Hujumchi belgini tanlang (ism): ")
            nishon = input("Nishon belgini tanlang (ism): ")

            hujumchi_belgi = next((b for b in belgilar if b.ism == hujumchi), None)
            nishon_belgi = next((b for b in belgilar if b.ism == nishon), None)

            if hujumchi_belgi and nishon_belgi:
                if isinstance(hujumchi_belgi, Mage):
                    hujumchi_belgi.use_magic(nishon_belgi)
                else:
                    hujumchi_belgi.hujum(nishon_belgi)
                print(f"{nishon_belgi} ning salomatligi: {nishon_belgi.salomatlik}")
            else:
                print("Noto'g'ri ismlar kiritildi.")

        elif tanlov == '4':
            print("Chiqish")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, qaytadan kiriting.")

if __name__ == "__main__":
    main()
