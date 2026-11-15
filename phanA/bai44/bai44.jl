function thuat_toan_On2(n)
    tong = 0
    for i in 1:n
        for j in 1:n
            tong += i * j
        end
    end
    return tong
end

function main()
    line = readline()
    isempty(line) && return
    n = parse(Int, line)
    
    # Goi mot lan de bien dich truoc (JIT warm-up)
    thuat_toan_On2(10) 
    
    min_time = Inf
    for _ in 1:3
        t = @elapsed thuat_toan_On2(n)
        min_time = min(min_time, t)
    end
    
    using Printf
    @printf("%.6f\n", min_time)
end

main()
