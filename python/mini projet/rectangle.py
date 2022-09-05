class rectangle:
    def __init__(self,long,larg):
        self.L=long
        self.l=larg
    def affiche(self):
        print('la longueur est',self.L,'\n')
        print('la largeur est',self.l,'\n')
    def perimetre(self):
        p=(self.l+self.L)*2
        print('le périmetre est',p)
    def surface(self):
        s=self.l*self.L
        print('la suface est',s)
class parallelipipede(rectangle):
    def __init__(self,haut,long,larg):
        super().__init__(long,larg)
        self.h=haut
    def volume(self):
        v=self.h*self.L*self.l
        print('le volume est',v)
rectangle1=rectangle(10,15)
rectangle1.affiche()
rectangle1.perimetre()
rectangle1.surface()
rectangle1=parallelipipede(10,15,14)
rectangle1.volume()
