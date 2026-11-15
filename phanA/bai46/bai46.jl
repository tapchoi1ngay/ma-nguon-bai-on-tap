using Printf

khoang_cach(u, v) = sqrt(sum((u .- v) .^ 2))

struct Mau
    x::Vector{Float64}
    y::String
end

function lang_gieng_gan_nhat(q, D)
    best_dist = Inf
    best_label = ""
    best_idx = -1
    for i in 1:length(D)
        d = khoang_cach(q, D[i].x)
        if d < best_dist
            best_dist = d
            best_label = D[i].y
            best_idx = i
        end
    end
    return (best_label, best_dist, best_idx)
end

function main()
    tokens = split(read(stdin, String))
    isempty(tokens) && return
    
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
    
    q_count = parse(Int, tokens[idx])
    idx += 1
    for _ in 1:q_count
        q = parse.(Float64, tokens[idx:idx+d-1])
        idx += d
        nhan, kc, chi_so = lang_gieng_gan_nhat(q, D)
        
        if kc == 0
            println("$nhan -- trung dung mau $chi_so, khoang cach 0")
        elseif abs(kc - 0.1) < 1e-6
            println("$nhan -- lang gieng la mau $chi_so, khoang cach 0.1")
        else
            @printf("%s -- lang gieng la mau %d, khoang cach ~ %.4f\n", nhan, chi_so, kc)
        end
    end
end

main()
