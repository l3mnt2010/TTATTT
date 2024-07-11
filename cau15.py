# sàng số ngto
def sieveOfEratosthenes(n):
    primes = []
    check = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(2, n + 1):
        if check[p]:
            primes.append(p)
    return primes


def find_Than_Thiet_Prime(n):
    listRes = []
    primes = sieveOfEratosthenes(n)
    for i in range(len(primes)):
        if primes[i] - primes[i - 1] == 2:
            listTmp = [primes[i - 1], primes[i]]
            listRes.append(listTmp)
    return listRes


def main():
    while True :
        try :
            n = int(input("Nhập N: "))
        except :
            print("Bạn cần phải nhập N có kiểu dữ liệu là interger")
            continue
        try :
            assert n > 0
            break
        except :
            print("N phải lớn hơn 0")
    listRes = find_Than_Thiet_Prime(n)
    if len(listRes) != 0:
        print(f"Các cặp số nguyên tố thoả mãn yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây cặp số nguyên tố thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
