texte = input("Donner la chaine principale : ").upper()
motif = input("Donner le motif : ").upper()
if motif in texte :
    print("Motif trouve a la position")
else:
    print("motif no trouve")