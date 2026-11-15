function cua_so_truot(a, k)
    (isempty(a) || k <= 0 || k > length(a)) && return (0, 0)
    
    current_sum = sum(a[1:k])
    max_sum = current_sum
    best_start = 1
    
    for i in (k + 1):length(a)
        current_sum = current_sum + a[i] - a[i - k]
        if current_sum > max_sum
            max_sum = current_sum
            best_start = i - k + 1
        end
    end
    return (max_sum, best_start)
end

function main()
    line1 = readline()
    isempty(line1) && return
    
    parts = parse.(Int, split(line1))
    n, k = parts[1], parts[2]
    
    line2 = readline()
    a = parse.(Int, split(line2))
    
    tong, vi_tri = cua_so_truot(a, k)
    println("tong $tong, bat dau tai vi tri $vi_tri")
end

main()
