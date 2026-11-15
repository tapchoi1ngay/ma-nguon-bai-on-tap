def cai_tui(w, v, W):
    n = len(w)
    f = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            f[i][j] = f[i - 1][j]
            if w[i - 1] <= j:
                f[i][j] = max(f[i][j], f[i - 1][j - w[i - 1]] + v[i - 1])
                
    print("Bảng f:")
    for row in f:
        print(row)
        
    chon = []
    j = W
    for i in range(n, 0, -1):
        if f[i][j] != f[i - 1][j]:
            chon.append(i)
            j -= w[i - 1]
            
    return f[n][W], sorted(chon)

if __name__ == "__main__":
    w = [2, 3, 4, 5, 7]
    v = [3, 7, 9, 12, 16]
    W = 11
    max_val, chon = cai_tui(w, v, W)
    print(f"\nGiá trị lớn nhất: {max_val}")
    print(f"Tập đồ vật được chọn: {chon}")
