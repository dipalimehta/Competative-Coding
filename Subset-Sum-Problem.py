

def subset_sum(arr,C,n):
    # Base cond
    if n==0:
        return False
    # Memoize
    if t[n][C] != -1:
        return t[n][C]

    # Choice Diagram
    if arr[n-1]==C:
        return True
    
    elif arr[n-1]>C:
        t[n][C] = subset_sum(arr,C,n-1)
        return t[n][C]
    else:
        t[n][C] = (subset_sum(arr,C-arr[n-1],n-1)
                  or
                  subset_sum(arr,C,n-1))
        return t[n][C]
        

# inputs 
arr = [3, 34, 4, 12, 5, 2]
C = 9 
n = len(arr)

# Initialization of table
t = [[-1 for _ in range(C+1)] for _ in range(n+1) ]


# Func call
subset_sum(arr,C,n)