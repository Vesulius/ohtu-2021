from kps import KPS
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

class PelinLataaja:
    
    @staticmethod
    def p_vs_p():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def p_vs_tkoaly():
        return KPSTekoaly()

    @staticmethod
    def p_vs_parempi_tkoaly():
        return KPSParempiTekoaly()