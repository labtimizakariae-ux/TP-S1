a=int(input("Write number:"))
if a>0:
 s=0
 for i in range(1,a):
  if a%i==0:
   s=s+i
   print(i)
 if s==a:
  print("a est un nomre parfais")
 else:
  print("a est un nombre non parfi")
else:
 a<=0
 print("errur")
  
  
