using Random

struct Mau
    x::Vector{Float64}
    y::String
end

function sinh_du_lieu(n, d)
    Random.seed!(12345)
    D = [Mau(rand(d) .* 10, "Lop$(i%3)") for i in 1:n]
    queries = [rand(d) .* 10 for _ in 1:1000]
    return D, queries
end

function lang_gieng_gan_nhat(q, D)
    best_dist = Inf
    best_label = ""
    for i in 1:length(D)
        dist = sum((q .- D[i].x) .^ 2)
        if dist < best_dist
            best_dist = dist
            best_label = D[i].y
        end
    end
    return best_label
end

function main()
    d = 20
    # JIT warm-up
    D_warm, queries_warm = sinh_du_lieu(10, d)
    lang_gieng_gan_nhat(queries_warm[1], D_warm)
    
    for n in [10^3, 10^4, 10^5]
        D, queries = sinh_du_lieu(n, d)
        
        t = @elapsed begin
            for q in queries
                lang_gieng_gan_nhat(q, D)
            end
        end
        
        using Printf
        @printf("n = %d -> %.4f giay\n", n, t)
    end
end

main()
