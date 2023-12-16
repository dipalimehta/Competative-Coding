# Dynamic Programming - 0/1 Knapsack problem

def knapsack(wt,v,C,n):
    # Base Condn
    if n==0 or C==0:
        return 0
    # Memozise
    if t[n][C] != -1:
        return t[n][C]
    # Choice diagram
    if wt[n-1]>C:
        t[n][C] = knapsack(wt,v,C,n-1)
    else:
        t[n][C] = max(
                             v[n-1] + knapsack(wt,v,C-wt[n-1],n-1),
                             knapsack(wt,v,C,n-1) 
                            )  
    return t[n][C]

# inputs
wt = [5, 4, 6, 3]
v = [10, 40, 30, 50]
n = len(wt)
C = 10

# Table initialization
t  = [[-1 for _ in range(C+1)] for _ in range(n+1)]

knapsack(wt,v,C,n)
