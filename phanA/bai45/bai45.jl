function luy_thua_mod(a::Int, b::Int, m::Int)
    r = 1 % m
    a = a % m
    while b > 0
        if b % 2 == 1
            r = (r * a) % m
        end
        a = (a * a) % m
        b = div(b, 2)
    end
    return r
end

function main()
    line = readline()
    isempty(line) && return
    parts = parse.(Int, split(line))
    a, b, m = parts[1], parts[2], parts[3]
    println(luy_thua_mod(a, b, m))
end

main()
