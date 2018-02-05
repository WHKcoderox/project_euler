import math

def count_factors(num):
  ans = 0
  # don't test the square root. that only adds one factor.
  for i in range(1, int(math.sqrt(num))):
    if num%i == 0:
      ans += 2 # factor pairs: num//i==j or num//j==i
  if (int(math.sqrt(num))**2 == num):
    return ans+1
  return ans+1

# main
num = 1
i = 2
while count_factors(num) <= 500:
  num += i # next triangle number
  i += 1 # next natural number
  
print(num)
