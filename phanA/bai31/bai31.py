import sys
input = sys.stdin.readline

def main():
    n_str = input().strip()
    if not n_str:
        return
    n = int(n_str)
    
    a = list(map(int, input().split()))
    
    tong = 0
    nho_nhat = a[0]
    lon_nhat = a[0]
    
    for x in a:
        tong += x
        if x < nho_nhat: nho_nhat = x
        if x > lon_nhat: lon_nhat = x
            
    trung_binh = tong / n
    
    print(f"{tong} {trung_binh:.4f} {nho_nhat} {lon_nhat}")

main()
