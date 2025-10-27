# Blind Signature Algorithm
import random 
import numpy as np
p = int(input("İmzalayıcı: Bir asal sayı giriniz: "))
q = int(input("İmzalayıcı: Bir asal sayı giriniz: "))
n = p * q
varphi_n = (p - 1) * (q - 1)


# It is only considered 4 primes, if
if varphi_n % 3 != 0:
  e = 3
elif  varphi_n % 5 != 0:
  e = 5
elif  varphi_n % 11 != 0:
  e = 11
elif  varphi_n % 13 != 0:
  e = 13
else:
  print("false")

i = 1
while i < varphi_n + 1:
  if (e * i) % varphi_n == 1:
    d = i
    break
  else:
     i = i + 1

r = random.randint(0, n)  # 0 ve n arasından rastgele(!) bir sayı seçer

j = 1
while j < n + 1:
  if (r * j) % n == 1:
    r_inverse = j
    break
  else:
     j = j + 1

M = int(input("İmzayı Talep Eden: Mesajı Sayısal Olarak Giriniz:  "))
M_1 = ((r ** e) * M) % n
s_1 = (M_1 ** d) % n
s = (s_1 * r_inverse) % n

if (s ** e) % n == M % n:
  print("True")
  print(s,M)
else:
  print("False")
