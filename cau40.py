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

# thuật toán tìm ước chung lớn nhất binary_gcd
def binary_gcd(a, b):
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

# Hàm tìm các cặp số
def find_pairs(A):
  pairs = []
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      g = binary_gcd(A[i], A[j])
      if miller_rabin(g, 4) == "nguyên tố":
            if (A[j], A[i]) not in pairs:
                pairs.append((A[i], A[j]))
  pairs = list(set(pairs))
  return sorted(pairs)

# Nhập mảng A từ bàn phím
A = list(map(int, input("Nhập mảng A: ").split()))

# Tìm các cặp số và in ra kết quả
pairs = find_pairs(A)
sum = len(pairs)
if pairs:
  print(f"Tìm thấy {sum} cặp số có ước chung lớn nhất là số nguyên tố")
  for pair in pairs:
    print(pair)
else:
  print("Không tìm thấy")