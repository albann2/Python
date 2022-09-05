print('\n********JEUX DES DEVINETTES**********\n')
print('choisisez le numéro de votre enigme')
c="O"
i=0
while c=="O" or c=="o" or c=="oui" or c=='Oui':
    s=str(input("1-le nom et l'action\n2-je tombe une fois dans l'année\n3-Haute mer\n4-Bob...\n5-musique\n6-quelque chose d'abstrait\n7-je suis trés souvent avec toi\n8-autre sortie\n9-l'armée des 25\n10-effroi\n\n"))
    v=5
    if s=="1":
        while v!=0 :
            print("Qu'est-se-qui est jaune et qui attend ?\n")
            r=str(input("biensur que c'est...?\n"))
            if r=='johnatan' or r=='jonathan' or r=='jonatan':
                print('reussi\n')
                i=i+1
                v=0
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***johnatan***\n')
    if s=='2':
        while v!=0 :
            print("Aussi beau qu'un lever de soleil, aussi delicat que le brume matinale, la poussière d'ange qui tombe des étoiles peut changer la terre en une lune gelée\n")
            r=input("Qui suis-je ?\n")
            if r=='neige' or r=='grele' or r=='glace':
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***neige***\n')
    if s=='3':
        while v!=0 :
            print("Amie du vent, je fais avancer les choses \n")
            r=input("Qui suis-je ?\n")
            if r=='voile':
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***voile***\n')
    if s=='4':
        while v!=0 :
            print("Je bois de l'eau mais ne l'avale pas \n")
            r=input("Qui suis-je ?\n")
            if r=='eponge' or r=='éponge' or r=="èponge":
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***éponge***\n')
    if s=='5':
        while v!=0 :
            print("J'ai six clé sans serrures. Si tu me grattes je murmure \n")
            r=input("Qui suis-je ?\n")
            if r=='guitare':
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***guitare***\n')
    if s=='6':
        while v!=0 :
            print("Plus je suis grande, moins on me voit. \n")
            r=input("Qui suis-je ?\n")
            if r=='verité' or r=="vérité" or r=="verite":
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***vérité***\n')
    if s=='7':
        while v!=0 :
            print("L’accepter revient à tout refuser. Le refuser revient à tout accepter. \n")
            r=input("Qui suis-je ?\n")
            if r=='doute' :
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***doute***\n')
    if s=='8':
        while v!=0 :
            print("Vieille invention, je permets aux gens de voir à travers les murs. \n")
            r=input("Qui suis-je ?\n")
            if r=='fenetre' :
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***FENÊTRE***\n')
    if s=='9':
        while v!=0 :
            print("Je suis un général à la tête d’une armée et sans moi, Paris serait pris. \n")
            r=input("Qui suis-je ?\n")
            if r=='A' or r=="a" :
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***la lettre <<A>>***\n')
    if s=='10':
        while v!=0 :
            print("On me jette souvent quand je suis mauvais \n")
            r=input("Qui suis-je ?\n")
            if r=='un sort' or r=="sort" :
                print('reussi\n')
                v=0
                i=i+1
            else :
                print('echec essayez encore\n')
                print("il vous reste")
                v=v-1
                print(v)
                print("chance\n")
        if v==0:
            print('la reponse étais ***un sort***\n')
    c=str(input("refaire une opération ? O or N \n"))
print("vous avez un total de {}".format(i))
print("Fin")