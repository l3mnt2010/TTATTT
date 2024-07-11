import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

## kiểm tra xem số lượng các số nguyên tố từ 1 đến n có phải là số nguyên tố hay không
def checkSuperPrime(n):
    cntPr = 0
    for i in range(1, n):
        if checkPrime(i):
            cntPr += 1
    return checkPrime(cntPr)

## tìm siêu số nguyên tố
def findSuperPrime(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if checkSuperPrime(i):
            cnt += 1
    return cnt


def main():
    while True:
        try :
            a = int(input("Nhập A: "))
            b = int(input("Nhập B: "))
        except :
            print("A và B bạn nhập phải là interger")
            continue
        try :
            assert a > 0 and b > 0 and a < b
            break
        except :
            print("A > 0 and B > 0 and A < B")
            continue 
        
    print(f"Số các siêu số nguyên tố trong đoạn [{a}, {b}] là: ", end="")
    print(findSuperPrime(a, b))


if __name__ == "__main__":
    main()
