
# tìm số mạnh mẽ
def find_strong_number(n):
    # gán mảng bằng full 0 có độ dài là n
    result = [0]*n
    
    # duyệt từ 4 đến n-1 với bước nhảy 1 đầu tiên gắn mảng lại là 0
    for i in range(4, n):
        result[i] = 0
        # duyệt từ 2 đến i với bước nhảy là 1 -> khởi tạo biến flag là 0 sau đó 
        for j in range(2, i):
            flag = 0
            for k in range(2, j): # kiểm tra xem nếu j có ước nào lớn hơn 2 và nhỏ hơn j-1 không nếu có thì flag = 1
                if j % k == 0:
                    flag = 1
            if flag != 1 and result[i] == 0:  # j là số nguyên tố vì có ước khác 1 và chính nó
                if i % (j*j) == 0:
                    result[i] = 1
    result2 = []
    for i in range(4, n):
        if result[i] == 1:
             result2.append(i)
    return result2


def main():
    n = int(input("Nhập n: "))
    result = find_strong_number(n)
    print(f"Các số mạnh mẽ nhỏ hơn {n} là: ")
    print(result)
    print(f"Tìm thấy {len(result)} số")

if __name__ == "__main__":
    main()