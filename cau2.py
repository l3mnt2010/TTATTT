def sieve_of_eratosthenes(A, B):
    n = B + 1
    prime = [True for _ in range(n)]
    prime[0] = False
    prime[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
    result = []
    for i in range(A, B + 1):
        if prime[i]:
            result.append(i)
    return result

def segmented_sieve(A, B):
    result = []
    primes = sieve_of_eratosthenes(2, int(B ** 0.5))
    num_segments = (B - A) // int(B ** 0.5) + 1
    for i in range(num_segments):
        lower = A + i * int(B ** 0.5)
        upper = min(lower + int(B ** 0.5) - 1, B)
        segment = [True for _ in range(upper - lower + 1)]
        for p in primes:
            start = lower + (p - (lower % p)) % p

            for j in range(start, upper + 1, p):
                if j != p:
                    segment[j - lower] = False
        for i in range(upper - lower + 1):
            if segment[i]:
                result.append(i + lower)
    return result

def main():
    N = int(input("Nhập n: "))
    primes = segmented_sieve(10**(N-1), 10**N)

    print(f"Các số nguyên tố có {N} chữ số là: \n {primes}")
    print(f"Tìm thấy {len(primes)} số")

main()

