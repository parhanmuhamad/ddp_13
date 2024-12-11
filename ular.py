from Animal import *

print("=======ULAR======")
class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.corak = corak
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("corak \t\t: ", self.corak,
         "\nracun \t\t: ", self.racun)
        
anaconda = ular("anaconda", "kambing", "amazon", "bertelur", "batik", "tidak beracun")
anaconda.cetak_ular()

print("==========")
piton = ular("piton", "kambing", "amazon", "bertelur", "batik", "beracun")
piton.cetak_ular()

