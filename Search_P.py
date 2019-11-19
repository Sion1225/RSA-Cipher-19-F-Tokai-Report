def Search_P(N) :
    prime=[]
    for i in range(2,N):
        if N % i == 0 :
            prime.append(i)
            break
    
    return prime
