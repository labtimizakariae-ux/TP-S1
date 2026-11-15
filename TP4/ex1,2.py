nombre=int(input("entre un nombre:"))
for h in range(1,nombre+1):
   b=0
   for i in range(1,h):
      if h%i==0:
        b=b+i
   if b==h:
    print(h)
    
        
 