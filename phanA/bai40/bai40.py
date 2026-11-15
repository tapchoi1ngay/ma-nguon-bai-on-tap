import sys
input = sys.stdin.readline

def kadane_chi_so(a):
    if not a: return (0, 0, 0)
    max_sum = current_sum = a[0]
    best_start = best_end = current_start = 0
    
    for i in range(1, len(a)):
        if a[i] > current_sum + a[i]:
            current_sum = a[i]
            current_start = i
        else:
            current_sum += a[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = current_start
            best_end = i
            
    return (max_sum, best_start + 1, best_end + 1)

def main():
    line1 = input().strip()
    if not line1: return
    
    a = list(map(int, input().split()))
    tong, dau, cuoi = kadane_chi_so(a)
    print(f"tong {tong}, doan [{dau}..{cuoi}]")

main()
