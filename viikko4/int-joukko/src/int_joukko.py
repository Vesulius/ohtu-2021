KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.ljono = [0] * max(kapasiteetti, 1)
        self.alkioiden_lkm = 0
        self.kasvatuskoko = max(kasvatuskoko, 1)


    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        if len(self.ljono) <= self.alkioiden_lkm:
            self.ljono.extend([0] * OLETUSKASVATUS)
        
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1
        return True

    def poista(self, n):
        for i in range(0, len(self.ljono)):
            if self.ljono[i] == n:
                self.ljono.pop(i)
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True
        return False

    def kopioi_taulukko(self, kopioitava, kopio):
        kopio = kopioitava.copy()

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        palautus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            palautus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            palautus.lisaa(b_taulu[i])

        return palautus

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        palautus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    palautus.lisaa(b_taulu[j])

        return palautus

    @staticmethod
    def erotus(joukko_a, joukko_b):
        palautus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            palautus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            palautus.poista(b_taulu[i])

        return palautus

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
        
