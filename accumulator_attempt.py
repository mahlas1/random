# Candidate Accumulator Implementation (it is not an accumulator)
import random
import hashlib
import math
import numpy as np

matrices = []
matrices_inverses = []
TCKN = random.getrandbits(36) # 11 digit TCKN approximately 36 bits
# print(len(str(abs(TCKN)))) # gives number of digits of a given number

hash_hex_1 = hashlib.sha256(str(TCKN).encode()).hexdigest()
hash_int_1 = int(hash_hex_1, 16)

if hash_int_1 % 2 == 0:
  hash_int_1 = hash_int_1  + 1      # no need to make them odd, they will be coprime when divided by gcd()wrong thoughts
else:
   hash_int_1 = hash_int_1

hash_hex_2 = hashlib.sha256(str(TCKN + hash_int_1).encode()).hexdigest()
hash_int_2 = int(hash_hex_2, 16)

if hash_int_2 % 2 == 0:
  hash_int_2 = hash_int_2  + 1
else:
   hash_int_2 = hash_int_2




gcd_old = math.gcd(hash_int_1, hash_int_2)
print("gcd_old", gcd_old)
hash_int_1 = int(hash_int_1 // gcd_old)
hash_int_2 = int(hash_int_2 // gcd_old)



gcd_new = math.gcd(hash_int_1, hash_int_2)
print("gcd_new", gcd_new)



def extended_gcd(a, b):  #finding Bezout's identity
    if b == 0:
        return a, 1, 0  # gcd, x, y
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example:
a = hash_int_1
b = hash_int_2
gcd, x, y = extended_gcd(a, b)
print(f"gcd({a}, {b}) = {gcd}")
print(f"Bezout coefficients: x = {x}, y = {y}")
print(f"Check: {a}*{x} + {b}*{y} = {a*x + b*y}")

# the x and y are not unique, to make the unique matrix corresponding to the TCKN, make x and y unique(because the output of the hash of a different inputs are
# statistically unique). The constraint is that x is the smallest positive even number, y is the corresponding number which must be a negative odd number.


m = 1
while m > 0:
  if x % 2 == 0 and x < 0: # x  is even and negative
    t = 2
    while t > 0:
      if (x + t * b) > 0:
        x = x + t * b
        y = y - t * a
        m = m - 1
        print(1)
        break
        break
      else:
        t = t + 2

  if x % 2 == 1 and x < 0: # x  is odd and negative
    t = 1
    while t > 0:
      if (x + t * b) > 0:
        x = x + t * b
        y = y - t * a
        m = m - 1
        print(2)
        break
        break
      else:
        t = t + 2

  if x % 2 == 1 and x > 0: # x is odd and positive
    t = 3
    while t > 0:
      if (x - b) < 0:
        x = x + b
        y = y - a
        m = m - 1
        print(3)
        break
        break
      elif (x - t * b) < 0:
        x = x - (t - 2) * b
        y = y + (t - 2) * a
        m = m - 1
        print(5)
        break
        break
      else:
        t = t + 2

  if x % 2 == 0 and x > 0: # x is even and positive
    t = 2
    while t > 0:
      if x - b < 0:
        x = x
        y = y
        m = m - 1
        print(4)
        break
        break
      elif (x - t * b) < 0:
        x = x - (t - 2) * b
        y = y + (t - 2) * a
        m = m - 1
        print(6)
        break
        break
      else:
        t = t + 2

print(f"___Check___: {a}*{x} + {b}*{y} = {a*x + b*y}")
print("x(should be even positive) = ", x)
print("y(should be odd negative) =" ,y)
print("a = ",a)
print("b = ",b)

A = np.array([[a, b],
              [-y, x]])

B = np.array([[x, -b],
              [y, a]])





matrices.append(np.array([[a, b], [-y, x]]))


for m in matrices:
  print(m, "\n")
