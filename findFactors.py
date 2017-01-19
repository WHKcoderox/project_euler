def pFactors(n):
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            print(i)
            largest = i

pFactors(600851475143)
