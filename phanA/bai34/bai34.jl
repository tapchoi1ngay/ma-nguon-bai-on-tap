function dao_nguoc(n::Int)
    rev::Int = 0
    abs_n = abs(n)
    
    while abs_n > 0
        rev = rev * 10 + (abs_n % 10)
        abs_n = div(abs_n, 10)
    end
    
    if n < 0
        return -rev
    else
        return rev
    end
end

function main()
    line = readline()
    if isempty(line) return end
    n = parse(Int, line)
    println(dao_nguoc(n))
end

main()
