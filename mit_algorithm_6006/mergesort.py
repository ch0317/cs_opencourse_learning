
def merge(L, R, A):
    nL = len(L)
    nR = len(R)
    i = 0
    j = 0
    k = 0

    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i < nL:
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < nR:
        A[k] = R[j]
        j = j + 1
        k = k + 1

def MergeSort(A):
    n = len(A)
    print("len=%d" % n)
    if n < 2:
        return
    mid = int(n / 2)
    left = A[0 : mid]
    print(left)
    right = A[mid :: ]
    print(right)

    MergeSort(left)
    MergeSort(right)
    merge(left,right,A)


A = [1,3,7,2,5,9,2,2,4,1,12,4,5,6]
MergeSort(A)
print(A)
