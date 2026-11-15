const DEM = Ref(0)

function fib_de_quy(n)
    DEM[] += 1
    if n <= 1 return n end
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)
end

function fib_ghi_nho(n, bo_nho=Dict{Int,Int}(0=>0, 1=>1))
    if haskey(bo_nho, n) return bo_nho[n] end
    bo_nho[n] = fib_ghi_nho(n - 1, bo_nho) + fib_ghi_nho(n - 2, bo_nho)
    return bo_nho[n]
end

function fib_lap(n)
    if n <= 1 return n end
    f0::Int64 = 0
    f1::Int64 = 1
    fn::Int64 = 0
    for i in 2:n
        if typemax(Int64) - f1 < f0
            return -1
        end
        fn = f0 + f1
        f0 = f1
        f1 = fn
    end
    return fn
end

function main()
    line = readline()
    isempty(line) && return
    n = parse(Int, line)
    
    if n <= 30
        DEM[] = 0
        f = fib_de_quy(n)
        println("F = $f, so loi goi = $(DEM[])")
    else
        f = fib_lap(n)
        if f == -1
            println("tran long long")
        else
            println("F = $f")
        end
    end
end

main()
