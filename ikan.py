from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, berkumis):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.warna = warna
        self.berkumis = berkumis

    def cetak_ikan(self):
        super().cetak()
        print("warna \t\t: ", self.warna,
         "\nberkumis \t: ", self.berkumis)
        
lele = ikan("lele", "daun", "sungai", "bertelur", "bunga", "tidak dimakan hidup hidup")
lele.cetak_ikan()

cupang = ikan("cupang", "daun", "sungai", "bertelur", "bunga", "tidak dimakan hidup hidup")
cupang.cetak_ikan()