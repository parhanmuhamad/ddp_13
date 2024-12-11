from person import *

class dosen(person):
    gelar = ""
    jabatan = ""
    gaji = 0

    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan

    def setgaji(self, uang):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print("gelar \t\t:", self.gelar,
              "\njabatan \t:", self.jabatan,
              "\ngaji \t\t:", self.gaji,
              "\n---------------") 
