import random

# thuật toán nhân bình phương có lặp
def modular_exponentiation(x, y, z):
    result = 1
    x = x % z
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % z
        y = y // 2
        x = (x * x) % z
    return result

def miller_rabin(n, t):
        # Đầu vào: Một số nguyên lẻ 𝑛 ≥ 3 và tham số an toàn t ≥ 1
    if n < 2 or t <= 0:
        return "hợp số", 0
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    probability = 1
    for i in range(t):
        a = random.randint(2, n - 2)
        y = modular_exponentiation(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = pow(y, 2, n)
                if y == 1:
                    return "hợp số", probability
                j += 1
            if y != n - 1:
                return "hợp số", probability
        probability *= (1 - (1 / (4**t)))
    return "nguyên tố", probability


def main():
    while True:
        try : 
            n = int(input("Nhập N: "))
            t = int(input("Nhập số lần thử T: "))
        except :
            print("Các số nhập là int")
            continue
        try :
            assert n > 0 and t > 0
            break
        except :
            print("n > 0 and t > 0")
            continue
    result, probability = miller_rabin(n, t)
    print(f"Kết luận: {n} là {result}. Xác suất kết luận sau thuật toán là: {probability}")



if __name__ == "__main__":
    main()
    
# Trong thuật toán Miller-Rabin, xác suất kết luận sau thuật toán được tính bằng cách
# Tính tổng của tỷ lệ khả năng mỗi lần lặp t có kết luận là "nguyên tố" (1/2^t). 
# Ví dụ, nếu số lần lặp t là 10, thì xác suất kết luận sau thuật toán là 1 - (1/4^10)