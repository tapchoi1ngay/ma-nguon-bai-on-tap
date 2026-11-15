import sys

def la_nguyen_to(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def sang(n: int) -> list:
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
        
    return [k for k in range(2, n + 1) if is_prime[k]]

def main():
    line = sys.stdin.readline().strip()
    if not line: return
    n = int(line)
    
    primes = sang(n)
    
    if n <= 30:
        print(" ".join(map(str, primes)) + f"  ({len(primes)} so)")
    elif n < 1000000:
        print(f"so luong = {len(primes)}")
    else:
        tong = sum(primes)
        print(f"so luong = {len(primes)}, tong = {tong}")

if __name__ == '__main__':
    main()
