import math

def sieveOfEratosthenes(n):
    listPrime = []
    check = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(100, n + 1):
        if check[p]:
            listPrime.append(p)
    return listPrime

def reverse(n) :
    return int(str(n)[::-1])



def findNumber():
    listNum = sieveOfEratosthenes(999)
    listResult = []
    for i in listNum:
            if pow(reverse(i),1/3) == int(pow(reverse(i),1/3)):
                listResult.append(i)
    return listResult

def main():
    print(f"Các số nguyên tố thoả mãn yêu cầu là: ", end="")
    print(findNumber())


if __name__ == "__main__":
    main()
