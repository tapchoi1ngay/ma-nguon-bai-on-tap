kc_euclid(u, v) = sqrt(sum((u .- v) .^ 2))
kc_manhattan(u, v) = sum(abs.(u .- v))

function lang_gieng_gan_nhat(q, D; kc = kc_euclid)
    best_dist = Inf
    best_idx = -1
    for i in 1:length(D)
        dist = kc(q, D[i].x)
        if dist < best_dist
            best_dist = dist
            best_idx = i
        end
    end
    return best_idx
end

function main()
end

main()
