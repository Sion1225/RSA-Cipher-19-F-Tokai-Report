from Eratosthenes import eratos
from Search_P import Search_P
from Extanded_Euclidean import Ex_eu
N = 1214348893105131924078850286591990112509 #p*q (Key)
e = 65537 # (Key)
C = 23161252532832885956948212465951275785 #Cipher
#p = 34442988190330466543
#q = 35256781043348862163
#Secret key d
# m = c^d mod N
#test_N = 1209
p = Search_P(N)
q = N / p
d = Ex_eu(e,(p-1)*(q-1)) #x=d
print(f"Secret key d is {d}")
m = pow(C,d,N)
print(f"Plaintext m is {m}")