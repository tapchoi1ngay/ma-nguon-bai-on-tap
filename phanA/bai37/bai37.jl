function dem(a)
    chan = 0
    le = 0
    am = 0
    for x in a
        if x < 0
            am += 1
        end
        
        if x % 2 == 0
            chan += 1
        else
            le += 1
        end
    end
    return (chan, le, am)
end

function main()
    line1 = readline()
    if isempty(line1) return end
    
    line2 = readline()
    a = parse.(Int, split(line2))
    
    chan, le, am = dem(a)
    println("chan $chan, le $le, am $am")
end

main()
