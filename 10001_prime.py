'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


count = 2
prime_num = []
while len(prime_num) < 10001:
    if not any(count%i == 0 for i in range(2, count)):
        prime_num.append(count)
    count+=1
print count
print prime_num