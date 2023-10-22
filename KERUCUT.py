print("Menghitung Luas dan Volume Kerucut")

# Variabel
r = 6
s = 10
T = 8

# Mengimport Rumus Nilai pi
from math import pi

# Rumus
ls = pi * r * s // 1
lp = (pi * r * s) + pi * (r ** 2) // 1
vol = (1/3) * pi * (r ** 2) * T // 1

# Output
print("Jari-Jari :", r)
print("Garis Pelukis :", s)
print("Tinggi :", T)
print("Luas Permukaan Kerucut :", lp)
print("Volume Kerucut :", vol)