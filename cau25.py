import random

def decompose(n, m):
    # sàng ngto
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes


    def backtrack(n, m, primes, decomposition):
        if m == 0:
            if n == 0:
                return primes
        else:
            for i in range(2, n + 1):
                if sieve(i)[i]:
                    result = backtrack(n - i, m - 1, primes + [i], decomposition)
                    if result: 
                        return result

    return backtrack(n, m, [], [])


def main():
    while True:
        n = int(input("Nhập 1<=N<=10000: "))
        m = int(input("Nhập 2<M<=100: "))
        if n >= 1 and n <= 10000:
            if m > 2 and m <= 100:
                break
            else:
                print("m phải thoả mãn 2<m<=100")
        else:
            print("n phải thoả mãn 1<=n<=10000")
            
    result = decompose(n, m)
    
    if len(result) > 0:
        print(f"Số {n} có thể được phân tích thành tổng của {m} số nguyên tố \n {result}")
    else:
        print(f"Số {n} không thể phân tích thành tổng của {m} số nguyên tố")


if __name__ == "__main__":
    main()
