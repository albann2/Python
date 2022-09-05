r="O"
while r=="O" or r=="o" or r=="oui" or r=='Oui':
    print('\n**********CALCULATRICE**********\n')
    print("choisissez votre operation\n")
    s=str(input("1-division\n2-multiplication\n3-sousutraction\n4-addition\n5-modulo\n\n"))
    a=int(input("entrer la premiere valeur "))
    b=0
    if s=='1':
        while b==0:
            b=int(input("entrer la deuxieme valeur differente de zero"))
    else :
        b=int(input("entrer la deuxieme valeur "))
    if s=="4" :
        c=a+b
    elif s=="3":
        c=a-b
    elif (s=="2"):
        c=a*b
    elif s=='1' :
        c=a/b
    elif s=='5':
        c=a%b
    else:
        print("syntaxe error")
    if s=="1" or s=="2" or s=="3" or s=="4" or s=="5" :
        print("la solution est")
        print(c)
    r=str(input("refaire une opération ? O or N \n"))
print("Fin")