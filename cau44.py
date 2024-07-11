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

def binary_gcd(a, b):
    # thuật toán binary gcd
    u = a
    v = b
    e = 1
    while u % 2 == 0 and v % 2 == 0:
        u = u // 2
        v = v // 2
        e = e * 2
    while u != 0:
        while u % 2 == 0:
            u = u // 2
        while v % 2 == 0:
            v = v // 2
        if u >= v:
            u = u - v
        else:
            v = v - u
    return e * v

# thuật toán Binary gcd trong Fp
def inverse_mod(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while (u != 1 and v != 1):
        while u % 2 == 0:
            u = u // 2
            if x1 % 2 == 0:
                x1 = x1 // 2
            else:
                x1 = (x1 + p) // 2
        while v % 2 == 0:
            v = v // 2
            if x2 % 2 == 0:
                x2 = x2 // 2
            else:
                x2 = (x2 + p) // 2
        if u >= v:
            u = u - v
            x1 = x1 - x2
        else:
            v = v - u
            x2 = x2 - x1
        # print(f" v = {v} u = {u} x2 = {x2} x1 = {x1}")
    if u == 1:
        return x1 % p
    else:
        return x2 % p

def main():
    p = int(input("Nhập số nguyên p: "))
    
    if miller_rabin(p, 4) == "nguyên tố":
        A = input("Nhập mảng A: ")
        A = [int(x) for x in A.split()]
        
        result = []
        
        for i in A:
            result.append(inverse_mod(i, p))
    
    print(f"Mảng A: {A}")
    print(f"Nghịch đảo tương ứng: {result}")
    

if __name__ == "__main__":
    main()