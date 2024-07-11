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

def main():
  A = int(input("Nhập A: "))
  B = int(input("Nhập B: "))
  tong = 0
  for i in range(A, B + 1):
     if miller_rabin(i, 3) == "nguyên tố":
             tong+=i
  print(f"Tổng của các số nguyên tố nằm trong khoảng [{A}, {B}] là {tong}", end="")
  
if __name__ == "__main__":
   main()