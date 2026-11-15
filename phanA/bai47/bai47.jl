struct Mau
    x::Vector{Float64}
    y::String
end

function doc_du_lieu(ten_tep)
    if !isfile(ten_tep)
        return (Mau[], 0)
    end
    
    tokens = split(read(ten_tep, String))
    isempty(tokens) && return (Mau[], 0)
    
    n = parse(Int, tokens[1])
    d = parse(Int, tokens[2])
    idx = 3
    D = Mau[]
    
    for _ in 1:n
        x = parse.(Float64, tokens[idx:idx+d-1])
        idx += d
        y = tokens[idx]
        idx += 1
        push!(D, Mau(x, y))
    end
    return (D, d)
end

function lang_gieng_gan_nhat(q, D)
    best_dist = Inf
    best_label = ""
    best_idx = -1
    for i in 1:length(D)
        dist = sqrt(sum((q .- D[i].x) .^ 2))
        if dist < best_dist
            best_dist = dist
            best_label = D[i].y
            best_idx = i
        end
    end
    return (best_label, best_dist, best_idx)
end

function main()
    D, d = doc_du_lieu("dataset.txt")
    isempty(D) && return
    
    queries = [
        [4.9, 3.3, 1.5, 0.2], 
        [6.1, 2.8, 4.7, 1.2],
        [6.5, 3.0, 5.5, 2.0], 
        [5.9, 3.0, 4.8, 1.8], 
        [6.0, 2.7, 5.1, 1.6]
    ]
    
    using Printf
    for q in queries
        nhan, kc, chi_so = lang_gieng_gan_nhat(q, D)
        @printf("%s -- mau %d, khoang cach %.4f\n", nhan, chi_so, kc)
    end
end

main()
