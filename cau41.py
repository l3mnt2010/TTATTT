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
    while True:
        print("Nhập a, k, n với điều kiện 0 < a,k < n < 1000")
        a = int(input("Nhập a: "))
        k = int(input("Nhập k: "))
        n = int(input("Nhập n: "))
        if a > 0 and k > 0 and n > 0 and n < 1000:
            if a < n and k < n:
                break
    
    result = modular_exponentiation(a, k, n)
    if miller_rabin(result, 10) == "nguyên tố":
        print(f"Kết luận: {a}^{k} mod {n} = {result} là số nguyên tố")
    else:
        print(f"Kết luận: {a}^{k} mod {n} = {result} không phải là số nguyên tố")

if __name__ == "__main__":
    main()