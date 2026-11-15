import random
import time

def sinh_du_lieu(n, d):
    random.seed(12345)
    D = [{'x': [random.uniform(0, 10) for _ in range(d)], 'y': f"Lop{i%3}"} for i in range(n)]
    queries = [[random.uniform(0, 10) for _ in range(d)] for _ in range(1000)]
    return D, queries

def lang_gieng_gan_nhat(q, D):
    best_dist = float('inf')
    best_label = ""
    for mau in D:
        dist = sum((a - b)**2 for a, b in zip(q, mau['x']))
        if dist < best_dist:
            best_dist = dist
            best_label = mau['y']
    return best_label

def main():
    d = 20
    for n in [10**3, 10**4, 10**5]:
        D, queries = sinh_du_lieu(n, d)
        
        t0 = time.perf_counter()
        for q in queries:
            lang_gieng_gan_nhat(q, D)
        t = time.perf_counter() - t0
        
        print(f"n = {n} -> {t:.4f} giay")

if __name__ == '__main__':
    main()
