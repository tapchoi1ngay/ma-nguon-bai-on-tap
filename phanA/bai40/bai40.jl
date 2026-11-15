function kadane_chi_so(a)
    isempty(a) && return (0, 0, 0)
    max_sum = current_sum = a[1]
    best_start = best_end = current_start = 1
    
    for i in 2:length(a)
        if a[i] > current_sum + a[i]
            current_sum = a[i]
            current_start = i
        else
            current_sum += a[i]
        end
        
        if current_sum > max_sum
            max_sum = current_sum
            best_start = current_start
            best_end = i
        end
    end
    return (max_sum, best_start, best_end)
end

function main()
    line1 = readline()
    isempty(line1) && return
    
    line2 = readline()
    a = parse.(Int, split(line2))
    tong, dau, cuoi = kadane_chi_so(a)
    println("tong $tong, doan [$dau..$cuoi]")
end

main()
