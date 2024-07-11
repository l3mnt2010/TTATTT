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

def checkErmipNumber(n):
   n_reverse = int(str(n)[::-1])
   if miller_rabin(n,3) == "nguyên tố" and miller_rabin(n_reverse,3) == "nguyên tố":
       return True
   else:
       return False

def main():
    while True :
        try :
            n = int(input("Nhập N: "))
        except :
            print("Bạn cần phải nhập N có kiểu dữ liệu là int")
            continue
        try :
            assert n > 0
            break
        except :
            print("N cần phải lớn hơn 0")
            
    listRes = [2,3,5,7]
    for i in range(11, n):
        if checkErmipNumber(i):
            listRes.append(i)
    if len(listRes) != 0:
        print(f"Các số Emirp nhỏ hơn hoặc bằng {n} là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây số Emirp thoả yêu cầu!!!")
    print()

if __name__ == "__main__":
    main()   