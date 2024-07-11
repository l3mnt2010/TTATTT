def main():
       n = int(input("Nhập N: "))
       found = False
       result = []
       for i in range(2, n + 1):
            divisors = 2
            for j in range(2, i):
              if i % j == 0:
                   divisors += 1
            if divisors == 4:
                   result.append(i)
                   found = True
       print(f"Tìm thấy {len(result)} số Q-prime nhỏ hơn hoặc bằng {n} là: \n {result}")
main()