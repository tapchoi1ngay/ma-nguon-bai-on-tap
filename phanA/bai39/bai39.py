import sys
import random

def cach1(a):
    if not a: return 0
    max_sum = a[0]
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            max_sum = max(max_sum, sum(a[i:j+1]))
    return max_sum

def cach2(a):
    if not a: return 0
    max_sum = a[0]
    n = len(a)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

def kadane(a):
    if not a: return 0
    max_sum = current_sum = a[0]
    for x in a[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum

def kiem_thu_tu_dong(so_lan=1000):
    print(f"Dang kiem thu tu dong {so_lan} lan...")
    for _ in range(so_lan):
        n = random.randint(1, 50)
        a = [random.randint(-100, 100) for _ in range(n)]
        kq1 = cach2(a)
        kq2 = kadane(a)
        if kq1 != kq2:
            print("Phat hien loi!")
            return False
    print("Kiem thu thanh cong!")
    return True

def main():
    # kiem_thu_tu_dong(1000)
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)
    a = list(map(int, sys.stdin.readline().split()))
    print(kadane(a))

if __name__ == '__main__':
    main()
