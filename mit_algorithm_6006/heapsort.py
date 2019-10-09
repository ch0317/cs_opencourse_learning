heap_size = 0

def PARENT(i):
    return int(i / 2)

def LEFT(i):
    return 2 * i

def RIGHT(i):
    return 2 * i + 1

def MAX_HEAPIFY(A, i):
    global heap_size
    l = LEFT(i)
    r = RIGHT(i)
    print("i=%d, l=%d, r=%d" % (i,l,r))
    if l <= heap_size and A[l - 1] > A[i - 1]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r - 1] > A[largest - 1]:
        largest = r

    #print("largest %d, %d" % (largest,  A[largest - 1]))

    if largest != i:
        #print("exchange %d %d" % (A[i - 1] , A[largest - 1]))
        temp = A[i - 1]
        A[i - 1] = A[largest - 1]
        A[largest - 1] = temp

        MAX_HEAPIFY(A,  largest)

        
def BUILD_MAX_HEAP(A):
    global heap_size
    heap_size = len(A)
    print("heap size: %d" % heap_size)
    for i in range(int(len(A) / 2), 0, -1):
        print(i)
        MAX_HEAPIFY(A, i)
        print(A, i)

def HEAPSORT(A):
    global heap_size
    BUILD_MAX_HEAP(A)
    print(A[0])
    for i in range(len(A), 1 , -1):
        temp = A[0]
        print("exchange %d %d" % (A[0], A[i - 1]))
        A[0] = A[i - 1]
        A[i - 1] = temp
        heap_size = heap_size - 1
        MAX_HEAPIFY(A, 1)
        
A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(A)
HEAPSORT(A)
print(A)
