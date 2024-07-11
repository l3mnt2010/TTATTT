n = int(input("Nhập N: "))

divisors = []
for i in range(1, n + 1):
  if n % i == 0:
    divisors.append(i)


prime_divisors = []
for i in divisors:
  is_prime = True
  if i == 1:
    is_prime = False
  else:
    for j in range(2, i):
      if i % j == 0:
        is_prime = False
        break
  if is_prime:
    prime_divisors.append(i)

print(f"Số ước của {n} là {len(divisors)}")
print(f"Số ước nguyên tố của {n} là {len(prime_divisors)}")
