class banque():
    def __init__(self,Num,Nom,Sold):
        self.num=Num
        self.nom=Nom
        self.solde=Sold
    def versement(self,montant,nom,num):
        if(nom==self.nom | num==self.num):
            self.solde+=montant
        else :
            print("compte inexitant")
    def retrait(self,montant,num):
        if(num==self.num & self.solde>=montant):
            self.solde-=montant
        else :
            print("solde insiffisant")
    def afficher(self,num):
        if(num==self.num):
            print('\n')
            print('nnuméro de compte :',self.num)
            print("nom :",self.nom)
            print('solde :',self.solde)
        else :
            print("compte inexitant")
    def transaction(self,dest,montant):
        if (nom==self.nom | num==self.num)&(self.solde>=montant):
            dest.versement(montant,nom,num)
            self.solde-=montant
r="O"
i=0
while r=="O" or r=="o" or r=="oui" or r=='Oui':
    print("***Bienvenue à ApyBank***\n\n\n")
    r=int(input("***Que pouvons nous faire pour vous ?***\n\n1-Creer un compte\n2-Effectuer un depot\n3-Effectuer un retrait\n4-Voir ses informations\n\nchoix : "))
    if(r==1):
        Nom=str(input("entrer votre nom\n"))
        Sold=0
        import random
        Num=random.randint(0, i)
        client=banque(Num,Nom,Sold)
        client.afficher(Num)
        i=i+1
    elif(r==2):
        a=str(input("entrer le nom du beneficieur : "))
        b=str(input("entrer le numero de compte du beneficieur : "))
        c=int(input("entrer le montant du depot : "))
        client.versement(c,a,b)
        client.afficher(Num)
    r=str(input("refaire une opération ? O or N \n"))
print("Merci pour votre fidélité à ApyBank")