import random

def miller_rabin(n, t):
    # thuật toán miller rabin kiểm tra tính nguyên tố
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

# thuật toán nhân bình phương có lặp
def modular_exponentiation(x, y, z):
    result = 1
    x = x % z
    #i = 0
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % z
        #print(f"{i} {x} {result}")
        y = y // 2
        x = (x * x) % z
        #i += 1
    return result


def main():
    # Sinh ra 2 số nguyên tố p và q
    while True:
        p = random.randint(0, 1000)
        q = random.randint(0, 1000)
        if miller_rabin(p, 4) == "nguyên tố" and miller_rabin(q, 4) == "nguyên tố":
            break
    
    print(f"p = {p}, q = {q}")
    result = []
    for i in range(1, 100):
        if miller_rabin(modular_exponentiation(i, p, q), 4) == "nguyên tố":
            result.append(i)
    
    print(f"Các kết quả thoả mãn a^{p} mod {q} là số nguyên tố : {result}")
    

if __name__ == "__main__":
    main()