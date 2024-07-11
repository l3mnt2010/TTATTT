# hàm kiểm tra số nguyên tố với độ phức tạp của thuật toán là O(log(n^1/2))
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



n = int(input("Nhập giới hạn của x (là N trong đề bài): "))
A = int(input("Nhập số nguyên A: "))
B = int(input("Nhập số nguyên B: "))
C = int(input("Nhập số nguyên C: "))

# Tìm số nguyên dương x nhỏ nhất sao cho giá trị của biểu thức A*x^2+B*x+C là số nguyên tố
x = 1
while True:
    result = A*x**2 + B*x + C
    if is_prime(result):
        print(f"Số nguyên dương x nhỏ nhất mà chúng tôi tìm thấy đó là {x}")
        break
    x += 1
    if x >= n:
        print("Không có giá trị thoả mãn yêu cầu của bạn")
        break
