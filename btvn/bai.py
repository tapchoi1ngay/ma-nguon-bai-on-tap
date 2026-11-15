def insertion_sort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = x
    return A

A = [8, 3, 5, 1, 9, 2]
print("Mảng trước khi sắp xếp:", A)
print("Mảng sau khi sắp xếp:", insertion_sort(A))
