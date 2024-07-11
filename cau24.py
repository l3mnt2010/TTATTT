import math


# sàng số nguyên tố
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

    # tạo ra 2 mảng S1, S2 chứa bình phương các số nguyên nhỏ hơn b^1/2 + 1
    S1 = [i**2 for i in range(int(math.sqrt(b)) + 1)]
    S2 = [i**2 for i in range(int(math.sqrt(b)) + 1)]
    
    primes = sieve_of_eratosthenes(b)
    # lọc chỉ lấy nhưng phần tử nằm khoảng [A, B]
    primes = [p for p in primes if a <= p <= b]
    
    pairs = []

    for n in primes:
        for x in S1:
            if x > n:
                break
            y = n - x
            if y in S2:
                if x > y:
                    # Hoán đổi x ,y để loại bỏ sự lặp lại
                    x, y = y, x
                pairs.append((x, y))
                
    # Xóa những phần tử lặp lại
    pairs = list(set(pairs))                

    print("Các cặp x^2 và y^2 và số nguyên tố thoả mãn là:")
    for pair in pairs:
        print(pair, sum(pair))
    print(f"Có {len(pairs)} số nguyên tố thuộc khoảng [{a},{b}] thoả mãn yêu cầu đề bài")

if __name__ == "__main__":
    main()
