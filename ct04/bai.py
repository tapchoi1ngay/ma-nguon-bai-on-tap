def solve_n_queens(n):
    # Khởi tạo mảng x với kích thước n+1 để dùng chỉ số từ 1 đến n
    x = [0] * (n + 1)
    nodes = 0
    sols = 0

    def safe(r, c):
        for i in range(1, r):
            if x[i] == c or abs(x[i] - c) == abs(i - r):
                return False
        return True

    def try_queen(i):
        nonlocal nodes, sols
        nodes += 1 # Đếm 1 nút mỗi khi gọi hàm đệ quy
        
        for j in range(1, n + 1):
            if safe(i, j):
                x[i] = j
                if i == n:
                    sols += 1
                    if sols == 1:
                        # In lời giải đầu tiên (bỏ phần tử 0 ở đầu mảng)
                        print("Loi giai 1:", x[1:])
                else:
                    try_queen(i + 1)

    try_queen(1)
    print(f"Nodes: {nodes}, Sols: {sols}")

n = int(input("Nhap n: "))
solve_n_queens(n)
