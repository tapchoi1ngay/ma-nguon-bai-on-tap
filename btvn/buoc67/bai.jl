function cai_tui(w, v, W)
    n = length(w)
    f = zeros(Int, n + 1, W + 1)
    
    for i in 1:n
        for j in 0:W
            f[i+1, j+1] = f[i, j+1]
            if w[i] <= j
                f[i+1, j+1] = max(f[i+1, j+1], f[i, j-w[i]+1] + v[i])
            end
        end
    end
    
    println("Bảng f:")
    for r in 1:n+1
        for c in 1:W+1
            print(f[r, c], "\t")
        end
        println()
    end
    
    chon = Int[]
    j = W
    for i in n:-1:1
        if f[i+1, j+1] != f[i, j+1]
            push!(chon, i)
            j -= w[i]
        end
    end
    
    return f[n+1, W+1], sort(chon)
end

w = [2, 3, 4, 5, 7]
v = [3, 7, 9, 12, 16]
W = 11
max_val, chon = cai_tui(w, v, W)
println("\nGiá trị lớn nhất: ", max_val)
println("Tập đồ vật được chọn: ", chon)
