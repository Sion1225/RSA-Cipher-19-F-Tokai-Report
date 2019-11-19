from Eratosthenes import eratos
from Search_P import Search_P
N = 1214348893105131924078850286591990112509 #p*q (Key)
e = 65537 # (Key)
C = 23161252532832885956948212465951275785 #Cipher
#Secret key d
test_N = 20
p = eratos(test_N)
for i in range(test_N):
  print(f"{i}={p[i]}")