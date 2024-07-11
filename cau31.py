import random
import re

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

def ngto_gan_nhat(student_code):
  student_code = int(student_code)
  # Kiểm tra nếu mã sinh viên đã là nguyên tố
  if miller_rabin(student_code, 4) == "nguyên tố":
    return student_code
  # Tìm số nguyên tố gần mã số sinh viên nhất mà nhỏ hơn mã sinh viên
  i = student_code - 1
  while i > 1:
    if miller_rabin(i, 4) == "nguyên tố":
      return i
    i -= 1
  # Tìm số nguyên tố gần mã số sinh viên nhất mà lớn hơn mã sinh viên
  i = student_code + 1
  while True:
    if miller_rabin(i, 4) == "nguyên tố":
      return i
    i += 1

# x^y mod z
def modular(x, y, z):
    result = 1
    x = x % z
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % z
        y = y // 2
        x = (x * x) % z
    return result

def main():
  alphanumeric_code = input("Nhập mã sinh viên: ")
  student_code = int(re.search(r'\d+', alphanumeric_code).group())
  k = ngto_gan_nhat(student_code)
  a = int(input("Nhập SBD: "))
  n = 123456
  result = modular(a, k, n)
  print(f"Số nguyên tố gần phần số của mã SV bạn là: k = {k}")
  print(f"a^k mod n = {result}")

if __name__ == "__main__":
  main()
