function da_sap_xep(a; nghiem_ngat=false)
    for i in 2:length(a)
        if nghiem_ngat
            if a[i] <= a[i - 1]
                return false
            end
        else
            if a[i] < a[i - 1]
                return false
            end
        end
    end
    return true
end

function main()
    line1 = readline()
    if isempty(line1) return end
    
    line2 = readline()
    a = isempty(line2) ? Int[] : parse.(Int, split(line2))
    
    nn = da_sap_xep(a, nghiem_ngat=true) ? "YES" : "NO"
    kg = da_sap_xep(a, nghiem_ngat=false) ? "YES" : "NO"
    println("nghiem ngat: $nn -- khong giam: $kg")
end

main()
