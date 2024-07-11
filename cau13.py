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

def find_primes(n):
    primes = eratosthenes_sieve(n)
    for i in range(len(primes)):
        for j in range(len(primes)):
            if i != j:
                if is_prime(abs(primes[i] - primes[j])) and is_prime(primes[i] + primes[j]):
                    print(primes[i])
                    print(primes[j])
                    return
            

def main():
  n = int(input("Nhập N: "))
  find_primes(n)

main()