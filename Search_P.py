from math import sqrt

def Search_P(N) :
    n=sqrt(N)
    n=int(n)
    for i in range(2,n):
        if N % (n-i) == 0 :
            prime = n-i
            break
    
    return prime
