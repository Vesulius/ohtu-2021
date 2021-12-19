from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

# class KPSParempiTekoaly:
#     def pelaa(self):
#         tuomari = Tuomari()
#         tekoaly = TekoalyParannettu(10)

#         ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#         tokan_siirto = tekoaly.anna_siirto()

#         print(f"Tietokone valitsi: {tokan_siirto}")

#         while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
#             tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
#             print(tuomari)

#             ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#             tokan_siirto = tekoaly.anna_siirto()

#             print(f"Tietokone valitsi: {tokan_siirto}")
#             tekoaly.aseta_siirto(ekan_siirto)

#         print("Kiitos!")
#         print(tuomari)

#     def _onko_ok_siirto(self, siirto):
#         return siirto == "k" or siirto == "p" or siirto == "s"

class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly_parannettu = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        self.tekoaly_parannettu.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly_parannettu.anna_siirto()
