##Even Fibonacci numbers
##Problem 2
##Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
##
##1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##
##By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

##f(n) = f(n-1) + f(n-2)
##f(1) = 1
##f(2) = 2

##def fiboR(n):
##    if n == 1:
##        return 1
##    if n == 2:
##        return 2
##    else:
##        return fiboR(n-1) + fiboR(n-2)

#iteration

first = 1
second = 2
answer = 0
seqFibo = [1, 2]
while first + second < 4000000:
    answer = first + second
    first = second
    second = answer
    seqFibo.append(answer)

print(answer)

evenTerms = []
for term in seqFibo:
    if term % 2 == 0:
        evenTerms.append(term)

print(sum(evenTerms))
