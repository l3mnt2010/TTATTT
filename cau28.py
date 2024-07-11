import random

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

def gcd(a, b):
    while a :
        a , b = b % a , a
    return b

def is_carmichael(n):
    if miller_rabin(n, 10) == "nguyên tố":
        return False
    for b in range(2, n):
        # check xem b và n có phải là số nguyên tố cùng nhau hay không
        if gcd(b, n) == 1:
            # check b^(n-1) mode n có đồng dư với 1 hay không
            if pow(b, n-1, n) != 1:
                return False
    return True

def find_carmichael(N):
    # Tìm số Carmichael nhỏ hơn N
    carmichael_numbers = []
    for n in range(2, N):
        if is_carmichael(n):
            carmichael_numbers.append(n)
    return carmichael_numbers

def main() :
    while True :
        try :
            N = int(input("Nhập N: "))
        except :
            print("N là int")
            continue
        try :
            assert 0 <= N <= 10000
            break
        except :
            print("0 <= N <= 10000")
            continue
    if 0 <= N <= 10000:
        print(f"Các số Carmichel nhỏ hơn {N} là : {find_carmichael(N)}")
    else :
        print("None")
if __name__ == "__main__":
    main()

