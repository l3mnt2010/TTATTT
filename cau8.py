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

def findTPrime(n):
   sqrt_n = pow(n,1/2) 
   sqrt_n_int = int(sqrt_n)
   return (pow(sqrt_n_int,2) == n) and miller_rabin(sqrt_n_int,3) == "nguyên tố"


def main():
    while True :
        try :
            n = int(input("Nhập N: "))
        except :
            print("Bạn cần nhập N là kiểu dữ liệu interger")
            continue
        try :
            assert n > 0
            break
        except :
            print("Bạn cần nhập N lớn hơn 0")
    listRes = []
    for i in range(1, n + 1):
        if findTPrime(i):
            listRes.append(i)
    if len(listRes) != 0:
        print(f"Các số T-Prime nhỏ hơn hoặc bằng {n} là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây số T-Prime thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()

    