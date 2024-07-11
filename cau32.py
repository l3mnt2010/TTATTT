import random
import math

def miller_rabin(n, t):
    # Đầu vào: Một số nguyên lẻ 𝑛 ≥ 3 và tham số an toàn t ≥ 1
    if n < 2:
        return "hợp số"
    if n == 2 or n == 3:
        return "nguyên tố"
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    for i in range(t):
        a = random.randint(2, n - 2)
        y = pow(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = pow(y, 2, n)
                if y == 1:
                    return "hợp số"
                j += 1
            if y != n - 1:
                return "hợp số"
    return "nguyên tố"

# x^y mod z
def modular(x, y, z):
    result = 1
    x = x % z
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % z
        y = y // 2
        x = (x * x) % z
    return result

# random p_q
def generate_p_q():
    p = random.randint(101, 499)
    while not miller_rabin(p, 10) == "nguyên tố":
        p = random.randint(101, 499)
    q = random.randint(101, 499)
    while not miller_rabin(q, 10) == "nguyên tố":
        q = random.randint(101, 499)
    return p, q

# tính n và phi
def calculate_n_phi(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    return n, phi

def choose_e(phi):
    e = 0
    while True:
        e = random.randint(1, phi)
        if gcd(e, phi) == 1:
            break
    return e


def calculate_d(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = math.floor(v/u)
        r = v - q*u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p


def encrypt(m, e, n):
    c = modular(m, e, n)
    return c

def decrypt(c, d, n):
    m = modular(c, d, n)
    return m

def gcd(a, b):
    while a :
        a , b = b%a , a
    return b

def main():
    SBD = int(input("Nhập SBD: "))
    p, q = generate_p_q()
    n, phi = calculate_n_phi(p, q)
    e = choose_e(phi)
    d = calculate_d(e, phi)
    m = SBD + 123
    c = encrypt(m, e, n)
    decrypted_m = decrypt(c, d, n)

    print("p:", p)
    print("q:", q)
    print("n:", n)
    print("phi(n):", phi)
    print("e:", e)
    print("d:", d)
    print(f"Thông điệp gốc m = {SBD} + 123  = ", m)
    print("Bản mã:", c)
    print("Bản giải mã:", decrypted_m)

main()
