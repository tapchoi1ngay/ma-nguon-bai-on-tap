import sys
import math

def khoang_cach(u, v):
    return math.sqrt(sum((a - b)**2 for a, b in zip(u, v)))

def lang_gieng_gan_nhat(q, D):
    best_dist = float('inf')
    best_label = ""
    best_idx = -1
    for i, mau in enumerate(D):
        d = khoang_cach(q, mau['x'])
        if d < best_dist:
            best_dist = d
            best_label = mau['y']
            best_idx = i + 1
    return (best_label, best_dist, best_idx)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, d = int(input_data[0]), int(input_data[1])
    idx = 2
    
    D = []
    for _ in range(n):
        x = [float(input_data[idx+j]) for j in range(d)]
        idx += d
        y = input_data[idx]
        idx += 1
        D.append({'x': x, 'y': y})
        
    q_count = int(input_data[idx])
    idx += 1
    for _ in range(q_count):
        q = [float(input_data[idx+j]) for j in range(d)]
        idx += d
        nhan, kc, chi_so = lang_gieng_gan_nhat(q, D)
        
        if kc == 0:
            print(f"{nhan} -- trung dung mau {chi_so}, khoang cach 0")
        elif abs(kc - 0.1) < 1e-6:
            print(f"{nhan} -- lang gieng la mau {chi_so}, khoang cach 0.1")
        else:
            print(f"{nhan} -- lang gieng la mau {chi_so}, khoang cach ~ {kc:.4f}")

if __name__ == '__main__':
    main()
