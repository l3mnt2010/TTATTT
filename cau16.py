import random
import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def generateRandomList(n):
    listRandom = []
    for i in range(n):
        listRandom.append(random.randint(1, 500))
    return listRandom


def findPrimeFromRandomList(n):
    listRandom = generateRandomList(n)
    listResult = []
    for i in listRandom:
        if checkPrime(i):
            listResult.append(i)
    return listRandom, listResult


def main():
  
    while True :
        try :
            n = int(input("Nhập n :"))
        except :
            print("N là int")
            continue
        try :
            assert n > 0
            break
        except :
            print("N > 0")
    
    listSrc, listRes = findPrimeFromRandomList(n)
    print(f"Mảng sinh ngẫu nhiên {n} phần tử: {listSrc}")
    if len(listRes) != 0:
        print(f"Các số nguyên tố trong mảng ngẫu nhiên {n} phần tử trên là: {listRes}")
    else:
        print(f"Không tìm thây số nguyên tố trong mảng ngẫu nhiên {n} phần tử trên")
    print()


if __name__ == "__main__":
    main()
