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

def calculate(N):
    p,s,q,k = 0, 0, 0, 0
    for i in range(1, N+1):
        if(N % i == 0):
             s+=1
             p+=i
             if miller_rabin(i,3) == "nguyên tố":
                      k+=1
                      q += i
    return p + s - q - k


def main():
    while True : 
        try :
            N = int(input("Nhập n :"))
        except :
            print("N là int")
          
        try :
            assert N > 0
            break
        except :
            print("N > 0")
            
    result = N + calculate(N)
    print(f"Tổng cần tìm là: N + p + s - q - k = {result}", end="")
if __name__ == "__main__":
    main()