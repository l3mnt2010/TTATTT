
import random

# thuật toán miller rabin kiểm tra tính nguyên tố
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

# thuật toán random search sinh số snt k bit
def random_search(k, t):
    while True:
        n = random.getrandbits(k)
        primes = [2,3,5,7,11,13,17,19]
        for i in primes:
            if n % i == 0:
                continue
        if miller_rabin(n, t) == "nguyên tố":
            return n

 
def main():
    N = int(input("Nhập N: "))
    
    A = []
    for i in range(0, N):
        A.append(random_search(10, 10))
    print("Mảng nguyên tố sau khi sinh:")
    print(A)
    
    B = sorted(A)
    min_diff = float("inf")
    for i in range(len(B) - 1):
        diff = B[i + 1] - B[i]
        if diff < min_diff:
            min_diff = diff
        
    print("Mảng sau khi sắp xếp:")
    print(B)
    print(f"Khoảng cách nhỏ nhất giữa hai số bất kỳ trong mảng là: {min_diff}")

if __name__ == "__main__":
    main()
    