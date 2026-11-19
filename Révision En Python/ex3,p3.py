a=float(input("entre la note :"))
if a>20:
    print("error")
elif a<0:
    print("error")
elif a>=16:
    print("Excellent")
elif 16>a>=14:
    print("Bien")
elif 14>a>=12:
    print("Assez bien")
elif 12>a>=10:
    print("Passable")
else:
    print("Non admis")



