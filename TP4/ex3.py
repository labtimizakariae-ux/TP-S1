ch=input("entre une chaine de caractaire:")
if ch=="":
    print("la chaine est vide")
else:
 r=""
 c=1
 for i in range(1,len(ch)):
    if ch[i]==ch[i-1]:
        c=c+1
    else:
        r=r+ch[i-1]+str(c)
        c=1
 r=r+ch[-1]+str(c)
 print(r)
 