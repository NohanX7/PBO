print("Menghitung Luas dan Volume Tabung")

# Variabel
r = 5
T = 7

# Mengimport Rumus Nilai pi
from math import pi

# Rumus
ls = 2 * pi * r * T // 1
lp = (2 * pi * r * T) + 2 * (pi * r ** 2) // 1
vol = pi * (r ** 2) * T // 1

# Menampilkan hasil
print("Luas Selimut Tabung: ", ls)
print("Luas Permukaan Tabung: ", lp)
print("Volume Tabung: ", vol)