from tekoaly import Tekoaly
from kps import KPS

# class KPSTekoaly:
#     def pelaa(self):
#         tuomari = Tuomari()
#         tekoaly = Tekoaly()

#         ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#         tokan_siirto = tekoaly.anna_siirto()

#         print(f"Tietokone valitsi: {tokan_siirto}")

#         while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
#             tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
#             print(tuomari)

#             ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#             tokan_siirto = tekoaly.anna_siirto()

#             print(f"Tietokone valitsi: {tokan_siirto}")

#         print("Kiitos!")
#         print(tuomari)

#     def _onko_ok_siirto(self, siirto):
#         return siirto == "k" or siirto == "p" or siirto == "s"

class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()
