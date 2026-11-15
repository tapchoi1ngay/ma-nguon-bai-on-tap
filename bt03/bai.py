def n_quan_hau(n):
    x = [0] * (n + 1)
    cot = [False] * (n + 1)
    cheo1 = [False] * (2 * n + 1)
    cheo2 = [False] * (2 * n + 1)
    so_loi_giai = 0
    so_nut = 0
    loi_giai_dau_tien = None

    def dat(i):
        nonlocal so_loi_giai, so_nut, loi_giai_dau_tien
        so_nut += 1
        if i > n:
            so_loi_giai += 1
            if loi_giai_dau_tien is None:
                loi_giai_dau_tien = x[1:].copy()
            return
        
        for j in range(1, n + 1):
            if not cot[j] and not cheo1[i + j] and not cheo2[i - j + n]:
                x[i] = j
                cot[j] = cheo1[i + j] = cheo2[i - j + n] = True
                dat(i + 1)
                cot[j] = cheo1[i + j] = cheo2[i - j + n] = False

    dat(1)
    return so_nut, so_loi_giai, loi_giai_dau_tien

if __name__ == "__main__":
    print("N24DCDT090 LeVoDatThoi\n")
    
    for n in [5, 6, 8]:
        print(f"--- KẾT QUẢ CHO n = {n} ---")
        nut, sol, board = n_quan_hau(n)
        print(f"Số nút đã duyệt: {nut}")
        print(f"Số lời giải: {sol}")
        if board:
            print("Bàn cờ lời giải đầu tiên:")
            for i in range(n):
                row = ['.'] * n
                row[board[i] - 1] = 'Q'
                print(" ".join(row))
        print("\n")
