a=int(input(" donne unr annee:"))
if a%400==0:
    print("bissexitile")
elif a%4==0 and a%100!=0:
    print("bissexitile")
else:
    print("ne lest pas")