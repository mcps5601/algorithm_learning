def insertion_sort(A):
    for j in range(1, len(A)):
        right_index = j
        
        while right_index > 0 and A[right_index - 1] > A[right_index]:
            A[right_index], A[right_index - 1] = A[right_index - 1], A[right_index]
            right_index -= 1

    return A
