a=input("entre une chaîne principale:").upper()
b=input("entre une sous-chaîne:").upper()
c=False
for i in range(len(a)-len(b)+1):
    d=True
    for h in range(len(b)):
        if a[i+h] != b[h]:
           d = False 
    if d:
       print("Motif trouve a la position",i+1)
       c = True

if c== False:
   print("motif no trouve ") 


  
    