a = float(input("saisir la quantité achetée:"))
b = float(input("saisir le prix unitaire:"))
c = 15/100
d=a*b
print("le prix total avant réduction",d)
print("le montant de la réduction",c*d)
print("le prix final à payer",d-c*d)
