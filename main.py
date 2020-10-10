from geometri.bangun_ruang import BangunRuang
from geometri.persegi_panjang import PersegiPanjang
from geometri.segi_tiga import SegiTiga

print('Mengugunakan OOP')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = SegiTiga(4, 2)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari kelas BanguRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())