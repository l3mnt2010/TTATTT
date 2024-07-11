import math
import random

# x^y mod z
def modular_exponentiation(x, y, z):
    # thuật toán nhân bình phương có lặp
    result = 1
    x = x % z
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % z
        y = y // 2
        x = (x * x) % z
    return result

def fermat(n, t):
    for i in range(t):
        a = random.randint(2, n - 1)
        r = modular_exponentiation(a, n - 1, n)
        if r != 1:
            return "Hợp số"
    return "Nguyên tố"

def main():
    n = int(input("Nhập n >= 3: "))
    t = int(input("Nhập số lần lặp t: "))
    if fermat(n, t) == "Nguyên tố":
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")
    

if __name__ == "__main__":
    main()
    
# trong trường hợp số Carmichael thì thuật toán Fermat cho kết quả kiểm tra sai vd: 1105
# Tuy nhiên, có một số số hợp số có thể bị Fermat sai lầm và được coi là số nguyên tố. Đây là những số hợp số có dạng (2^p) + 1 với p là số nguyên tố.