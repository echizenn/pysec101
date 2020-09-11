#!/usr/bin/python

import math
import random

def isprime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, n):
        if math.sqrt(n) < i:
            return True
        if n%i == 0:
            return False

p, q = 0, 0
while (p==q) or not isprime(p) or not isprime(q):
    p = random.randint(10**5, 10**6)
    q = random.randint(10**5, 10**6)  # 素数でなく一致しないpとqの選択をする

print('p: ' + str(p))
print('q: ' + str(q))