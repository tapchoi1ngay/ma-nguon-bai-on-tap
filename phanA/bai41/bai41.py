import sys

def tich_lon_nhat(a):
    if not a: return 0
    max_val = min_val = best = a[0]
    
    for i in range(1, len(a)):
        if a[i] < 0:
            max_val, min_val = min_val, max_val
            
        max_val = max(a[i], max_val * a[i])
        min_val = min(a[i], min_val * a[i])
        best = max(best, max_val)
        
    return best

def tich_lon_nhat_n2(a):
    if not a: return 0
    best = a[0]
    for i in range(len(a)):
        current = 1
        for j in range(i, len(a)):
            current *= a[j]
            best = max(best, current)
    return best

def main():
    line = sys.stdin.readline().strip()
    if not line: return
    
    a = list(map(int, sys.stdin.readline().split()))
    print(tich_lon_nhat(a))

if __name__ == '__main__':
    main()
