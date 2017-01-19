##Largest palindrome product
##Problem 4
##A palindromic number reads the same both ways. The largest palindrome
##made from the product of two 2-digit numbers is 9009 = 91 × 99.
##
##Find the largest palindrome made from the product of two 3-digit numbers.

maximum = 998001 # largest product of 2 3 digit numbers (i.e. 999 ** 2)

def dfactors(n):
    a = []
    for i in range(100, 1000):
        if n % i == 0 and 99 < (n / i) < 1000:
            a.append(i)
            a.append(n / i)
    return a

def pArray(a):
    for element in a:
        print(element)

def digit(n, di):
    return (n//(10**(di-1)))%10

def count_digits(n):
    i = 0
    while n//(10**i) > 0:
        i += 1
    return i
#palindromic whereby
#   First digit is the same as the last digit
#   Second digit is the same as the second last digit
#   Third digit is the same as the third last digit

n = maximum
cont = True
while cont:
    n -= 1
    factors = []
    if count_digits(n) == 6:
        if digit(n, 1) == digit(n, 6) and digit(n, 2) == digit(n, 5) and digit(n, 3) == digit(n, 4):
        # for every palindrome, find the 3 digit factors
            factors = dfactors(n)
            if len(factors) >= 2: # if palindrome is made of 2 3 digit factors                cont = False
                print(n)
    elif count_digits(n) == 5:
        if digit(n, 1) == digit(n, 5) and digit(n, 2) == digit(n, 4):
        # for every palindrome, find the 3 digit factors
            factors = dfactors(n)
            if len(factors) >= 2: # if palindrome is made of 2 3 digit factors                cont = False
                print(n)
