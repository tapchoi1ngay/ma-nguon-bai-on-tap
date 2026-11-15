import sys

def cua_so_truot(a, k):
    if not a or k <= 0 or k > len(a):
        return (0, 0)
        
    current_sum = sum(a[:k])
    max_sum = current_sum
    best_start = 1
    
    for i in range(k, len(a)):
        current_sum = current_sum + a[i] - a[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - k + 2
            
    return (max_sum, best_start)

def main():
    line1 = sys.stdin.readline().strip()
    if not line1: return
    
    n, k = map(int, line1.split())
    a = list(map(int, sys.stdin.readline().split()))
    
    tong, vi_tri = cua_so_truot(a, k)
    print(f"tong {tong}, bat dau tai vi tri {vi_tri}")

if __name__ == '__main__':
    main()
