import sys
import math
input = sys.stdin.readline

def giai_thua(n: int) -> int:
    # Python số nguyên mở rộng vô hạn nên dùng luôn thư viện chuẩn
    return math.factorial(n)

def main():
    line = input().strip()
    if not line:
        return
    n = int(line)
    # In trực tiếp vì Python không bao giờ bị tràn số
    print(giai_thua(n))

main()
