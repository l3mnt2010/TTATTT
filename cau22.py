# sàng ra các số nguyên tố trong khoảng 2 đến n
def sieve_of_eratosthenes(n):
  primes = [True] * (n+1)
  primes[0] = primes[1] = False

  for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
      for j in range(i**2, n+1, i):
        primes[j] = False
  return [i for i in range(2, n+1) if primes[i]]

def sum_Fn(L, R):
  total = 0
  primes = sieve_of_eratosthenes(R)
  for i in range(len(primes)):
    for j in range(i+1, len(primes)):
      # nếu mà số này là số nguyên tố thì Fn = N và nếu N là một hợp số thì gán bằng 0
      if primes[i] >= L and primes[j] >= L:
        total += primes[i] * primes[j] 
  return total

def main():
    L = int(input("Nhập L: "))
    R = int(input("Nhập R: "))
    
    print(f"tổng của F(i) * F(j) là {sum_Fn(L,R)}")
    
main()