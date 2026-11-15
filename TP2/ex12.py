import math
a=float(input("Write the number a:"))
b=float(input("Write the number b:"))
c=float(input("write the numbre c:"))
if a==0:
 if b==0:
   if c==0:
     print("R")
   else:
     print("the equation has not solution")
 else:
    print("the solution to the equation is X=:",-c/b )
else:
 H=b**2-4*a*c
 if H==0:
  print("the solution to the equation is X=",-b/(2*a))
 elif H>0:
  print(" the solution to the equation is X1=",(-b+math.sqrt(H))/(2*a))
  print("X2=",(-b-math.sqrt(H))/(2*a))
 else:
  print(" the equaton has not solution")