def two_pointers_sum(A, S):
    A.sort()
    L, R = 0, len(A) - 1
    while L < R:
        current_sum = A[L] + A[R]
        if current_sum == S:
            return (A[L], A[R])
        elif current_sum < S:
            L += 1
        else:
            R -= 1
    return None

A = [8, 3, 5, 1, 9, 2]
S = 8
result = two_pointers_sum(A, S)
print(f"Cap co tong bang {S} la: {result}")
