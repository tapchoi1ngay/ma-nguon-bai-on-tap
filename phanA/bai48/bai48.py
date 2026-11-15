import math

def kc_euclid(u, v):
    return math.sqrt(sum((a - b)**2 for a, b in zip(u, v)))

def kc_manhattan(u, v):
    return sum(abs(a - b) for a, b in zip(u, v))

def lang_gieng_gan_nhat(q, D, kc=kc_euclid):
    best_dist = float('inf')
    best_idx = -1
    for i, mau in enumerate(D):
        dist = kc(q, mau['x'])
        if dist < best_dist:
            best_dist = dist
            best_idx = i + 1
    return best_idx

def main():
    pass

if __name__ == '__main__':
    main()
