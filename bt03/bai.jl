function n_quan_hau(n)
    x = zeros(Int, n)
    cot = falses(n)
    cheo1 = falses(2n)
    cheo2 = falses(2n)
    so_loi_giai = 0
    so_nut = 0
    loi_giai_dau_tien = Int[]

    function dat(i)
        so_nut += 1
        if i > n
            so_loi_giai += 1
            if isempty(loi_giai_dau_tien)
                loi_giai_dau_tien = copy(x)
            end
            return
        end
        for j in 1:n
            if !cot[j] && !cheo1[i+j] && !cheo2[i-j+n]
                x[i] = j
                cot[j] = cheo1[i+j] = cheo2[i-j+n] = true
                dat(i+1)
                cot[j] = cheo1[i+j] = cheo2[i-j+n] = false
            end
        end
    end

    dat(1)
    return so_nut, so_loi_giai, loi_giai_dau_tien
end

println("N24DCDT090 LeVoDatThoi\n")

for n in [5, 6, 8]
    println("--- KẾT QUẢ CHO n = $n ---")
    nut, sol, board = n_quan_hau(n)
    println("Số nút đã duyệt: ", nut)
    println("Số lời giải: ", sol)
    if !isempty(board)
        println("Bàn cờ lời giải đầu tiên:")
        for i in 1:n
            for j in 1:n
                print(board[i] == j ? "Q " : ". ")
            end
            println()
        end
    end
    println()
end
