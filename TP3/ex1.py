N=int(input("entre le nombre N:"))
while N <= 0:
 print("entre un outre nombre un entier naturel:")
 N=int(input("entre le nombre N:"))
s=0.0
for i in range(1,N+1):
  s= 1/i
  print("la somme est:",s)