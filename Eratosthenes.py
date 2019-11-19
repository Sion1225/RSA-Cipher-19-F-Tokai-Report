from math import sqrt

def eratos(N) :
  n=sqrt(N) #routin's max
  prime=[N]
  prime.insert(0,False)
  prime.insert(1,False)
  for i in range(int(n)) :
    if(prime[i] is not False):
      j=i*i
      while j<N :
        prime.insert(j,False)
        j=j+i
  return prime