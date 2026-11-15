N=int(input("entre un nombre:"))
for i in range(1,N+1):
    for j in range(1,N+1):
        s=i*j
        print(s,end="\t")
    print( )