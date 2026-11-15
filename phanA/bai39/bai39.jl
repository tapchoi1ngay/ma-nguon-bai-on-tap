function cach1(a)
    isempty(a) && return 0
    max_sum = a[1]
    n = length(a)
    for i in 1:n
        for j in i:n
            s = 0
            for k in i:j
                s += a[k]
            end
            max_sum = max(max_sum, s)
        end
    end
    return max_sum
end

function cach2(a)
    isempty(a) && return 0
    max_sum = a[1]
    n = length(a)
    for i in 1:n
        s = 0
        for j in i:n
            s += a[j]
            max_sum = max(max_sum, s)
        end
    end
    return max_sum
end

function kadane(a)
    isempty(a) && return 0
    max_sum = a[1]
    current_sum = a[1]
    for i in 2:length(a)
        current_sum = max(a[i], current_sum + a[i])
        max_sum = max(max_sum, current_sum)
    end
    return max_sum
end

function main()
    line1 = readline()
    isempty(line1) && return
    
    line2 = readline()
    a = parse.(Int, split(line2))
    println(kadane(a))
end

main()
