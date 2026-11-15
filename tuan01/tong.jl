function main()
    tokens = split(read(stdin, String))
    if isempty(tokens)
        return
    end
    n = parse(Int, tokens[1])
    a = [parse(Int64, tokens[i+1]) for i in 1:n]
    println("$(sum(a)) $(maximum(a))")
end

main()
