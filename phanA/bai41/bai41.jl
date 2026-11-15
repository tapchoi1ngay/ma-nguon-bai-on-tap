function tich_lon_nhat(a)
    isempty(a) && return 0
    max_val = min_val = best = a[1]
    
    for i in 2:length(a)
        if a[i] < 0
            temp = max_val
            max_val = min_val
            min_val = temp
        end
        
        max_val = max(a[i], max_val * a[i])
        min_val = min(a[i], min_val * a[i])
        best = max(best, max_val)
    end
    return best
end

function main()
    line1 = readline()
    isempty(line1) && return
    
    line2 = readline()
    a = parse.(Int, split(line2))
    println(tich_lon_nhat(a))
end

main()
