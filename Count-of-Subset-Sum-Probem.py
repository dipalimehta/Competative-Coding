t = [[-1 for _ in range(summ+1)] for _ in range(n+1)]


def cnt_subset_sum(arr,C,n):
    # Base cond
    if n == 0:
        return 1 if C == 0 else 0
    # Memoize
    if t[n][C] != -1:
        return t[n][C]
    # Choice Diagram
    if arr[n-1]>C:
        t[n][C] =  cnt_subset_sum(arr,C,n-1)
        return t[n][C]
    else:
        t[n][C] =  (cnt_subset_sum(arr,C-arr[n-1],n-1)
                    + cnt_subset_sum(arr,C,n-1))
        return t[n][C]
    

arr = [2,3,5,6,8,10]
summ = 10
n = len(arr)
cnt_subset_sum(arr,summ,n)