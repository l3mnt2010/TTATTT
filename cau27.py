import math

def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while a :
        a , b = b%a , a
    return b
   

def findAB(a, b):
    listRes = []
    for i in range(a, b):
        for j in range(i + 1, b):
            if checkPrime(gcd(i, j)):
                listTmp = [i, j , gcd(i,j)]
                listRes.append(listTmp)
    return listRes


def main():
    while True:
        try :
            a = int(input("Nhập A: "))
            b = int(input("Nhập B: "))
        except :
            print("a và b là int")
            continue
        try :
            assert  0 < a < b < 1000
            break
        except :
            print("0 < a < b < 1000")
            continue
       
    listRes = findAB(a, b)
    if len(listRes) != 0:
        print(f"Các cặp số thoả yêu cầu là: {listRes}")
    else:
        print(f"Không tìm thây cặp số thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
