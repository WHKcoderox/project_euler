##Largest prime factor
##Problem 3
##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: # if there is a factor of n
            return False
    # if there are no factors, it is prime
    return True

def factorsOf(number):
    a = []
    for i in range(2, number):
        if number % i == 0:
            a.append(i)
    return a

# main
number = 600851475143
answer = 0
factors = factorsOf(number)
for factor in factors:
    if isPrime(factor):
        answer = factor

print(answer)

