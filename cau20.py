def gcd(a, b):
    while a :
        a , b = b % a , a
    return b

def findAB(m, n, d):
    listRes = []
    for i in range(m + 1, n):
        for j in range(i + 1, n):
            if gcd(i, j) == d:
                listTmp = [i, j]
                listRes.append(listTmp)
    return listRes

def main():
    while True:
        try :
            m = int(input("Nhập M: "))
            n = int(input("Nhập N: "))
            d = int(input("Nhập d: "))
        except :
            print("M, N và D phải là integer")
            continue
        try :
            assert 0 < m < n < 1000 and d < 1000 
            break
        except :
            print("0 < m < n and d < 1000")
            continue
        
    
    listRes = findAB(n, m, d)
    if len(listRes) != 0:
        print(f"Các cặp số nguyên thoả mãn yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây cặp số nguyên thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
