t = [[-1 for _ in range(C+1)] for _ in range(n+1)]

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

def equal_sum_partition(arr,summ,n):
    if summ % 2 == 0 :
        return subset_sum(arr,summ//2,n)
    else:
        return False


# inputs
arr = [1,5,11,5]
n = len(arr)
summ = sum(arr)

# Func call
equal_sum_partition(arr,summ,n)