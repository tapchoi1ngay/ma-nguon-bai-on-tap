import sys
import time

def thuat_toan_On2(n):
    tong = 0
    for i in range(n):
        for j in range(n):
            tong += i * j
    return tong

def do_thoi_gian(n, lap=3):
    min_time = float('inf')
    for _ in range(lap):
        t0 = time.perf_counter()
        thuat_toan_On2(n)
        t1 = time.perf_counter()
        min_time = min(min_time, t1 - t0)
    return min_time

def main():
    line = sys.stdin.readline().strip()
    if not line: return
    n = int(line)
    
    thoi_gian = do_thoi_gian(n)
    print(f"{thoi_gian:.6f}")

if __name__ == '__main__':
    main()
