a=str(input("entrer votre nom "))
b=str(input("entrer votre e-mail "))
c=str(input("entrer votre mot de passe "))
if (a!='alban happi' & b!='albanhappi@gmail.com' and c!='happi1234'):
    print("\n")
    print("syntaxe error")
else :
    print("\n")
    print("valide")
print("\n")
if a!='alban happi':
    print("erreur au niveau du nom")
if b!='albanhappi@gmail.com':
    print("erreur au niveau de l'e-mail")
if c!='happi1234':
    print("erreur au niveau du mot de passe")