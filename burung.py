from Animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, terbang, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.terbang = terbang
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("terbang \t: ", self.terbang,
         "\nbunyi \t\t: ", self.bunyi)
        
pipit = burung("pipit", "padi", "pohon", "bertelur", "dikandangin", "gacor")
pipit.cetak_burung()

merpati = burung("merpati", "padi", "pohon", "bertelur", "dikandangin", "gacor")
merpati.cetak_burung()
