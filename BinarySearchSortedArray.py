def rotated_binary_search(A, N, key): 
    L = 0
    R = N - 1
    while (L <= R): 
        M = L + ((R - L) / 2)
        if (A[M] == key): return M
 
    # the bottom half is sorted
        if (A[L] <= A[M]):
            if (A[L] <= key and key < A[M]):
                R = M - 1
            else:
                L = M + 1
   
    # the upper half is sorted
        else: 
            if (A[M] < key and key <= A[R]):
                L = M + 1
            else:
                R = M - 1
    
  
    return -1

A = [6, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5]
N = len(A)
result = rotated_binary_search(A, N, 13)
print "Original List", A
if result == -1:
    print "Not found"
else:
    print "Found", A[result], "at position", result