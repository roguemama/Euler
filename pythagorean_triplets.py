'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

a = 0
b = 0
c = 0
 
for m in range(1000):
    for n in range(m):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a + b + c == 1000:
            print a * b * c