print("Menghitung Luas dan Volume Prisma Segitiga")

# variabel
s1 = 5
s2 = 6
s3 = 7
T = 7
a = 4
t = 6

# Rumus
ls = (s1 + s2 + s3) * T
lp = (s1 + s2 + s3) * T + (a + t)
vol = (a * t * T / 2)

# Output
print("Sisi 1 : ", s1)
print("Sisi 2 : ", s2)
print("Sisi 3 : ", s3)
print("Tinggi Prisma : ", T)
print("Tinggi : ", t)
print("Alas : ", a)
print("Luas Selimut Prisma Segitiga : ", ls)
print("Luas Permukaan Prisma Segitiga : ", lp)
print("Volume Prisma Segitiga : ", vol)