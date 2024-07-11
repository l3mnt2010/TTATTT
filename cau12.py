def eratosthenes_sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i**2, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def find_four(n):
    primes = eratosthenes_sieve(n)
    for i in range(len(primes)  - 3):
        total = primes[i] + primes[i+1] + primes[i+2] + primes[i+3]
        if is_prime(total) == True and total <= n:
            print(primes[i])
            print(primes[i + 1])
            print(primes[i + 2])
            print(primes[i + 3])
            

def main():
  n = int(input("Nhập N: "))
  find_four(n)
  
main()
