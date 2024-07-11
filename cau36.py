def boyer_moore(S1, S2):
    table = {}
    # Duyệt ngược mảng S1 từ chiều dài của chuỗi đến 0 và nếu mà chuỗi đó lặp lại thì không thêm vào trong tables shift
    for i in range(len(S1) - 1, -1, -1):
        if S1[i] not in table:
            table[S1[i]] = i
    
    i = 0
    # kiểm tra nếu mà chuỗi S2 lớn hơn chuỗi S1 và duyệt i nếu nhỏ hơn phần lớn hơn đó
    while i <= len(S2) - len(S1):
        # gán j bằng chiều dài chuỗi S1 - 1
        j = len(S1) - 1
        # lặp tìm xem có phần tử thứ i nào của S1 giống với phần tử i + j của S2 và j-- có nghĩa là khớp xem chuỗi S
        while j >= 0 and S1[j] == S2[i + j]:    
           j -= 1
        if j == -1:
            return i, table
        else:
            # Dịch chuyển chỉ mục tìm kiếm theo mức tối đa của dịch chuyển ký tự xấu và dịch chuyển hậu tố tốt
            shift = max(j - table.get(S2[i + j], -1), 1)
            i += shift
    
    # Không tìm thấy S1 trong S2
    return -1, table

def main():
  S1 = input("Nhập chuỗi ban đầu: ")
  S2 = input("Nhập chuỗi kiểm tra: ")
    
  result, table = boyer_moore(S2, S1)
  print(table)
  if result == -1:
        print(f"Không tìm thấy chuỗi '{S2}' trong '{S1}'")
  else:
    print(f"Tìm thấy chuỗi {S2} tại vị trí: {result}")

main()


# boyer-moore thực hiện tốt nếu bảng chữ cái lớn, chậm khi bảng chữ cái nhỏ
# tốt cho văn bản thông thường, kém với nhị phân
# boyer-moore có độ phức tạp xấu nhất là O(n) tìm mẫu dài n trong văn bản dài m, vét cạn O(nm)