using Printf

function main()
    line1 = readline()
    if isempty(line1) return end
    n = parse(Int, line1)
    
    a = parse.(Int, split(readline()))
    
    tong = 0
    nho_nhat = a[1]
    lon_nhat = a[1]
    
    for x in a
        tong += x
        if x < nho_nhat
            nho_nhat = x
        end
        if x > lon_nhat
            lon_nhat = x
        end
    end
    
    trung_binh = tong / n
    
    @printf("%d %.4f %d %d\n", tong, trung_binh, nho_nhat, lon_nhat)
end

main()
