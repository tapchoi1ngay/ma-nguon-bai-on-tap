import sys
input = sys.stdin.readline

def phan_tich(n: int):
    so_chu_so = 0
    tong_chu_so = 0
    while n > 0:
        tong_chu_so += n % 10
        so_chu_so += 1
        n //= 10
    return (so_chu_so, tong_chu_so)

def main():
    line = input().strip()
    if not line:
        return
    n = int(line)
    so, tong = phan_tich(n)
    print(f"{so} {tong}")

main()
