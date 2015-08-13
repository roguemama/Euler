'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


import math
 
def is_prime(n):
    if not any(n%i == 0 for i in range(2, n)):
        return n
 
def largest_prime_factor(num):
    factors = []
    primes = []
    for i in range(2,int(math.sqrt(num))):
        if num%i == 0:
            factors.append(i)
    for l in factors:
        primes.append(is_prime(l))
    return max(primes)

print largest_prime_factor(600851475143)