def kmp_search(pattern, text):
  prefix_table = compute_prefix_table(pattern)

  m = len(pattern)
  n = len(text)
  i = 0
  j = 0

  while i < n:
    if pattern[j] == text[i]:
      j += 1
      i += 1
      
      if j == m:
        return (i-j), prefix_table

    else:
      if j > 0:
        j = prefix_table[j - 1]
      else:
        i += 1
  return -1, prefix_table

def compute_prefix_table(pattern):
  m = len(pattern)
  prefix_table = [0] * m

  j = 0
  i = 1

  while i < m:
    if pattern[i] == pattern[j]:
      prefix_table[i] = j + 1
      i += 1
      j += 1

    else:
      if j > 0:
        j = prefix_table[j - 1]
      else:
        prefix_table[i] = 0
        i += 1

  return prefix_table

def main():
    
  S1 = input("Nhập chuỗi ban đầu: ")
  S2 = input("Nhập chuỗi kiểm tra: ")
    
  result, prefix_function = kmp_search(S2, S1)
  
  prefix_function2 = prefix_function
  prefix_function2.insert(0, -1)
  del prefix_function2[-1]
  print(prefix_function)
  
  if result == -1:
        print(f"Không tìm thấy chuỗi '{S2}' trong '{S1}'")
  else:
    print(f"Tìm thấy chuỗi \"{S2}\" tại vị trí: {result}")

main()
