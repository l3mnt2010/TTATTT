import math
import random

# miller rabin check số nguyên tố
def miller_rabin(n, t):
    # Đầu vào: Một số nguyên lẻ 𝑛 ≥ 3 và tham số an toàn t ≥ 1
    if n < 2:
        return "hợp số"
    if n == 2 or n == 3:
        return "nguyên tố"
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    for i in range(t):
        a = random.randint(2, n - 2)
        y = pow(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = pow(y, 2, n)
                if y == 1:
                    return "hợp số"
                j += 1
            if y != n - 1:
                return "hợp số"
    return "nguyên tố"

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def main():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    
    primes = sieve_of_eratosthenes(b)
    primes = [p for p in primes if a <= p <= b]
    print(f"Tổng là: {sum(primes)}")
    
    if miller_rabin(sum(primes), 10) == "nguyên tố":
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
