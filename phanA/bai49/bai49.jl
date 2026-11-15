function bo_mot_mau(D; kc)
    so_dung = 0
    tong_so = length(D)
    
    for i in 1:tong_so
        best_dist = Inf
        best_label = ""
        
        for j in 1:tong_so
            if i == j 
                continue # Bo qua chinh no
            end
            
            dist = kc(D[i].x, D[j].x)
            if dist < best_dist
                best_dist = dist
                best_label = D[j].y
            end
        end
        
        if best_label == D[i].y
            so_dung += 1
        end
    end
    
    return (so_dung, tong_so)
end

function main()
end

main()
