import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def main():
    n = int(input("Nhập N: "))
    primes = sieve_of_eratosthenes(n)
    print(f"Tổng các số nguyên tố nhỏ hơn hoặc bằng {n} là: \n {sum(primes)}")
    
main()