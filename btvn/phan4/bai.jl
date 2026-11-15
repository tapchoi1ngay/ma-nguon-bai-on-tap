function two_pointers_sum(A, S)
    sort!(A)
    L, R = 1, length(A)
    while L < R
        current_sum = A[L] + A[R]
        if current_sum == S
            return (A[L], A[R])
        elseif current_sum < S
            L += 1
        else
            R -= 1
        end
    end
    return nothing
end

A = [8, 3, 5, 1, 9, 2]
S = 8
result = two_pointers_sum(A, S)
println("Cap co tong bang $S la: $result")
