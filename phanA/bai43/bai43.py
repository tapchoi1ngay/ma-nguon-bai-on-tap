import sys

dem = 0

def fib_de_quy(n):
    global dem
    dem += 1
    if n <= 1: return n
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)

def fib_ghi_nho(n, bo_nho=None):
    if bo_nho is None: bo_nho = {0: 0, 1: 1}
    if n in bo_nho: return bo_nho[n]
    bo_nho[n] = fib_ghi_nho(n - 1, bo_nho) + fib_ghi_nho(n - 2, bo_nho)
    return bo_nho[n]

def fib_lap(n):
    if n <= 1: return n
    f0, f1 = 0, 1
    for _ in range(2, n + 1):
        f0, f1 = f1, f0 + f1
    return f1

def main():
    global dem
    line = sys.stdin.readline().strip()
    if not line: return
    n = int(line)
    
    if n <= 30:
        dem = 0
        f = fib_de_quy(n)
        print(f"F = {f}, so loi goi = {dem}")
    else:
        f = fib_lap(n)
        if n > 92:
            print("Python khong tran: F =", f)
        else:
            print(f"F = {f}")

if __name__ == '__main__':
    main()
