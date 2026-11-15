import sys
input = sys.stdin.readline

def da_sap_xep(a, nghiem_ngat=False) -> bool:
    for i in range(1, len(a)):
        if nghiem_ngat:
            if a[i] <= a[i - 1]:
                return False
        else:
            if a[i] < a[i - 1]:
                return False
    return True

def main():
    line1 = input().strip()
    if not line1:
        return
    n = int(line1)
    
    a = []
    if n > 0:
        a = list(map(int, input().split()))
        
    nn = "YES" if da_sap_xep(a, nghiem_ngat=True) else "NO"
    kg = "YES" if da_sap_xep(a, nghiem_ngat=False) else "NO"
    print(f"nghiem ngat: {nn} -- khong giam: {kg}")

main()
