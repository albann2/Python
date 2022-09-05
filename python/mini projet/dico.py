from multiprocessing import Value
from operator import truediv
from pickle import FALSE
from typing import Counter

def casse(t):
    l=list(t)
    for i in range(0,len(l)):
        l[i]=l[i].lower()
    return "".join(l)
def anagrame(a,b):
    l1=list(a)
    l2=list(b)
    if set(l1).issubset(set(l2)) or set(l2).issubset(set(l1)):
        return True
    return False
FR_ewo={
    "abam":"planche","aban":"arbre forestier, iroko","abe":"méchanceté, méchant, mauvais","abè":"mamelle, cuisse",
    "abemba":"étable de mouton","abenge":"cloche","abia":"jeu de hasard","abim":"mesure,quantité",
    "abok":"temps,saison,duréé","abom":"coup de baton","abon":"genoux, jointure, coude","abot":"petitesse, petit",
    "abuda":"patate douce","abui":"grand nombre, beaucoup","abui biyon":"beaucoup de fois, souvent",
    "abum":"ventre","ane abum":"elle est enceinte","adit":"poids,lourd","adzab":"arbre qui a des fruits huilleux",
    "afab":"aile","afan":"foret","afeb":"feuille,morceau de papier","afib":"épais, fort(étoffes)","afub":"champ, plantation",
    "afum":"couleur blanche, blanc","afu-nnem":"consolant,bienveillant,bienveillance","akab":"générosité, généreux",
    "aken":"ruse, malin","aki":"oeuf","aki kub":"oeuf de poule","akoe":"avarice, avare","akok":"pierre, rocher",
    "ako":"jambe, pied","akol":"jambe, pied","akon":"lance","akon nga":"balle de fusil","akon kalara":"plume à écrire",
    "akuda":"nombre trés grand","akuma":"riche, fortune","akut":"folie, fou","akyaè":"sorte, espèce","alabinda":"parfum",
    "alen":"palmier","alo":"oreille","bo melo":"désobéir","alu":"nuit","melu mebè ana":"depuis deux jours",
    "amvu melu metan":"après cinq nuits(le 6e jour)","aluk":"le mariage","luk":"épouser","aman":"joue","amos":"jour",
    "amu":"parce que...","amvus":"après, derrière","ana":"aujourd'hui","melu mebè ana":"après deux nuits(le 3e jour)",
    "anè":"comme","ane":"chaque","ane mot abele fek dzie":"chaque homme a son idée","anen":"grandeur, grand","angoge":"hier",
    "anyu":"bouche","asimba":"miracle, merveilleix","ason":"dent","aso":"chique","asu":"1)visage, front 2)pour",
    "asu dam":"pour moi","asub":"cendre","asuk":"lenteur d'esprit, sot","asye":"sorte d'acajou","atek":"paresse, paresseux",
    "atin":"promesse, noeud","lik metin":"faire des promesses","buk metin":"manquer à sa promesse","aveb":"froid","aven":"blessure",
    
}
print("\n DICTIONNAIRE FRANCAIS-EWONDO\n")
for key,value in FR_ewo.items():
    print("{} : {}".format(key,value))
print("\n1-FRANCAIS vers EWONDO\n2-EWONDO vers FRANCAIS\n")
a=str(input("entrer un choix : "))
if a=="1":
    s=str(input("\nentrer un mot à traduire : "))
    s=casse(s)
    i=0
    for key,value in FR_ewo.items():
        if s==value:
            print("la traduction de {} est {}".format(s,key))
            break
        elif(anagrame(s,value)):
            print("la traduction de {} est {}".format(value,key))
            i=1
            if(i != 1):
                    print("valeur abscente dans le dictionnaire")
elif a=="2":
    s=str(input("\nentrer un mot à traduire : "))
    s=casse(s)
    i=0
    for key,value in FR_ewo.items():
        if s==key:
            print("la traduction de {} est {}".format(key,value))
            break
        else:
            if(anagrame(s,key)):
                print("la traduction de {} est {}".format(key,value))
                i=1
            if(i != 1):
                    print("valeur abscente dans le dictionnaire")
else:
    print("choix incorrect")
#Counter
#sorted
#def anagrame(a,b):
#    if Counter(a)==Counter(b):
#        return True
#    else:
#        return False