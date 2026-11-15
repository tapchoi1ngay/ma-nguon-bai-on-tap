import math

def doc_du_lieu(ten_tep):
    D = []
    d = 0
    try:
        with open(ten_tep, 'r') as f:
            lines = f.read().split()
            if not lines: 
                return D, d
            n, d = int(lines[0]), int(lines[1])
            idx = 2
            for _ in range(n):
                x = [float(lines[idx+j]) for j in range(d)]
                idx += d
                y = lines[idx]
                idx += 1
                D.append({'x': x, 'y': y})
    except FileNotFoundError:
        pass
    return D, d

def lang_gieng_gan_nhat(q, D):
    best_dist = float('inf')
    best_label = ""
    best_idx = -1
    for i, mau in enumerate(D):
        dist = math.sqrt(sum((a - b)**2 for a, b in zip(q, mau['x'])))
        if dist < best_dist:
            best_dist = dist
            best_label = mau['y']
            best_idx = i + 1
    return best_label, best_dist, best_idx

def main():
    D, d = doc_du_lieu("dataset.txt")
    if not D: return
    
    queries = [
        [4.9, 3.3, 1.5, 0.2], 
        [6.1, 2.8, 4.7, 1.2],
        [6.5, 3.0, 5.5, 2.0], 
        [5.9, 3.0, 4.8, 1.8], 
        [6.0, 2.7, 5.1, 1.6]
    ]
    
    for q in queries:
        nhan, kc, chi_so = lang_gieng_gan_nhat(q, D)
        print(f"{nhan} -- mau {chi_so}, khoang cach {kc:.4f}")

if __name__ == '__main__':
    main()
