function la_nguyen_to(n::Int)
    if n < 2
        return false
    end
    i = 2
    while i * i <= n
        if n % i == 0
            return false
        end
        i += 1
    end
    return true
end

function sang(n::Int)
    is_prime = trues(n + 1)
    if n >= 0 is_prime[1] = false end 
    if n >= 1 is_prime[2] = false end 
    
    i = 2
    while i * i <= n
        if is_prime[i + 1]
            for j in (i * i):i:n
                is_prime[j + 1] = false
            end
        end
        i += 1
    end
    
    primes = Int[]
    for k in 2:n
        if is_prime[k + 1]
            push!(primes, k)
        end
    end
    return primes
end

function main()
    line = readline()
    if isempty(line) return end
    n = parse(Int, line)
    
    primes = sang(n)
    
    if n <= 30
        print(join(primes, " "))
        println("  ($(length(primes)) so)")
    elseif n < 1000000
        println("so luong = $(length(primes))")
    else
        tong = sum(primes)
        println("so luong = $(length(primes)), tong = $tong")
    end
end

main()
