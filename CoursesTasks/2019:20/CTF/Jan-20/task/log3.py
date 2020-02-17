from functools import reduce
from math import gcd

class prng_lcg():
    def __init__(self, seed, m, c, n):
        self.state = seed  # the "seed"
        self.m = m
        self.c = c
        self.n = n

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state



def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return multiplier, increment, modulus

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

a = [3272066543, 3047754520]
res = crack_unknown_increment(a, 2 ** 32, 42945977)

m = res[0]
c = 42945977
n = 2 ** 32

new = prng_lcg(a[0], m, c, n)

print(new.next())
print(new.next())
print(new.next())
print(new.next())
print(new.next())

