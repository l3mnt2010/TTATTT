
def Uoc(n):
   uoc = [False] * (n+1)
   for i in range(1,n):
      if n % i == 0:
         uoc[i] = True
   return [i for i in range(1,n) if uoc[i] == True] 

n  = int(input("Nhập N: "))
check = []

print("các cặp số thân thiết nhỏ hơn", n, "là: ")
for i in range(n+1):
   sum1 = sum(Uoc(i))
   j = sum1
   sum2 = sum(Uoc(j))
   if (i != j and i==sum2):
      if [i, j] and [j, i] not in check:
        print(i, "va", j)
        check.append([i, j])
