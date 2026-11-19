N=int(input("enter ur wanted number= "))
total = 0
if N < 2 : 
    print("ur number needs to be higher than 2")
else : 
    for i in range(2,N+1):
        counter = 0
        for j in range (1,i+1):
            if i%j == 0:
                counter +=1
        if counter == 2 : 
            total +=1
         
        
print(total)


