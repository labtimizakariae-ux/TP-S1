nombre=int(input("entre un nombre:"))
b=0
for i in range(1,nombre):
    if nombre%i==0:
        b=b+i
if b==nombre:
    print("le nombre parfait")
else:
    print("le nombre ne pas marfait")

    
    