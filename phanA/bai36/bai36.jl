function giai_thua(n::Int)
    try
        # Thử tính giai thừa bằng số nguyên chuẩn 64-bit
        kq = factorial(n)
        println(kq)
    catch e
        # Bắt lỗi chủ động nếu bị tràn
        if isa(e, OverflowError)
            kq_big = factorial(big(n))
            max_int = typemax(Int)
            println("TRAN SO ($n! = $kq_big > $max_int)")
        end
    end
end

function main()
    line = readline()
    if isempty(line) return end
    n = parse(Int, line)
    giai_thua(n)
end

main()
