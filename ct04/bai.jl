function solve_n_queens(n)
    # Julia mặc định đánh chỉ số từ 1
    x = zeros(Int, n)
    nodes = 0
    sols = 0

    function safe(r, c)
        for i in 1:(r-1)
            if x[i] == c || abs(x[i] - c) == abs(i - r)
                return false
            end
        end
        return true
    end

    function try_queen(i)
        nodes += 1 # Đếm 1 nút mỗi khi gọi hàm đệ quy
        
        for j in 1:n
            if safe(i, j)
                x[i] = j
                if i == n
                    sols += 1
                    if sols == 1
                        println("Loi giai 1: ", x)
                    end
                else
                    try_queen(i + 1)
                end
            end
        end
    end

    try_queen(1)
    println("Nodes: $nodes, Sols: $sols")
end

print("Nhap n: ")
n = parse(Int, readline())
solve_n_queens(n)
