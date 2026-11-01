a=input("ecrire un chaine de caractaire :")
c=a.replace(" ", "").lower()
b=c[::-1]
if c==b:
    print("palindrome")
else:
    print("nest pas palindrome")