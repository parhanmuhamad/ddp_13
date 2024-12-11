from mahasiswa import * 
from dosen import *

m1 = mahasiswa("dea rahayu", "laki laki",23,"SI",1)
m2 = mahasiswa("uun nurpalah", "laki laki",20,"TI",1)
d1 = dosen("tika kartika", "wanita", 45,"s.Si, M.kom","ber" )
d2 = dosen("kartika", "wanita", 47,"s.Si, M.kom", "gd")

d1.setgaji(6000000)
d2.setgaji(7800000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()