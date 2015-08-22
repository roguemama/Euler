'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
evenly_divisible = []
 
 
for i in range(5000000,500000000):
    if len(evenly_divisible) < 20:
        for g in range(1,21):
            if i%g != 0:
                evenly_divisible = []
            else:
                evenly_divisible.append(i)
    else:
        break
 
print evenly_divisible