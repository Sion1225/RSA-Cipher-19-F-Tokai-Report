from math import sqrt

def eratos(N) :
  n=sqrt(N) #routin's max
  prime=[True for a in range(int(N)+1)] #Eratosthenes True is prime number

  prime[0] = False
  prime[1] = False

  for i in range(2,int(n)+1) :
    if(prime[i] is not False):
      for j in range(i,N) :
        if i*j >= N:
          break
        prime[i*j] = False

  return prime
