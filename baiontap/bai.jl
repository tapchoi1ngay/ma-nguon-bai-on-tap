function tao_ke(n::Integer, canh::Vector{Tuple{Int,Int}})
    if !(1 <= n <= 100)
        throw(ArgumentError("So dinh n phai trong khoang từ 1 den 100."))
    end
    ke = [Vector{Int}() for _ in 1:n]
    for (u, v) in canh
        if !(1 <= u <= n) || !(1 <= v <= n) || u == v
            throw(ArgumentError("Canh khuyen hoac dinh vuot quá phạm vi cho phep."))
        end
        push!(ke[u], v)
        push!(ke[v], u)
    end
    for i in 1:n
        unique!(ke[i])
        sort!(ke[i])
    end
    return ke
end

function bfs_chia_lop(n::Integer, canh::Vector{Tuple{Int,Int}}, s::Integer)
    ke = tao_ke(n, canh)
    if !(1 <= s <= n)
        throw(ArgumentError("Dinh nguon s khong hop le."))
    end
    
    d = fill(-1, n)
    d[s] = 0
    hang = Int[]
    push!(hang, s)
    dau = 1
    
    while dau <= length(hang)
        u = hang[dau]
        dau += 1
        for v in ke[u]
            if d[v] == -1
                d[v] = d[u] + 1
                push!(hang, v)
            end
        end
    end
    return d
end
