function insertion_sort!(A)
    n = length(A)
    for i in 2:n
        x = A[i]
        j = i - 1
        while j > 0 && A[j] > x
            A[j+1] = A[j]
            j -= 1
        end
        A[j+1] = x
    end
    return A
end

A = [8, 3, 5, 1, 9, 2]
println(insertion_sort!(A))
