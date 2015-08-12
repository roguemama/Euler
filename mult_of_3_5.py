'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def mult_of_3_and_5(top_num):
    multiples = []
    for i in range(1,top_num):
        if (i % 3 == 0):
            multiples.append(i)
        elif (i % 5 == 0):
            multiples.append(i)
#    print multiples
    return multiples

print "What is your max number?"
your_num = input()
print "The sum of the multiples of 3 and 5 under", your_num, "is", sum(mult_of_3_and_5(your_num))